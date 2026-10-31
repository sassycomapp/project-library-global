#!/usr/bin/env bash
# Mybizz test suite: the local runtime of one Anvil app (test PR-09).
#
# Starts the Anvil App Server on an empty database, with the local mail
# catcher, and runs test commands with the app's .env loaded. The values in
# .env are loaded into the environment of the processes started here and are
# never printed, so an agent that runs this script never reads them.
#
# Usage (WSL):
#   bash ts_local.sh APP_FOLDER init           the developer only: write .env with new local keys
#   bash ts_local.sh APP_FOLDER start         start the runtime on an empty database
#   bash ts_local.sh APP_FOLDER stop           stop it
#   bash ts_local.sh APP_FOLDER run COMMAND... run a command with .env loaded
#
# Example:
#   bash ts_local.sh /mnt/c/dev/dev-mb-3-cs/mb-3-cs-app1 run pytest tests/integration -m local
#
# The runtime serves the app at http://localhost:3030, the server and client
# Uplink connections at ws://localhost:3030/_/uplink, and catches every email
# the app sends in /tmp/mybizz-runtime/{app folder name}/mail.
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: bash ts_local.sh APP_FOLDER init|start|stop|run COMMAND..." >&2
  exit 2
fi

APP_DIR=$(realpath "$1")
ACTION=$2
shift 2

VENV="$HOME/mybizz-test-tools/venv"
RUN="/tmp/mybizz-runtime/$(basename "$APP_DIR")"
PORT=3030
MAIL_PORT=8025

load_env() {
  if [ ! -f "$APP_DIR/.env" ]; then
    echo "No .env in $APP_DIR; Step 11 creates it." >&2
    exit 1
  fi
  set -a
  # shellcheck disable=SC1091
  . "$APP_DIR/.env"
  set +a
}

stop_runtime() {
  for name in app-server mail; do
    if [ -f "$RUN/$name.pid" ]; then
      pid=$(cat "$RUN/$name.pid")
      # The App Server launcher's Java child outlives it unless killed too.
      pkill -P "$pid" 2>/dev/null || true
      kill "$pid" 2>/dev/null || true
      rm -f "$RUN/$name.pid"
    fi
  done
  # The runtime owns these ports alone; make sure a start begins ports-free
  # even when an orphaned child from an older run still holds one.
  for port in "$PORT" "$MAIL_PORT" 2525; do
    fuser -k "${port}/tcp" 2>/dev/null || true
  done
}

case "$ACTION" in
  init)
    # Run by the developer, never by an agent: writes the app's .env with
    # new random local keys and a test password. Refuses to overwrite.
    if [ -e "$APP_DIR/.env" ]; then
      echo "$APP_DIR/.env already exists; nothing written." >&2
      exit 1
    fi
    umask 077
    printf 'TS_TARGET=local\nTS_UPLINK_URL=ws://localhost:%s/_/uplink\nANVIL_UPLINK_KEY=%s\nANVIL_CLIENT_KEY=%s\nTS_TEST_PASSWORD=%s\nTS_ROLE_COLUMN=role\n' \
      "$PORT" "$(openssl rand -hex 24)" "$(openssl rand -hex 24)" "$(openssl rand -hex 16)" > "$APP_DIR/.env"
    echo "Wrote $APP_DIR/.env (values not shown)."
    ;;
  start)
    [ -f "$APP_DIR/anvil.yaml" ] || { echo "$APP_DIR holds no anvil.yaml" >&2; exit 1; }
    load_env
    stop_runtime
    for port in "$PORT" "$MAIL_PORT" 2525; do
      if fuser "${port}/tcp" >/dev/null 2>&1; then
        echo "Port $port is still in use after stop; nothing started." >&2
        exit 1
      fi
    done
    rm -rf "$RUN"
    # The mail catcher builds no Maildir folders inside a folder that exists.
    mkdir -p "$RUN/data" "$RUN/mail/tmp" "$RUN/mail/new" "$RUN/mail/cur"
    chmod 700 "$RUN"

    # The App Server reads its keys from a config file only this user can read.
    umask 077
    printf 'uplink-key: "%s"\nclient-uplink-key: "%s"\n' \
      "$ANVIL_UPLINK_KEY" "$ANVIL_CLIENT_KEY" > "$RUN/anvil.conf.yaml"

    nohup "$VENV/bin/python" -m aiosmtpd -n -l "127.0.0.1:$MAIL_PORT" \
      -c aiosmtpd.handlers.Mailbox "$RUN/mail" > "$RUN/mail.log" 2>&1 &
    echo $! > "$RUN/mail.pid"

    # The server takes the app's package name from the directory it is given,
    # so serve the app through a package-named link in the runtime folder.
    # Dependencies are cloned at the tag the app declares into directories
    # adjacent to that link (the App Server's documented layout) and mapped
    # with --dep-id keyed by dep_id; GitHub addresses come from the app's
    # tests/ts-config.yaml (dependency_sources).
    PLAN=$(TS_APP_DIR="$APP_DIR" TS_RUN="$RUN" "$VENV/bin/python" <<'PYEOF'
import os, re, subprocess, sys
import yaml

app_dir = os.environ["TS_APP_DIR"]
run = os.environ["TS_RUN"]
with open(os.path.join(app_dir, "anvil.yaml")) as f:
    doc = yaml.safe_load(f)
pkg = doc.get("package_name") or re.sub(r"[^A-Za-z0-9_]", "_", os.path.basename(app_dir))

sources = {}
cfg = os.path.join(app_dir, "tests", "ts-config.yaml")
if os.path.exists(cfg):
    with open(cfg) as f:
        sources = (yaml.safe_load(f) or {}).get("dependency_sources") or {}

flags = []
for dep in doc.get("dependencies") or []:
    dep_id = dep.get("dep_id")
    hints = dep.get("resolution_hints") or {}
    app_id = hints.get("app_id")
    name = hints.get("package_name")
    tag = (dep.get("version") or {}).get("version_tag")
    url = sources.get(app_id)
    if not all([dep_id, name, tag, url]):
        print(f"ts_local: cannot wire dependency {dep_id}: "
              f"missing package name, tag or GitHub source", file=sys.stderr)
        continue
    dest = os.path.join(run, name)
    if subprocess.run(["git", "clone", "--quiet", "--depth", "1",
                       "--branch", tag, url, dest]).returncode != 0:
        sys.exit(f"ts_local: cloning {name} at {tag} failed")
    flags += ["--dep-id", f"{dep_id}={name}"]

print(pkg)
print(" ".join(flags))
PYEOF
    )
    PKG=$(printf '%s\n' "$PLAN" | head -1)
    read -r -a DEP_FLAGS <<< "$(printf '%s\n' "$PLAN" | tail -1)"
    ln -sfn "$APP_DIR" "$RUN/$PKG"

    nohup "$VENV/bin/anvil-app-server" \
      --config-file "$RUN/anvil.conf.yaml" \
      --app "$RUN/$PKG" \
      --data-dir "$RUN/data" \
      --auto-migrate \
      --ip 127.0.0.1 \
      --port "$PORT" \
      --origin "http://localhost:$PORT" \
      --smtp-host 127.0.0.1 \
      --smtp-port "$MAIL_PORT" \
      --smtp-server-port 2525 \
      "${DEP_FLAGS[@]}" \
      > "$RUN/app-server.log" 2>&1 &
    echo $! > "$RUN/app-server.pid"

    for _ in $(seq 1 180); do
      if curl -s -o /dev/null "http://localhost:$PORT"; then
        echo "Local runtime started: http://localhost:$PORT (log: $RUN/app-server.log)"
        exit 0
      fi
      if ! kill -0 "$(cat "$RUN/app-server.pid")" 2>/dev/null; then
        echo "The App Server stopped; see $RUN/app-server.log" >&2
        exit 1
      fi
      sleep 1
    done
    echo "The App Server did not answer within 180 seconds; see $RUN/app-server.log" >&2
    exit 1
    ;;
  stop)
    stop_runtime
    echo "Local runtime stopped."
    ;;
  run)
    [ $# -ge 1 ] || { echo "run needs a command" >&2; exit 2; }
    load_env
    export TS_MAIL_DIR="$RUN/mail"
    export PATH="$VENV/bin:$PATH"
    cd "$APP_DIR"
    exec "$@"
    ;;
  *)
    echo "Unknown action: $ACTION (init, start, stop or run)" >&2
    exit 2
    ;;
esac
