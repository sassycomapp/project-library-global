---
title: "spec-client-instance-hosting"
doc-id: "mb-0a52a7a2"
updated: "2026-11-11"
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
| App 4 — each client instance | DigitalOcean App Platform (one container per client) and DigitalOcean Managed PostgreSQL (one database per client) |
| App 5 — `{Product}_management` | Mybizz's Anvil Business account |

- Every client instance runs on the Anvil App Server, the open-source Anvil runtime (`anvil-works/anvil-runtime`). Its licence is the GNU Affero General Public License with Anvil's exception: applications run by it keep their own licence. Mybizz runs the App Server unmodified.
- DigitalOcean runs the servers, operating-system security updates, container restarts, failover and database backups. Mybizz runs no server of its own.
- Each Mybizz business has its own DigitalOcean project, holding its own database cluster, its own registry repository, its own test client instance and its client containers.
- Region: London (`LON1`) for every container and every cluster, next to Amazon SES in `eu-west-1`.
- The demo instances (`demo.mybizz.live`, `try.mybizz.live`) run on Mybizz's Anvil Business account.

---

## 2. The Release Image

Every client container runs the same image, built once per release. The image holds:

- the Anvil App Server, at the one version Mybizz pins; every App Server upgrade is the developer's decision and passes the full test suite first;
- App 3, the client app: the startup module, the full table definitions, the scheduled tasks and the Users service settings;
- App 2, `master_template`, and the `m3` theme, each joined to App 3 by its dependency ID;
- the Python version and every Python package App 2 needs, matching App 1's server environment.

The image is defined in the business's code repository `{slug}-app4`, which holds the image definition (`Dockerfile`), the container start script, the release checks (section 6) and the image build workflow. It holds no application code.

Each built image is stored in DigitalOcean Container Registry under its release tag (`vMAJOR.MINOR.PATCH`). The registry keeps the last three release images of each business.

---

## 3. The Container

- One DigitalOcean App Platform app per client, named `[client-name]-{vertical}`, with one container of size `apps-s-1vcpu-1gb`: 1 shared vCPU and 1 GiB memory.
- The start script caps the App Server's Java memory at 400 MB (`JAVA_TOOL_OPTIONS=-Xmx400m`). The rest of the container's memory is left for the Python processes that run the server code, the background tasks and the PDF building, so the container's memory use stays predictable.
- Each client's app has an App Platform alert that fires when the container's memory use passes 80%. The alert goes to App 5, which raises that client's container to `apps-s-1vcpu-2gb` (1 shared vCPU, 2 GiB memory, $25 a month, £18.75) and messages the developer. 2 GiB is the largest size App 5 chooses ([[[default:adr-global/adr-automatic-resizing]]](C:/dev/project-library-global/adr-global/adr-automatic-resizing.md)).
- The size is raised for one client by a setting change; the client keeps its address and its data.
- App Platform provides the client's HTTPS certificate on the client's own domain.

### App Server settings

Each container starts the App Server with these settings, held as encrypted App Platform environment values:

| Setting | Value |
|---|---|
| `database` | The client's own database in the business's cluster, over TLS with full certificate verification (`sslmode=verify-full`), with `prepareThreshold=0` so the App Server works through DigitalOcean's connection pooler in any pooling mode |
| `db-connection-pool-size` | 3 |
| `auto-migrate` | On. Off after a rollback, until the next release |
| `ignore-invalid-schema` | Off. On after a rollback, until the next release |
| `origin` | `https://` and the client's own domain |
| `disable-tls` | On |
| `secret` | `encryption_key`, the Vault's master key ([[[default:specifications-global/spec-vault-system\|The Vault System]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md)) |
| `smtp-host`, `smtp-port`, `smtp-encryption`, `smtp-username`, `smtp-password` | `email-smtp.eu-west-1.amazonaws.com`, port `587`, STARTTLS, and the client's scoped SES SMTP credentials |
| `google-*`, `microsoft-*`, `facebook-*` | Mybizz's own sign-in keys, for each sign-in method the application uses |

### Container keys

The App Server keeps two keys in its data folder: `secret.key` and `anvil-live-object-key.txt`. A container keeps no files across restarts. Each client's two keys are created once, at provisioning, held as encrypted environment values, and written into the data folder by the start script before the App Server starts. The keys stay the same through every restart and release.

### What runs in the container

- Every server function, form and background task, from App 2.
- Every scheduled task, from App 3, with no timeout.
- The management endpoints, the webhook endpoints and the inbound email endpoint `/_/api/email/inbound`.
- The heartbeat to App 5 every 15 minutes, carrying the client's database size and its AI and voice spend for the month ([[[default:adr-global/adr-mybizz-management-visibility|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)).
- AI and voice metering and the AI request rate limit of [[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md).

Each container's output is kept in DigitalOcean's log view. The instance's own `error_log`, `health_log` and `activity_log` tables carry the application's records ([[[default:adr-global/adr-observability-architecture|Observability Architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md)).

---

## 4. The Database

- One DigitalOcean Managed PostgreSQL cluster per business, in `LON1`, PostgreSQL version 18. The cluster grows in four stages with the business's client count (Capacity, below). A cluster's edition is fixed when it is created; its size can be raised at any time.
- The cluster holds one database per client, each with its own database user that can reach only that client's database.
- Each client database user is created with a connection limit of 3, a statement timeout of 60 seconds and an idle-in-transaction timeout of 120 seconds ([[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md)). PostgreSQL enforces these limits itself.
- Client database users and their limits are created by the provisioning job, which runs inside DigitalOcean, because the cluster accepts connections from inside DigitalOcean only.
- **Trusted sources:** the cluster accepts connections only from the business's client containers and its test client instance.
- DigitalOcean runs the cluster's patching, daily backups kept for 7 days, point-in-time recovery and TLS.
- From client 25 the cluster is Advanced Edition with a standby node, which takes over automatically when the main node fails. Before client 25 the cluster is Standard Edition, which cannot have a standby: if its node fails, DigitalOcean restores the cluster from its backups, and clients may be offline for up to a few hours.
- **Storage autoscaling** is on: DigitalOcean adds storage before the disk fills, at $0.12 (£0.09) per GiB per month.
- **Maintenance window:** Sunday 06:00 UK time (07:00 Europe, 01:00 New York, Saturday 22:00 Los Angeles).
- On first start, the App Server builds every table in the client's empty database from App 3's table definitions.

### Capacity

Each client's App Server holds at most 3 database connections. A cluster gives 25 connections per GiB of memory, less 3 kept for maintenance. Each client stores about 100 MB of data a year; files go to the client's R2 bucket.

| Stage | Business's clients | Cluster | Connections | Holds | Monthly price | GBP |
|---|---|---|---|---|---|---|
| 1 | 1 to 11 | Standard Edition, 2 GiB, one node | 47 | 15 clients | $30 | £22.50 |
| 2 | 12 to 24 | Standard Edition, 4 GiB, one node | 97 | 32 clients | $60 | £45 |
| 3 | 25 to 59 | Advanced Edition, 8 GiB, with a standby | 197 | 65 clients | $260 | £195 |
| 4 | 60 and more | Advanced Edition, 16 GiB, with a standby | 397 | 132 clients | about $520 | about £390 |

App 5 moves the cluster to each stage in the next maintenance window and messages the developer ([[[default:adr-global/adr-automatic-resizing]]](C:/dev/project-library-global/adr-global/adr-automatic-resizing.md)). Stages 2 and 4 raise the size of the same cluster. Stage 3 changes the edition, so App 5's **Rebuild** action creates the new Advanced cluster and moves every client into it, once the developer approves ([[[default:specifications-global/spec-deployment|Deployment Specification]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) section 10). The 16 GiB price is an estimate until DigitalOcean's control panel shows it.

---

## 5. Services Each Instance Uses

| Service | Supplier | Paid by |
|---|---|---|
| Email sent and received | Amazon SES, `eu-west-1` | Mybizz |
| Files, backups and history | The client's own Cloudflare R2 bucket, kept below 10 GB | Free tier, in the client's account |
| Speech-to-text | Groq Whisper, through App 5 | Mybizz |
| Invoices and quotes | PDF built on the server with `reportlab` ([[[default:adr-global/adr-pdf-invoice-generation\|PDF Invoice Generation]]](C:/dev/project-library-global/adr-global/adr-pdf-invoice-generation.md)) | — |

---

## 6. Releases

1. The developer pushes App 1's tagged release into App 2's repository (Step 42). Table changes of the release are written into App 3's table definitions.
2. The release image is built from App 2, App 3 and `m3`, and stored in the registry under the release tag.
3. The image build stops if App 3 holds any form or server module ([[[default:adr-global/adr-client-instance-readme-five-app-system|Client Instance README]]](C:/dev/project-library-global/adr-global/adr-client-instance-readme-five-app-system.md)). The table-change check compares App 3's table definitions with the previous release. The release stops if any table or column is removed, renamed or changed in type. After a business's first release, releases only add tables and nullable columns.
4. The full test suite passes on the release image.
5. The test client instance moves to the release image and passes its smoke test.
6. App 5's **Release** action, through the DigitalOcean API, points every client container to the release image. Each container restarts on it; its App Server adds the release's new tables and columns to the client's database as it starts.
7. **Staged rollout:** every release goes to the test client instance, then to 10% of clients, then to all clients. Each stage passes its health check before the next starts. A failed health check rolls that stage back automatically ([[[default:adr-global/adr-dependency-update-model|Dependency Update Model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md)).
8. **Signed images:** each release image is signed when it is built. Each client container runs the image by its digest, never by a tag, and App 5 releases only an image whose signature verifies.
9. **Registry clean-up:** at every release, images older than the last three releases are deleted and the registry's storage is cleaned.
10. **Rollback:** App 5 points the containers back to the previous release image, with `auto-migrate` off and `ignore-invalid-schema` on. The previous release then runs on the newer schema, and the App Server never removes the newer tables and columns. The next release switches `auto-migrate` back on.

---

## 7. Provisioning

### Once per business

1. A DigitalOcean project for the business, in Mybizz's DigitalOcean account.
2. The Managed PostgreSQL cluster, in `LON1`: Standard Edition, PostgreSQL 18, 2 GiB, storage autoscaling on and trusted sources set (section 4).
3. The provisioning job inside DigitalOcean (section 4).
4. The business's repository in the Container Registry.
5. The test client instance: a container and a database of its own, run as a client.
6. Two DigitalOcean access keys with custom scopes, in App 5's Vault ([[[default:security-global/cloud/sec-client-provisioning-security|Client Provisioning Security]]](C:/dev/project-library-global/security-global/cloud/sec-client-provisioning-security.md)).

### Once per client

App 5's **New client** action, after registration and the client's Cloudflare set-up ([[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)):

1. Creates the client's database and database user in the cluster, through the provisioning job, with the user's three limits (section 4).
2. Creates the client's `encryption_key`, management Bearer token and two container keys.
3. Creates the client's App Platform app from the current release image, with every setting in section 3.
4. Adds the client's domain to the app; App 5 writes the domain's DNS record through the Cloudflare API, proxied through Cloudflare with the web application firewall, DDoS protection and bot blocking switched on.
5. Starts the container; the App Server builds the client's tables.

---

## 8. Client Exit

1. The client gives notice, and the service runs to the end of the paid month; or the client has not paid 37 days after a failed renewal payment ([[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) section 5).
2. App 5 exports all the client's data into the client's own R2 bucket ([[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md)).
3. App 5's **Remove** action deletes the client's App Platform app and the client's database and database user. DigitalOcean's charges for them stop at deletion.

---

## 9. Uptime and Resilience

| Service | DigitalOcean's monthly commitment |
|---|---|
| App Platform container | 99.95% |
| Managed PostgreSQL, Advanced Edition with a standby node (from client 25) | 99.95% |
| Container Registry | 99.95% |

99.95% allows about 22 minutes of downtime a month.

- One cluster in one region serves every client of a business. A DigitalOcean failure in `LON1`, or a suspension of Mybizz's DigitalOcean account, stops every client of the business.
- Every client's data is copied to the client's own R2 bucket every night, outside DigitalOcean. Each copy is locked for its whole retention period, so no key can delete or overwrite it ([[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md)).
- **Backup check:** App 5 checks every day that each client's nightly copy arrived, with the right date and a plausible size.
- **Restore drill:** once a month, the test client instance restores one client's nightly copy into a scratch database in the cluster, compares its row counts with the source, deletes the scratch database and reports the result to App 5.
- App 5's **Rebuild** action restores every client of a business in another DigitalOcean region: a new cluster of the current stage, a database per client loaded from DigitalOcean's backups or, when those are unreachable, from its nightly copy, and a container per client from the release image ([[[default:specifications-global/spec-deployment|Deployment Specification]]](C:/dev/project-library-global/specifications-global/spec-deployment.md)). At most 24 hours of data is lost when the nightly copy is used.
- DigitalOcean Uptime checks App 5's status endpoint every minute ([[[default:adr-global/adr-observability-architecture|Observability Architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md)).

---

## 10. Conditions Before the First Paying Client

1. The full test suite passes on the release image.
2. The test client instance has run under realistic load, and its memory use and database connections are recorded against section 3 and section 4.
3. The rebuild procedure has restored the test client instance in another region.
4. The release path has run end to end: test client instance, staged rollout, rollback.
5. The App Server reconnects by itself after its database connection is cut, tested on the test client instance.
6. The cluster is at its stage of section 4, its trusted sources refuse a connection from outside DigitalOcean, and each client database user carries its three limits.

---

## 11. Monthly Cost

Suppliers bill in US dollars. Each cost is shown as billed, with its GBP figure at Mybizz's planning rate of $1 = £0.75 ([[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) section 2).

| Item | Monthly cost, billed | GBP | Basis |
|---|---|---|---|
| Anvil Business account (Apps 1, 2, 3, 5 and the demo instances) | $99 | £74.25 | Per Mybizz account |
| Container Registry, Basic plan | $5 | £3.75 | Per Mybizz account |
| Test client instance container | $12 | £9.00 | Per business |
| Client container | $12 | £9.00 | Per client |
| Managed PostgreSQL cluster | $30 to about $520 | £22.50 to about £390 | By stage (section 4) |

Revenue is shown at £79 per client; the fixed prices in the other currencies sit close to £79.

| Clients | Containers | Database | Fixed | Total cost | Revenue at £79 | Gross margin |
|---|---|---|---|---|---|---|
| 1 | £9 | £22.50 | £87 | £118.50 | £79 | −£39.50 |
| 7 | £63 | £22.50 | £87 | £172.50 | £553 | £380.50 |
| 25 | £225 | £195 | £87 | £507 | £1,975 | £1,468 |
| 50 | £450 | £195 | £87 | £732 | £3,950 | £3,218 |
| 60 | £540 | £390 | £87 | £1,017 | £4,740 | £3,723 |
| 100 | £900 | £390 | £87 | £1,377 | £7,900 | £6,523 |

Not in these figures: the usage costs per client (email, AI, voice and data transfer, budgeted at £7.60), Paddle's fee of £4.33 per £79 payment, and Mybizz-Live Ltd's company costs. Mybizz's full cost and profit figures, with break-even at 7 clients, are in [[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md).

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-five-app-architecture-model\|Five-App Architecture Model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md) | The five apps and their roles |
| [[[default:adr-global/adr-client-instance-architecture\|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) | The decision this specification carries out |
| [[[default:specifications-global/spec-deployment\|Deployment Specification]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) | Release, rollback, backup and failure procedures |
| [[[default:adr-global/adr-tiers-model\|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md) | Price and subscription terms |
| [[[default:specifications-global/spec-client-billing\|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) | How clients pay, and the exit of a client that does not pay |
