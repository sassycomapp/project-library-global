---
title: "spec-client-instance-hosting"
doc-id: "mb-0a52a7a2"
updated: "2026-11-24"
---
# Mybizz — Client Instance Hosting (Specification)

**Scope:** Mybizz-wide. Covers where and how every client instance (App 4) runs: the platform, the release image, the container, the database, releases, provisioning, exit, uptime, capacity and cost. Applies to every Mybizz business.

---

## 1. The Platform

| App | Runs on |
|---|---|
| App 1 — `{slug}-app1` | Mybizz's Anvil Business account |
| App 2 — `master_template` | Mybizz's Anvil Business account |
| App 3 — `blank_client_template` | Mybizz's Anvil Business account |
| App 4 — each client instance | A Docker container on a Mybizz Hetzner Cloud application server (one container per client), with its own database in Mybizz's Ubicloud managed PostgreSQL service (one database per client) |
| App 5 — `{Product}_management` | Mybizz's Anvil Business account |

- Every client instance runs on the Anvil App Server, the open-source Anvil runtime (`anvil-works/anvil-runtime`). Its licence is the GNU Affero General Public License with Anvil's exception: applications run by it keep their own licence. Mybizz runs the App Server unmodified, from Anvil's official `anvilworks/anvil-app-server` image.
- **Application servers:** Hetzner Cloud `CPX42` servers (x86, 8 vCPU, 16 GB memory), Ubuntu LTS, in Nuremberg (`nbg1`). Each Mybizz business has its own servers in its own Hetzner project. Mybizz runs Docker, Caddy and the provisioning runner on each server (section 7). Operating-system security updates install automatically, and a reboot an update needs happens in the Sunday 06:00 UK maintenance window. Hetzner's automatic server backups are on for every server.
- **Database:** one Ubicloud managed PostgreSQL service in Germany, on Hetzner hardware, shared by every Mybizz business, with a standby from the first client. Ubicloud runs the database's patching, backups, point-in-time recovery and failover (section 4).
- **Firewalls:** each server's Hetzner firewall allows ports 80 and 443 from anywhere and port 22 (SSH, key only) from the developer's addresses. The database's Ubicloud firewall accepts connections only from Mybizz's Hetzner servers.
- **Web addresses and certificates:** Caddy, the web server on each application server, routes each client's domain to the client's container and obtains the domain's HTTPS certificate on demand, only for domains App 5 has approved (section 3).
- The demo instances (`demo.mybizz.live`, `try.mybizz.live`) run on Mybizz's Anvil Business account. The test client instance runs on Hetzner, as a client.

---

## 2. The Release Image

Every client container runs the same image, built once per release. The image is built on Anvil's official App Server image and holds:

- the Anvil App Server, at the one version Mybizz pins; every App Server upgrade is the developer's decision and passes the full test suite first;
- App 3, the client app: the startup module, the full table definitions, the scheduled tasks and the Users service settings;
- App 2, `master_template`, and the `m3` theme, each joined to App 3 by its dependency ID;
- the Python version and every Python package App 2 needs, matching App 1's server environment.

The image is defined in the business's code repository `{slug}-app4`, which holds the image definition (`Dockerfile`), the container start script, the release checks (section 6) and the image build workflow. It holds no application code.

Each built image is stored privately in GitHub's container registry (`ghcr.io`) under its release tag (`vMAJOR.MINOR.PATCH`). The registry keeps the last three release images of each business.

---

## 3. The Container

- One Docker container per client, named `[client-name]-{vertical}`, started from the release image with a memory limit of 1 GiB and restarted by Docker whenever it stops.
- The start script caps the App Server's Java memory at 400 MB (`JAVA_TOOL_OPTIONS=-Xmx400m`). The rest of the container's memory is left for the Python processes that run the server code, the background tasks and the PDF building, so the container's memory use stays predictable.
- The provisioning runner reports each container's memory use to App 5. Above 80%, App 5 raises that container's limit to 2 GiB through the runner and messages the developer. 2 GiB is the largest size App 5 chooses ([[[default:adr-global/adr-automatic-resizing]]](C:/dev/project-library-global/adr-global/adr-automatic-resizing.md)). The client keeps its address and its data.
- **Places:** an application server holds 12 places. A 1 GiB container takes one place and a 2 GiB container takes two. The remaining memory serves the operating system, Docker, Caddy and the runner.
- **Certificates:** Caddy asks the runner before it obtains a certificate for a domain, and the runner answers yes only for a domain App 5 has approved for one of that server's clients. A client domain proxied through Cloudflare passes the certificate check through Cloudflare.
- Each container's output is kept by Docker, rotated at 10 MB with three files kept.

### App Server settings

Each container starts the App Server with these settings, held in the client's settings file on the server, readable only by the system administrator account:

| Setting | Value |
|---|---|
| `database` | The client's own database in Mybizz's Ubicloud service, over TLS with full certificate verification (`sslmode=verify-full`), with `prepareThreshold=0` so the App Server works through Ubicloud's connection pooler |
| `db-connection-pool-size` | 3 |
| `auto-migrate` | On. Off after a rollback, until the next release |
| `ignore-invalid-schema` | Off. On after a rollback, until the next release |
| `origin` | `https://` and the client's domain |
| `disable-tls` | On (Caddy ends TLS) |
| `secret` | `encryption_key`, the Vault's master key ([[[default:specifications-global/spec-vault-system]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md)) |
| `smtp-host`, `smtp-port`, `smtp-encryption`, `smtp-username`, `smtp-password` | `email-smtp.eu-west-1.amazonaws.com`, port `587`, STARTTLS, and the client's scoped SES SMTP credentials |
| `google-*`, `microsoft-*`, `facebook-*` | Mybizz's own sign-in keys, for each sign-in method the application uses |

### Container keys

The App Server keeps two keys in its data folder: `secret.key` and `anvil-live-object-key.txt`. A container keeps no files across restarts. Each client's two keys are created once, at provisioning, held in the client's settings file, and written into the data folder by the start script before the App Server starts. The keys stay the same through every restart and release.

### What runs in the container

- Every server function, form and background task, from App 2.
- Every scheduled task, from App 3, with no timeout.
- The management endpoints, the webhook endpoints and the inbound email endpoint `/_/api/email/inbound`.
- The heartbeat to App 5 every 15 minutes, carrying the client's database size and its AI and voice spend for the month ([[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)).
- AI and voice metering and the AI request rate limit of [[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md).

The instance's own `error_log`, `health_log` and `activity_log` tables carry the application's records ([[[default:adr-global/adr-observability-architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md)).

---

## 4. The Database

- One Ubicloud managed PostgreSQL service, in Germany, shared by every Mybizz business. It runs the latest PostgreSQL version Ubicloud offers at set-up, and every version upgrade is the developer's decision.
- **Standby:** one standby of the same size from the first client. Ubicloud keeps it up to date and promotes it automatically when the primary fails, so clients are back within minutes.
- The service holds one database per client, each with its own database user that can reach only that client's database.
- Each client database user is created with a connection limit of 3, a statement timeout of 60 seconds and an idle-in-transaction timeout of 120 seconds ([[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md)). PostgreSQL enforces these limits itself.
- Client databases and users are created by the provisioning runner with Mybizz's provisioning database role, which may create databases and roles and nothing else (section 7).
- **Firewall:** the service accepts connections only from Mybizz's Hetzner application servers, over TLS.
- **Backups:** Ubicloud backs up the service continuously and keeps 7 days, with restore to any minute.
- **Maintenance window:** Sunday 06:00 UK time.
- On first start, the App Server builds every table in the client's empty database from App 3's table definitions.

### Capacity

Each client's App Server holds at most 3 database connections, through Ubicloud's connection pooler. Each client stores about 100 MB of data a year; files go to the client's R2 bucket. The stage follows the number of clients of every Mybizz business together.

| Stage | Clients, all businesses | Service | Monthly price | GBP |
|---|---|---|---|---|
| 1 | 1 to 59 | `standard-2` (2 vCPU, 8 GB, 64 GB storage), with a standby | $156 | £116.22 |
| 2 | 60 to 129 | `standard-4` (4 vCPU, 16 GB, 128 GB storage), with a standby | $312 | £232.44 |
| 3 | 130 and more | `standard-8` (8 vCPU, 32 GB, 256 GB storage), with a standby | $626 | £466.37 |

App 5 raises the service to each stage through Ubicloud's API in the next maintenance window and messages the developer ([[[default:adr-global/adr-automatic-resizing]]](C:/dev/project-library-global/adr-global/adr-automatic-resizing.md)). No client moves. App 5 also messages the developer when the service's storage passes 80%.

---

## 5. Services Each Instance Uses

| Service | Supplier | Paid by |
|---|---|---|
| Email sent and received | Amazon SES, `eu-west-1` | Mybizz |
| Files, backups and history | The client's own Cloudflare R2 bucket, kept below 10 GB | Free tier, in the client's account |
| Speech-to-text | Groq Whisper, through App 5 | Mybizz |
| Invoices and quotes | PDF built on the server with `reportlab` ([[[default:adr-global/adr-pdf-invoice-generation]]](C:/dev/project-library-global/adr-global/adr-pdf-invoice-generation.md)) | — |

---

## 6. Releases

1. The developer pushes App 1's tagged release into App 2's repository (Step 42). Table changes of the release are written into App 3's table definitions.
2. The release image is built from App 2, App 3 and `m3`, and stored in the registry under the release tag.
3. The image build stops if App 3 holds any form or server module ([[[default:adr-global/adr-client-instance-readme-five-app-system]]](C:/dev/project-library-global/adr-global/adr-client-instance-readme-five-app-system.md)). The table-change check compares App 3's table definitions with the previous release. The release stops if any table or column is removed, renamed or changed in type. After a business's first release, releases only add tables and nullable columns.
4. The full test suite passes on the release image.
5. The test client instance moves to the release image and passes its smoke test.
6. App 5's **Release** action, through each server's provisioning runner, moves every client container to the release image. Each container restarts on it; its App Server adds the release's new tables and columns to the client's database as it starts.
7. **Staged rollout:** every release goes to the test client instance, then to 10% of clients, then to all clients. Each stage passes its health check before the next starts. A failed health check rolls that stage back automatically ([[[default:adr-global/adr-dependency-update-model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md)).
8. **Signed images:** each release image is signed when it is built. Each client container runs the image by its digest, never by a tag, and the runner starts only an image whose signature verifies.
9. **Registry clean-up:** at every release, images older than the last three releases are deleted.
10. **Rollback:** App 5 moves the containers back to the previous release image, with `auto-migrate` off and `ignore-invalid-schema` on. The previous release then runs on the newer schema, and the App Server never removes the newer tables and columns. The next release switches `auto-migrate` back on.

---

## 7. Provisioning

### The provisioning runner

- A small Python service, the provisioning runner, runs on every application server and connects out to App 5 through Anvil Uplink. No inbound port is opened for it.
- The runner exposes only these functions to App 5: create instance, release instance, resize container, suspend instance, resume instance, remove instance, approve domain, and report server health (each container's memory and data transfer, and the server's disk).
- Each function uses fixed commands with checked arguments; the runner never runs free-form commands.
- Each server's Uplink key and the provisioning database role's password are held on the server, readable only by the system administrator account, and in App 5's Vault ([[[default:security-global/cloud/sec-client-provisioning-security]]](C:/dev/project-library-global/security-global/cloud/sec-client-provisioning-security.md)).

### Once for Mybizz

1. The Ubicloud managed PostgreSQL service in Germany, `standard-2` with one standby, its firewall and the provisioning database role (section 4).
2. A Ubicloud API key in App 5's Vault, used only to change the service's size.

### Once per business

1. A Hetzner project for the business, with its firewall (section 1).
2. A Hetzner API key with read and write access to that project only, in App 5's Vault.
3. The first application server, created by App 5's **Add server** action: the action orders a `CPX42` through the Hetzner API with backups on, and the server's start-up script installs Docker, Caddy and the runner and joins the server to App 5.
4. The server's address added to the Ubicloud firewall.
5. The test client instance: a container and a database of its own, run as a client.

### Once per client

App 5's **New client** action, after registration and the client's Cloudflare set-up ([[[default:specifications-global/spec-client-activation-runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)):

1. Chooses the server with a free place; when the business's last server has 2 places left, App 5 runs **Add server** first.
2. Creates the client's database and database user through the runner, with the user's three limits (section 4).
3. Creates the client's `encryption_key`, management Bearer token and two container keys.
4. Creates the client's container from the current release image, with every setting in section 3.
5. Approves the client's domain on the runner; App 5 writes the domain's DNS record through the Cloudflare API, proxied through Cloudflare with the web application firewall, DDoS protection and bot blocking switched on.
6. Starts the container; the App Server builds the client's tables.

---

## 8. Client Exit

1. The client gives notice, and the service runs to the end of the paid month; or the client has not paid 37 days after a failed renewal payment ([[[default:specifications-global/spec-client-billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) section 5).
2. App 5 exports all the client's data into the client's own R2 bucket ([[[default:adr-global/adr-client-r2-storage-and-exit-handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md)).
3. App 5's **Remove** action, through the runner, deletes the client's container, settings file and domain approval, and the client's database and database user. The client's place on the server is free at once.

---

## 9. Uptime and Resilience

| Failure | Effect | Response |
|---|---|---|
| One container fails | One client | Docker restarts it; if it does not recover, App 5 recreates it from the current release image |
| One application server fails | The up to 12 clients on that server | App 5's **Rebuild server** action orders a new server through the Hetzner API and recreates each client's container from the release image. Client data is in the database, so none is lost |
| Database primary fails | Every client, for minutes | Ubicloud promotes the standby automatically |
| Hetzner location outage | Every client of the business | **Rebuild server** for each server, in Falkenstein (`fsn1`) |
| Ubicloud service lost or suspended | Every client | App 5's **Rebuild** action restores every client into a new managed PostgreSQL service from each client's nightly copy, at most 24 hours of data lost ([[[default:specifications-global/spec-deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md)) |

- Every client's data is copied to the client's own R2 bucket every night, outside Hetzner and Ubicloud. Each copy is locked for its whole retention period, so no key can delete or overwrite it ([[[default:adr-global/adr-client-r2-storage-and-exit-handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md)).
- **Backup check:** App 5 checks every day that each client's nightly copy arrived, with the right date and a plausible size.
- **Restore drill:** once a month, the test client instance restores one client's nightly copy into a scratch database, compares its row counts with the source, deletes the scratch database and reports the result to App 5.
- **Spare place:** every business keeps at least 2 free places on its servers, so a container can always be recreated at once.
- **Uptime check:** UptimeRobot checks App 5's status endpoint every 5 minutes and emails the developer on a fault ([[[default:adr-global/adr-observability-architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md)).

---

## 10. Conditions Before the First Paying Client

1. The full test suite passes on the release image.
2. The test client instance has run under realistic load, and its memory use and database connections are recorded against section 3 and section 4.
3. **Rebuild server** has replaced the test client instance's server, and **Rebuild** has restored the test client instance into a new database service from its nightly copy.
4. The release path has run end to end: test client instance, staged rollout, rollback.
5. The App Server reconnects by itself after its database connection is cut, and after a Ubicloud failover, both tested on the test client instance.
6. The database service is at its stage of section 4, its firewall refuses a connection from outside Mybizz's servers, and each client database user carries its three limits.

---

## 11. Monthly Cost

Each cost is shown with its GBP figure at Mybizz's planning rates of $1 = £0.745 and €1 = £0.834.

| Item | Monthly cost, billed | GBP | Basis |
|---|---|---|---|
| Anvil Business account (Apps 1, 2, 3, 5 and the demo instances) | — | £87.00 | Per Mybizz account |
| Application server `CPX42`, with backups and its IPv4 address | €83.89 | £69.96 | Per 12 places, per business |
| Dedicated application server `CCX33`, with backups and its IPv4 address | €166.69 | £139.02 | Per Mybizz Shop Enterprise client |
| Ubicloud managed PostgreSQL, with a standby | $156 to $626 | £116.22 to £466.37 | By stage (section 4), shared by every business |
| Release image registry | — | £0 | GitHub container registry |
| Uptime check | — | £0 | UptimeRobot free plan |

For one business, with the test client instance taking one place:

| Clients | Servers | Application servers | Database (stage) | Total |
|---|---|---|---|---|
| 10 | 1 | £69.96 | £116.22 | £186.18 |
| 50 | 5 | £349.80 | £116.22 | £466.02 |
| 100 | 9 | £629.64 | £232.44 | £862.08 |

The database is shared, so a second business adds only its own application servers until the stage changes. Not in these figures: the usage costs per client (email, AI and voice), Paddle's fee, the Anvil account and Mybizz-Live Ltd's company costs. The company's figures are in `mybizz-live-budget.xlsx`.

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-five-app-architecture-model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md) | The five apps and their roles |
| [[[default:adr-global/adr-client-instance-architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) | The decision this specification carries out |
| [[[default:specifications-global/spec-deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) | Release, rollback, backup and failure procedures |
| [[[default:adr-global/adr-tiers-model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md) | Price and subscription terms |
| [[[default:specifications-global/spec-client-billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) | How clients pay, and the exit of a client that does not pay |
