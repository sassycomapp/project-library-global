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
      kill "$(cat "$RUN/$name.pid")" 2>/dev/null || true
      rm -f "$RUN/$name.pid"
    fi
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
    rm -rf "$RUN"
    mkdir -p "$RUN/mail"
    chmod 700 "$RUN"

    # The App Server reads its keys from a config file only this user can read.
    umask 077
    printf 'uplink-key: "%s"\nclient-uplink-key: "%s"\n' \
      "$ANVIL_UPLINK_KEY" "$ANVIL_CLIENT_KEY" > "$RUN/anvil.conf.yaml"

    nohup "$VENV/bin/python" -m aiosmtpd -n -l "127.0.0.1:$MAIL_PORT" \
      -c aiosmtpd.handlers.Mailbox "$RUN/mail" > "$RUN/mail.log" 2>&1 &
    echo $! > "$RUN/mail.pid"

    nohup "$VENV/bin/anvil-app-server" \
      --config-file "$RUN/anvil.conf.yaml" \
      --app "$APP_DIR" \
      --data-dir "$RUN/data" \
      --auto-migrate \
      --ip 127.0.0.1 \
      --port "$PORT" \
      --origin "http://localhost:$PORT" \
      --smtp-host 127.0.0.1 \
      --smtp-port "$MAIL_PORT" \
      --smtp-server-port 2525 \
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
