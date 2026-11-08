---
title: "spec-client-instance-hosting"
doc-id: "mb-0a52a7a2"
updated: "2026-11-08"
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
- The size is raised for one client by a setting change; the client keeps its address and its data.
- App Platform provides the client's HTTPS certificate on the client's own domain.

### App Server settings

Each container starts the App Server with these settings, held as encrypted App Platform environment values:

| Setting | Value |
|---|---|
| `database` | The client's own database in the business's cluster, over SSL |
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
- The heartbeat to App 5 every 15 minutes ([[[default:adr-global/adr-mybizz-management-visibility|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)).

Each container's output is kept in DigitalOcean's log view. The instance's own `error_log`, `health_log` and `activity_log` tables carry the application's records ([[[default:adr-global/adr-observability-architecture|Observability Architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md)).

---

## 4. The Database

- One DigitalOcean Managed PostgreSQL cluster per business, in `LON1`. It holds one database per client, each with its own database user that can reach only that client's database.
- DigitalOcean runs the cluster's patching, daily backups kept for 7 days, point-in-time recovery and SSL.
- The cluster has a standby node from the first paying client. The standby takes over automatically when the main node fails.
- On first start, the App Server builds every table in the client's empty database from App 3's table definitions.

### Capacity

Each client's App Server holds at most 3 database connections. A cluster gives 25 connections per GiB of memory, less 3 kept for maintenance. Each client stores about 100 MB of data a year; files go to the client's R2 bucket.

| Cluster memory | Connections | Clients | Monthly price, with standby |
|---|---|---|---|
| 1 GiB | 22 | 7 | $30 |
| 2 GiB | 47 | 15 | $60 |
| 4 GiB | 97 | 32 | $120 |
| 8 GiB | 197 | 65 | $240 |
| 16 GiB | 397 | 132 | $480 |

App 5 shows the business's client count against its cluster's limit. The cluster is moved to the next size in DigitalOcean's control panel before the limit is reached.

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
7. **Staged rollout:** a high-risk release goes first to a chosen group of clients, then to the rest.
8. **Rollback:** App 5 points the containers back to the previous release image, with `auto-migrate` off and `ignore-invalid-schema` on. The previous release then runs on the newer schema, and the App Server never removes the newer tables and columns. The next release switches `auto-migrate` back on.

---

## 7. Provisioning

### Once per business

1. A DigitalOcean project for the business, in Mybizz's DigitalOcean account.
2. The Managed PostgreSQL cluster, in `LON1`.
3. The business's repository in the Container Registry.
4. The test client instance: a container and a database of its own, run as a client.
5. A DigitalOcean API token, scoped to the business's project, in App 5's Vault.

### Once per client

App 5's **New client** action, after registration and the client's Cloudflare set-up ([[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)):

1. Creates the client's database and database user in the cluster.
2. Creates the client's `encryption_key`, management Bearer token and two container keys.
3. Creates the client's App Platform app from the current release image, with every setting in section 3.
4. Adds the client's domain to the app; App 5 writes the domain's DNS record through the Cloudflare API.
5. Starts the container; the App Server builds the client's tables.

---

## 8. Client Exit

1. The client gives notice; the service runs to the end of the paid month.
2. App 5 exports all the client's data into the client's own R2 bucket ([[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md)).
3. App 5's **Remove** action deletes the client's App Platform app and the client's database and database user. DigitalOcean's charges for them stop at deletion.

---

## 9. Uptime and Resilience

| Service | DigitalOcean's monthly commitment |
|---|---|
| App Platform container | 99.95% |
| Managed PostgreSQL with a standby node | 99.95% |
| Container Registry | 99.95% |

99.95% allows about 22 minutes of downtime a month.

- One cluster in one region serves every client of a business. A DigitalOcean failure in `LON1`, or a suspension of Mybizz's DigitalOcean account, stops every client of the business.
- Every client's data is copied to the client's own R2 bucket every night, outside DigitalOcean.
- The rebuild procedure restores every client of a business in another DigitalOcean region from the release image and the R2 copies: a new cluster, a database per client loaded from its copy, and a container per client.

---

## 10. Conditions Before the First Paying Client

1. The full test suite passes on the release image.
2. The test client instance has run under realistic load, and its memory use and database connections are recorded against section 3 and section 4.
3. The rebuild procedure has restored the test client instance in another region.
4. The release path has run end to end: test client instance, staged rollout, rollback.

---

## 11. Monthly Cost

| Item | Monthly cost | Basis |
|---|---|---|
| Anvil Business account (Apps 1, 2, 3, 5 and the demo instances) | $99 | Per Mybizz account |
| Container Registry, Basic plan | $5 | Per Mybizz account |
| Test client instance container | $12 | Per business |
| Client container | $12 | Per client |
| Managed PostgreSQL cluster with standby | $30 to $480 | By client count (section 4) |

| Clients | Containers | Database | Fixed | Total | Revenue at $99 | Gross margin |
|---|---|---|---|---|---|---|
| 1 | $12 | $30 | $116 | $158 | $99 | −$59 |
| 2 | $24 | $30 | $116 | $170 | $198 | $28 |
| 10 | $120 | $60 | $116 | $296 | $990 | $694 |
| 25 | $300 | $120 | $116 | $536 | $2,475 | $1,939 |
| 50 | $600 | $240 | $116 | $956 | $4,950 | $3,994 |
| 100 | $1,200 | $480 | $116 | $1,796 | $9,900 | $8,104 |

Not in these figures: Amazon SES at $0.10 per 1,000 emails, Groq usage, payment processing fees, taxes, and bandwidth beyond each container's 150 GiB allowance at $0.02 per GiB.

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-five-app-architecture-model\|Five-App Architecture Model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md) | The five apps and their roles |
| [[[default:adr-global/adr-client-instance-architecture\|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) | The decision this specification carries out |
| [[[default:specifications-global/spec-deployment\|Deployment Specification]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) | Release, rollback, backup and failure procedures |
| [[[default:adr-global/adr-tiers-model\|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md) | Price and subscription terms |
