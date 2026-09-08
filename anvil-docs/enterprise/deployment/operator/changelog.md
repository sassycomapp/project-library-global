---
title: "Changelog"
url: "/docs/enterprise/deployment/operator/changelog"
---


# [Anvil Operator Changelog](#anvil-operator-changelog)

## [2026-07-17](#2026-07-17)

-   Add agent model provider configuration
-   Individual agents can now be disabled
-   Better support for no-downtime upgrades when platform server env vars are updated
-   Add LLM provider configuration

## [2026-07-06](#2026-07-06)

-   Add support for Anvil Agents

## [2026-06-11](#2026-06-11)

-   Remove NetworkPolicies when no longer required
-   Move downlinks.registryCerts to top level spec

## [2026-06-02](#2026-06-02)

-   Add support for additional downlink volumes
-   Speed up git server pod startup by setting `fsGroupChangePolicy: OnRootMismatch`

## [2026-05-06](#2026-05-06)

-   Add support for anvil_common_runtime_origin configuration
-   Improve Kopia error message when auth fails

## [2026-04-24](#2026-04-24)

-   Add version tag for default PDF Renderer image

## [2026-03-17](#2026-03-17)

-   Reduce memory usage for platform servers.

## [2026-03-03](#2026-03-03)

*Upgrade will cause Anvil to restart*

-   Perform rolling upgrades of downlink runners, to prevent downtime when upgrading.
-   Add accounting support, allowing developers to view per-app resource usage through the Anvil Editor

## [2026-02-19](#2026-02-19)

-   Fix misreported downlink resource usage metrics in Grafana dashboards

## [2026-02-11](#2026-02-11)

-   Add downlink reachability metrics
-   Upgrade query exporter to 4.0.1, to fix startup connection issues

## [2026-02-02](#2026-02-02)

-   Improve disk usage reporting in Grafana dashboards
-   Pin metrics service container image versions

## [2026-01-13](#2026-01-13)

-   Fix backups being retried too frequently after failure

## [2026-01-12](#2026-01-12)

-   Additional Grafana dashboards

## [2025-12-12](#2025-12-12)

-   Add migration support for OAuth Server and Git Sync improvements

## [2025-12-10](#2025-12-10)

-   Add support for git operations over HTTP

## [2025-11-24](#2025-11-24)

-   Support different Google credentials for Anvil Editor and Anvil app login (requires Anvil 2025-10-31 or later)
-   Add anvilMaxHttpBody platform server config option (requires Anvil 2025-11-24 or later)

## [2025-10-31-b](#2025-10-31-b)

-   Increase default Prometheus PVC size to 40Gi
-   Support reading the admin app password from a Kubernetes Secret

## [2025-10-17](#2025-10-17)

-   Support setting GitHub webhook secrets from k8s secrets

## [2025-10-15](#2025-10-15)

-   Add Postgres Query Exporter metrics dashboard
-   Automatically restart metrics services on config update
-   Add configuration of awsNlb loadBalancerClass

## [2025-10-01](#2025-10-01)

-   Logging of remote execution output no longer waits for the process to complete
-   Set default Grafana timezone to UTC

## [2025-09-11](#2025-09-11)

-   Add app logs retention policy configuration
-   Standardise retention configuration to use `d`, `h`, `m`, `s` units (configs may need to be manually updated)

## [2025-09-01](#2025-09-01)

-   Add sessionCompactionBatchSize Platform Server config option

## [2025-08-12](#2025-08-12)

*Upgrade will cause Anvil to restart*

-   Support custom /dev/shm size for deployment pool DBs
-   Trigger a rebuild of all downlink images after a restore

## [2025-08-05-b](#2025-08-05-b)

-   Support custom /dev/shm size for databases

## [2025-07-17](#2025-07-17)

-   Add Cluster Grafana dashboard and associated monitoring

## [2025-07-16](#2025-07-16)

-   Avoid the need for rinetd with dynamic downlinks
-   Upgrade databases automatically
-   Collect downlink container logs
-   Add backup retention setting

## [2025-06-30](#2025-06-30)

-   Prevent downtime during upgrades
-   Allow custom database config

## [2025-06-19](#2025-06-19)

-   Add support for custom Prometheus metrics retention time

## [2025-06-18](#2025-06-18)

-   Use the same version tag for the Downlink Registry as the Downlink Host

## [2025-06-17](#2025-06-17)

-   Add support for custom platform server image
-   Add support for custom node exporter image
-   Add support for custom Tempo trace retention time

## [2025-06-04](#2025-06-04)

-   Add legacy downlink environment variables from config
-   Add imagePullSecrets to Prometheus and node-exporter pods
-   Improvements to tracking of backups
-   Fix unreliable detection of DB migration completion
-   Fix incorrect replay of old events when a watch is restarted

## [2025-05-30](#2025-05-30)

-   Make Helm version value mandatory
-   Add more debug logging

## [2025-05-29](#2025-05-29)

-   Support privileged legacy downlinks

## [2025-05-23b](#2025-05-23b)

-   Allow platform server crash dumps to be captured to a PVC

## [2025-05-23](#2025-05-23)

-   Allow platform server JVM options to be configured
-   Allow Kubernetes secrets to be used with relevant platformServer.config fields
-   Tidy up configuration of legacy downlinks
-   Move `platformServerConfig` to `platformServers.config`

## [2025-05-08](#2025-05-08)

This release improves the documentation and validation of the Operator configuration. Several configuration settings have been reorganized and renamed to improve consistency and maintainability.

See [the Operator Cluster Configuration Documentation](https://anvil.works/docs/enterprise/deployment/operator/cluster) for a detailed description of the new configuration settings.

### Configuration Changes

#### Required Settings

-   `versionTag` is now required to explicitly specify the Anvil version running in the cluster.
-   `anvilOrigin` is now a required top-level setting (moved from `platformServerConfig`).

#### Top-level Settings

-   `platformServerVersionTagOverride` has been removed, use `versionTag` instead.
-   `platformServerConfig.anvilOrigin` → `anvilOrigin`.
-   `platformServerConfig.appOrigin` → `appOrigin`.
    -   This now defaults to `<anvilOrigin>/apps/{{id-or-alias}}`.
-   `licenceKeySecret` → `licenceKeySecretName`.
    -   The secret key is now always `"value"`.

#### Downlinks Configuration

All downlink-related settings have been consolidated under the `downlinks` section:

-   `enableDynamicDownlinks` → `downlinks.mode`.
    -   To disable downlinks, set `downlinks.mode="disabled"`.
-   `dynamicDownlinkMode` → `downlinks.mode`.
-   `includeDownlinkBaseImages` → `downlinks.includeBaseImages`.
-   `downlinkBaseImages` → `downlinks.baseImages`.
-   `downlinkRegistryCerts` → `downlinks.regisryCerts`.
-   `extraDynamicDownlinkVolumes` → `downlinks.extraVolumes`.

#### Backup Configuration

-   `backup.ssh.remoteDirectory` → `backup.ssh.directory`.
-   `backup.nfs.path` → `backup.nfs.export`.

#### Storage Configuration

All storage-related settings now use consistent PVC config naming:

-   `storage.*.persistentVolumeClaim` → `storage.*.pvc.existingClaimName`.
-   `storage.*.size` → `storage.*.pvc.size`.
-   `storage.*.storageClass` → `storage.*.pvc.storageClass`.

#### Other Renamed Settings

-   `enablePdfRenderer` → `pdfRenderer.enabled`.
-   `secrets.*` → `secretNames.*`.
-   `metrics.grafana.adminPasswordSecret` → `metrics.grafana.adminPasswordSecretName`.
    -   The secret key is now always `"value"`.
-   `tempo.image` and `tempo.version` → `tempo.image`.
    -   Now includes both the image and version tag.
-   `pods.nodeAffinity` → `pods.affinity.node`.
    -   Applies to all subfields of `pods` too.
-   `pods.podAffinity` → `pods.affinity.pod`.
    -   Applies to all subfields of `pods` too.

### Other Changes

#### Backup Path Changes

-   `backup.nfs.directory` and `backup.pvc.directory` no longer require the `"/anvil-backups"` prefix.
    -   This prefix is now automatically added to the SSH server configuration.
    -   If using custom NFS or PVC directories, remove this prefix from your settings.
-   The same applies to `restore.nfs.directory` and `restore.pvc.directory`.

#### S3 Backup Changes

-   S3 backups now strip all leading `/`’s from the prefix.
-   If no `pathPrefix` is set, backups will be stored in the root folder of the bucket.
-   **Note**: The new operator cannot restore backups made by old operators if `pathPrefix="/"`.

#### PVC Behavior Changes

-   All PVCs are now `Immutable`.
-   Once created, the operator will never attempt to update them.
-   This standardizes behavior across all PVC types.

#### Pod Environment Variables

-   Environment variables are now sorted alphabetically.
-   Changing the order of environment variables no longer triggers pod recreation. This prevents the need for downtime for future upgrades.
-   **Note**: Upgrading to this version will cause downtime as platform servers restart due to environment variable reordering.

### Configuration Validation

The operator now validates configurations before applying them. Invalid configurations will raise errors for unknown or missing fields.

Example of validation errors:

```yaml
# An invalid configuration:
spec:
  platformServerConfig:
    anvilOrigin: "https://anvil.example.com/"

# Will raise these errors:
# 1. versionTag field required
# 2. anvilOrigin field required
# 3. platformserverConfig.anvilOrigin is no longer supported,
#    use anvilOrigin outside platformServerConfig instead
```

## [2025-04-05](#2025-04-05)

-   Add Loki for log monitoring

## [2025-03-31](#2025-03-31)

-   Add Podman metrics to Prometheus
-   Perform a no-downtime rolling upgrade if the licence key is updated
-   Fix issue that prevented platform servers from draining during an upgrade
-   Logging improvements
-   Restore PVCs to the same size as they were when backed up
-   Fix issues with pod affinity
