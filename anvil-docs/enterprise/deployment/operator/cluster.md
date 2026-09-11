---
document: "Cluster Configuration"
title: "Cluster Configuration"
url: "/docs/enterprise/deployment/operator/cluster"
doc-id: cluster
state: Live
date-created: 2026-09-08
---

# [Cluster Configuration](#cluster-configuration)

Your Anvil cluster can be configured by specifying appropriate options in the Cluster Custom Resource spec. Here is a sample Cluster resource:

```yaml
apiVersion: anvil.works/v1
kind: Cluster
metadata:
  namespace: anvil
  name: maple
spec:
  versionTag: 2025.01.01
  anvilOrigin: https://anvil.mycorp.com
  appOrigin: https://{{id-or-alias}}.apps.anvil.mycorp.com
  platformServerCount: 3
  loadBalancer:
    internalTls:
      certificateSecretName: anvil-certs
```

### Upgrading Anvil

Update your Anvil cluster by replacing the `spec.versionTag` property in your `Cluster` Resource.

### Rolling Updates

If a field marked with No Downtime is updated, the Anvil Operator will take care of bringing up servers with the new configuration and draining the old ones, avoiding downtime where possible.

This feature is enabled with the `updatePolicy="rolling"` setting, and requires a multi-node cluster licence.

## [Configuration Reference](#configuration-reference)

#### versionTag

No Downtime Required

The Anvil Enterprise version to install into the cluster.

#### anvilOrigin

Required

The base URL used by the Anvil platform server.

#### appOrigin

Default: `"<anvilOrigin>/apps/{{id-or-alias}}"`

The base URL used for individual apps. `{{id-or-alias}}` will be replaced automatically for each app.

If not provided, apps will be served from `<anvilOrigin>/apps/{{id-or-alias}}`. This is not recommended for production clusters, as it [is more secure](https://en.wikipedia.org/wiki/Same-origin_policy) to serve unrelated apps from a different origin.

Instead, set `appOrigin` to ensure each app has a different origin. For example:

```yaml
anvilOrigin: "https://anvil.example.com"
appOrigin: "https://{{id-or-alias}}.apps.anvil.example.com"
```

#### licenceKeySecretName

No Downtime Default: `null`

The name of an Opaque Secret containing the Anvil licence key.

For example, create the following Secret and use it with `licenceKeySecretName: anvil-licence-key`:

```bash
kubectl create -n anvil secret generic anvil-licence-key --from-literal="value=<LICENCE_KEY>"
```

#### imagePullSecretName

Default: `"anvil-registry-creds"`

The name of a [`kubernetes.io/dockerconfigjson` Secret](https://kubernetes.io/docs/concepts/configuration/secret/#docker-config-secrets) to be used when pulling images from the Anvil container registry.

If not set, the default name can be overridden by the `ANVIL_IMAGE_PULL_SECRET` environment variable or the `imagePullSecret` Helm chart value.

#### imagePrefix

Default: `null`

If set, this overrides the default container image prefix for `imagePrefixPublic` and `imagePrefixPrivate`.

#### imagePrefixPublic

Default: `"anvil.works/public/"`

The prefix to use for public Anvil container images. If not set, `imagePrefix` is used. If that isn’t set either, `"anvil.works/public/"` is used.

#### imagePrefixPrivate

Default: `"anvil.works/on-site/"`

The prefix to use for private Anvil container images. If not set, `imagePrefix` is used. If that isn’t set either, `"anvil.works/on-site/"` is used.

#### busyboxImage

Default: `"busybox"`

The Busybox image to use for init containers.

#### haproxyImage

Default: `"haproxy:2.9"`

The HAProxy image to use for load balancers.

#### sshServerImage

Default: `"linuxserver/openssh-server"`

The OpenSSH server image to use for SSH servers.

#### timescaleDbVersion

Default: `"14"`

The PostgreSQL version to use for the timescale databases.

#### postgresDbVersion

Default: `"10"`

The PostgreSQL version to use for the standard databases.

#### allowDbUpgrade

Default: `true`

When `true`, databases will be automatically upgraded to the version specified in `postgresDbVersion`.

If set to `false`, databases will fail to start if you attempt to run an incompatible database version.

#### platformDbImageOverride

Default: `null`

If set, this overrides the platform database container image.

#### splitDb

Default: `false`

If set, the app data tables are stored in a separate database (`data-tables-db`) instead of the main platform database (`platform-db`).

#### platformServerCount

No Downtime Default: `1`

The number of platform servers in the cluster’s main pool.

#### updatePolicy

Default: `"rolling"`

The policy to use for updating the Anvil platform servers:

-   `"rolling"`: When the configuration changes, create new platform servers with the updated configuration, wait for them to become ready, then drain and delete the old ones.
-   `"immediate"`: When the configuration changes, immediately shut down the existing platform servers, and create new ones with the updated configuration.

#### updateApproval

Default: `null`

If set, only platform servers with the specified version tag will be created. This can either be a single version tag, or a dictionary of Deployment Pool IDs to version tags. Any platform servers that already exist are not affected.

Platform servers in the main pool are unaffected by this setting.

#### extraCertsSecret

Default: `null`

The name of an Opaque Secret containing additional certificate files to add to the platform server’s keystore.

For example, you could create the following Secret and use it with `extraCertsSecret: my-extra-certs`:

```bash
kubectl create -n anvil secret generic my-extra-certs --from-file="<PATH_TO_CERTIFICATE_FILE>"
```

## [registryCerts\[\]](#registrycerts)

Custom CA (or even client) certificates for connecting to registries from the downlink and agent runners. This is useful when pulling custom base images from private registries in podman mode.

See the [containers-certs.d documentation](https://github.com/containers/image/blob/main/docs/containers-certs.d.5.md#directory-structure) for more details.

#### registryCerts\[\].registry

Required

The `"server:port"` of the registry.

#### registryCerts\[\].secret

Required

The name of an Opaque Secret containing one or more `.crt`, `.cert` or `.key` files.

## [Platform Servers](#platform-servers)

#### platformServers.image

Default: `"<imagePrefixPrivate>anvil-platform-server"`

The container image to use for the platform servers, excluding the version tag.

#### platformServers.jvmOptions\[\]

No Downtime Default: `["-Xmx4g"]`

A list of JVM options to use for the platform servers.

### platformServers.config

No Downtime

Override the default configuration of the Anvil platform servers by setting the fields below inside a `platformServers.config` block. For example, to disable email verification:

```yaml
platformServers:
  config:
    noVerifyEmail: true
```

Some fields below have comments indicating that they can be provided by a Kubernetes Secret. These can be configured as follows:

```yaml
platformServers:
  config:
    anvilGoogleClientSecret:
      valueFrom:
        secretKeyRef:
          name: <secret-name>
          key: value
```

Field

Description

`noVerifyEmail`

If set, the server will not send verification emails when accepting signups.  
**Default: `false`**

`anvilRequireUserEmailSuffix`

If set, all signups must use an email address with this suffix.  
**Default: `null`**

`anvilEnableEmailLogin`

By default, email login to the Anvil Editor is disabled unless there are no other login methods enabled. Set this field to `True` to override this and enable email login unconditionally.  
**Default: `null`**

`anvilEnableGoogleLogin`

Allow users to sign in to the Anvil Editor with Google.  
**Default: `null`**

`anvilEnableMicrosoftLogin`

Allow users to sign in to the Anvil Editor with Microsoft.  
**Default: `null`**

`anvilEnableGithubLogin`

Allow users to sign in to the Anvil Editor with GitHub.  
**Default: `null`**

`anvilGoogleIdeClientId`

Google credentials for Anvil Editor login. Defaults to `anvilGoogleClientId` if not set. Generate from the [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager).  
**Default: `null`**

`anvilGoogleIdeClientSecret`

Google credentials for Anvil Editor login. Defaults to `anvilGoogleClientSecret` if not set. Generate from the [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager). Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilGoogleClientId`

Google credentials for use in Anvil apps. Generate from the [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager).  
**Default: `null`**

`anvilGoogleClientSecret`

Google credentials for use in Anvil apps. Generate from the [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager). Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilGoogleMapsApiKey`

Generate from the [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager). Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilGooglePickerApiKey`

Generate from the [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager). Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilFacebookAppId`

**Default: `null`**

`anvilFacebookAppSecret`

Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilMicrosoftIdeAppId`

Microsoft credentials for Anvil Editor login. Generate from the Azure console ([see our guide](https://anvil.works/docs/integrations/microsoft/linking-azure-and-anvil))  
**Default: `null`**

`anvilMicrosoftIdeAppSecret`

Microsoft credentials for Anvil Editor login. Generate from the Azure console ([see our guide](https://anvil.works/docs/integrations/microsoft/linking-azure-and-anvil)) Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilMicrosoftIdeTenantId`

Microsoft credentials for Anvil Editor login. Generate from the Azure console ([see our guide](https://anvil.works/docs/integrations/microsoft/linking-azure-and-anvil)), if a tenant ID is required.  
**Default: `null`**

`anvilMicrosoftAppId`

Microsoft credentials for use in Anvil apps. Generate from the Azure console ([see our guide](https://anvil.works/docs/integrations/microsoft/linking-azure-and-anvil))  
**Default: `null`**

`anvilMicrosoftAppSecret`

Microsoft credentials for use in Anvil apps. Generate from the Azure console ([see our guide](https://anvil.works/docs/integrations/microsoft/linking-azure-and-anvil)) Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilMicrosoftTenantId`

Microsoft credentials for use in Anvil apps. Generate from the Azure console ([see our guide](https://anvil.works/docs/integrations/microsoft/linking-azure-and-anvil)), if a tenant ID is required.  
**Default: `null`**

`anvilGithubAppUrl`

**Default: `null`**

`anvilGithubClientId`

**Default: `null`**

`anvilGithubClientSecret`

Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilGithubWebhookSecret`

Can be provided by a Kubernetes Secret.  
**Default: `null`**

`anvilGithubEnterpriseHostname`

**Default: `null`**

`anvilGithubVerifyTls`

**Default: `true`**

`anvilIdeApiToken`

The bearer token to use for the Anvil IDE API authentication. If not set, the IDE API will be disabled. Can be provided by a Kubernetes Secret.  
**Default: `null`**

`sessionCompactionBatchSize`

The number of log lines to compact in each batch during session compaction.  
**Default: `10000`**

`smtpHost`

External SMTP server to use for sending email: Hostname  
**Default: `null`**

`smtpPort`

External SMTP server to use for sending email: Port  
**Default: `25`**

`smtpUser`

External SMTP server to use for sending email: Username  
**Default: `null`**

`smtpPass`

External SMTP server to use for sending email: Password Can be provided by a Kubernetes Secret.  
**Default: `null`**

`smtpSsl`

**Default: `false`**

`smtpTls`

**Default: `false`**

`emailFrom`

“From” email address to use for outgoing emails.  
**Default: `null`**

`emailTo`

Address for email notifications and support requests.  
**Default: `null`**

`adminAppPassword`

The password for the admin app. Can be provided by a Kubernetes Secret. If the Secret does not already exist, it will be created automatically with a random password. If not set, a Secret named `anvil-<cluster-name>-admin-app-password` will be used.  
**Default: `{"valueFrom": {"secretKeyRef": {"name": "anvil-<cluster-name>-admin-app-password", "key": "value"}}}`**

`adminAppPasswordHash`

Deprecated, use `adminAppPassword` instead. If set, `adminAppPassword` will be ignored.  
**Default: `null`**

`adminAppEnableGoogleLogin`

Allow users to sign in to the admin app with Google.  
**Default: `false`**

`adminAppGoogleLoginAllowedEmails`

Comma-separated list of email addresses that can be used to sign in to the admin app with Google.  
**Default: `null`**

`adminAppEnableMicrosoftLogin`

Allow users to sign in to the admin app with Microsoft Account.  
**Default: `false`**

`adminAppMicrosoftLoginAllowedEmails`

Comma-separated list of email addresses that can be used to sign in to the admin app with Microsoft Account.  
**Default: `null`**

`adminAppIpWhitelist`

Comma-separated list of IP addresses and CIDR blocks that are allowed to access the admin app (Example: 172.16.0.10,127.0.0.0/12). If null there are no restrictions.  
**Default: `null`**

`anvilDbPoolSize`

The maximum number of concurrent database connections.  
**Default: `90`**

`anvilDbTxnPoolSize`

The maximum number of concurrent database transactions to use for app transactions.  
**Default: `75`**

`anvilMaxHttpBody`

Maximum number of bytes to accept in an HTTP request body.  
**Default: `268435456`**

`anvilDisableUrlSessionTokensOutsideIde`

**Default: `null`**

`anvilInsecureCookies`

Set to `True` to allow cookies to be sent over HTTP, and to disable same-site cookie enforcement.  
**Default: `null`**

`noConfirmValidEmailAddressDuringAuth`

**Default: `null`**

`twilioVerifyServiceId`

**Default: `null`**

`twilioVerifyAccountSid`

**Default: `null`**

`twilioVerifyAuthToken`

Can be provided by a Kubernetes Secret.  
**Default: `null`**

`defaultSessionExpiryTimeoutMins`

**Default: `30`**

`anvilStripeConfig`

JSON configuration blob for Anvil’s Stripe integration Can be provided by a Kubernetes Secret.  
**Default: `null`**

`dynamicDownlinkMemory`

The maximum memory to allow each downlink process.  
**Default: `"1g"`**

`dynamicDownlinkCpus`

The maximum number of CPUs to allow each downlink process.  
**Default: `"1"`**

`dynamicDownlinkWorkerTimeout`

The maximum time in seconds to allow each downlink call to run.  
**Default: `30`**

`anvilCommonRuntimeOrigin`

The origin on which to serve common app routes, such as OAuth redirect endpoints.  
**Default: `"<anvilOrigin>"`**

`anvilLlmProvider`

LLM provider to use for miscellaneous tasks in the editor (excluding the AI Agents feature). Select from “openai-chat”, “openai-responses” or “anthropic”. If you don’t configure the corresponding API key, LLM-based functionality will not be available.  
**Default: `"openai-chat"`**

`anvilOpenaiApiKey`

OpenAI API key to use for the LLM provider.  
**Default: `null`**

`anvilOpenaiBaseUrl`

OpenAI API base URL to use for the LLM provider.  
**Default: `"https://api.openai.com/v1"`**

`anvilAnthropicApiKey`

Anthropic API key to use for the LLM provider.  
**Default: `null`**

`anvilAnthropicBaseUrl`

Anthropic API base URL to use for the LLM provider.  
**Default: `"https://api.anthropic.com/v1"`**

### platformServers.crashDumps

#### platformServers.crashDumps.enabled

Default: `false`

If set to `true`, crash dumps from each of the platform servers will be collected in an EmptyDir volume. This persists across restarts of the platform server, but is deleted when the platform server is removed or upgraded.

## [Databases](#databases)

Configure the databases for the cluster.

#### databases.config\[\]

Default: `[]`

Additional lines of configuration, appended to the database’s config file. Databases must be manually restarted for the new config to take effect.

### databases.platformDb

#### databases.platformDb.config\[\]

Default: `"<databases.config>"`

Additional lines of configuration, appended to the database’s config file. Databases must be manually restarted for the new config to take effect.

If not set, the parent `databases.config` setting will be used.

#### databases.platformDb.shmSize

Default: `"64Mi"`

The amount of shared memory that should be made available to PostgreSQL.

### databases.dataTablesDb

#### databases.dataTablesDb.config\[\]

Default: `"<databases.config>"`

Additional lines of configuration, appended to the database’s config file. Databases must be manually restarted for the new config to take effect.

If not set, the parent `databases.config` setting will be used.

#### databases.dataTablesDb.shmSize

Default: `"64Mi"`

The amount of shared memory that should be made available to PostgreSQL.

#### databases.dataTablesDb.ginCleanInterval

Default: `null`

The number of seconds between GIN index pending list cleanup operations. If not set, GIN index cleanup is disabled.

#### databases.dataTablesDb.vacuumInterval

Default: `null`

The number of seconds between vacuum operations. If not set, vacuum is disabled.

### databases.appLogsDb

#### databases.appLogsDb.config\[\]

Default: `"<databases.config>"`

Additional lines of configuration, appended to the database’s config file. Databases must be manually restarted for the new config to take effect.

If not set, the parent `databases.config` setting will be used.

#### databases.appLogsDb.shmSize

Default: `"64Mi"`

The amount of shared memory that should be made available to PostgreSQL.

#### databases.appLogsDb.retention

Default: `"forever"`

The retention period for session logs. If set to `"forever"`, session logs will be retained indefinitely. Supported units: `d`, `h`, `m`, `s`.

#### databases.appLogsDb.looseEventRetention

Default: `"47h"`

The retention period for loose events that have not yet been compacted to a session. If set to `"forever"`, loose events will be retained indefinitely. Supported units: `d`, `h`, `m`, `s`.

### databases.accountingDb

#### databases.accountingDb.config\[\]

Default: `"<databases.config>"`

Additional lines of configuration, appended to the database’s config file. Databases must be manually restarted for the new config to take effect.

If not set, the parent `databases.config` setting will be used.

#### databases.accountingDb.shmSize

Default: `"64Mi"`

The amount of shared memory that should be made available to PostgreSQL.

## [Downlinks](#downlinks)

#### downlinks.mode

Default: `"podman"`

Either `"podman"` to provide container-based Python server environments, or `"disabled"` to disable this functionality.

#### downlinks.includeBaseImages

Default: `false`

Include all base images in the downlink registry. If not set, base images will be downloaded when the cluster boots.

### downlinks.baseImages\[\]

A list of Python base images to make available for use. If not set, the default list of base images will be used.

For example, to include only the `Minimal 3.10` base image:

```yaml
downlinks:
  baseImages:
    - name: python310-minimal
      title: "Minimal 3.10"
      repo: anvil.works/public/anvil-downlink-base-python310-minimal
```

#### downlinks.baseImages\[\].name

Required

A unique identifier for the base image.

#### downlinks.baseImages\[\].repo

Required

The repository URL for the base image container.

#### downlinks.baseImages\[\].title

Human-readable title of the base image, shown in the UI. If not set, the `name` field will be used.

### downlinks.extraVolumes\[\]

No Downtime

Provide additional volumes to mount in the downlink server container.

#### downlinks.extraVolumes\[\].volume

No Downtime Required

The [Kubernetes Volume definition](https://kubernetes.io/docs/concepts/storage/volumes/) to be added to the downlink server. It must not include the `name` field, as this will be set automatically.

For example:

```yaml
downlinks:
  extraVolumes:
    - volume:
        persistentVolumeClaim:
          claimName: my-pvc
      mountPath: /my-data
```

#### downlinks.extraVolumes\[\].mountPath

No Downtime Required

The path within the downlink server container to mount the volume at.

#### downlinks.extraVolumes\[\].mode

No Downtime Default: `"rw"`

The mount access mode for the volume: `ro` for read-only, or `rw` for read-write.

## [Legacy Downlinks](#legacy-downlinks)

Provide the legacy ‘Full Python 3\` server environment.

#### legacyDownlinks.count

Default: `1`

Enable the legacy (“Full Python 3”) server environments by setting this to greater than zero

#### legacyDownlinks.image

Default: `"<imagePrefixPublic>anvil-downlink-python3-minimal"`

The container image to use for the `Full Python 3` downlink server. The default is the ‘-minimal’ image; for the full (multi-gigabyte) set of packages use the ‘-full’ image.

#### legacyDownlinks.timeout

Default: `30`

The timeout in seconds for the `Full Python 3` downlink server. Any server calls that take longer than this will be stopped.

#### legacyDownlinks.privileged

Default: `false`

Whether to run the legacy downlink images in privileged mode.

#### legacyDownlinks.config

Default: `{}`

Additional environment variables for the downlink server.

## [Load Balancer](#load-balancer)

Configuration for the load balancer used as an entry point to the cluster.

By default, the load balancer is enabled and configured as `internalTls`. You can override this with one of the following options:

-   `disabled`: Disable the load balancer
-   `internalTls`: Use internal TLS termination (default)
-   `externalTls`: Use external TLS termination
-   `awsNlb`: Use an AWS network load balancer
-   `insecure`: No TLS

#### loadBalancer.disabled

Default: `false`

Disable the load balancer.

#### loadBalancer.externalDns

Default: `null`

Set the domain name for the load balancer service using the [`external-dns.alpha.kubernetes.io/hostname`](https://kubernetes-sigs.github.io/external-dns/latest/docs/annotations/annotations/#external-dnsalphakubernetesiohostname) annotation.

#### loadBalancer.image

Default: `null`

The container image to use for the load balancer. If not set, the cluster’s `haproxyImage` setting is used.

#### loadBalancer.ip

Default: `null`

The static IP address for the load balancer using the `loadBalancerIP` service field.

This field is deprecated (see the [note in the Kubernetes LoadBalancer docs](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)). Use a provider-specific annotation instead.

#### loadBalancer.smtpPort

Default: `25`

The external port to use for incoming SMTP traffic.

#### loadBalancer.sshPort

Default: `22`

The external port to use for incoming SSH traffic.

### loadBalancer.internalTls

Configure the load balancer to use internal TLS termination. This is the default mode of operation.

#### loadBalancer.internalTls.loadBalancerClass

Default: `null`

The value for the `loadBalancerClass` service field.

#### loadBalancer.internalTls.annotations

Default: `{}`

Additional annotations for the load balancer service.

#### loadBalancer.internalTls.certificateSecretName

Default: `null`

The name of a [`kubernetes.io/tls` Secret](https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets) containing a TLS certificate and key for the cluster load balancer.

A `<cert>.crt` and `<cert>.key` must be provided for each certificate. Multiple certificates can be specified by providing additional `<cert2>.crt` and `<cert2>.key` files in the Secret.

If not set, a self-signed certificate will be generated.

#### loadBalancer.internalTls.httpPort

Default: `80`

The external port to use for HTTP traffic.

#### loadBalancer.internalTls.httpsPort

Default: `443`

The external port to use for HTTPS traffic.

### loadBalancer.externalTls

Configure the load balancer to use external TLS termination.

#### loadBalancer.externalTls.loadBalancerClass

Default: `null`

The value for the `loadBalancerClass` service field.

#### loadBalancer.externalTls.annotations

Default: `{}`

Additional annotations for the load balancer service.

#### loadBalancer.externalTls.httpPort

Default: `80`

The external port to use for HTTP traffic.

#### loadBalancer.externalTls.trustedHttpPort

Default: `8000`

The external port to use for trusted HTTP traffic.

### loadBalancer.awsNlb

Use an AWS network load balancer. TLS can be terminated either:

-   In the AWS NLB by setting `certificateArn`.
-   In the cluster load balancer by setting `certificateSecretName`.
-   In the cluster load balancer with a self-signed certificate by not setting either certificate field.

#### loadBalancer.awsNlb.loadBalancerClass

Default: `"service.k8s.aws/nlb"`

The value for the `loadBalancerClass` service field.

Use the default `service.k8s.aws/nlb` when using the default AWS Load Balancer Controller configuration. Set to `eks.amazonaws.com/nlb` when using the AWS Load Balancer Controller provided by EKS in Auto-Mode.

#### loadBalancer.awsNlb.annotations

Default: `{}`

Additional annotations for the load balancer service.

#### loadBalancer.awsNlb.certificateArn

Default: `null`

The ARN of one or more certificates in AWS to use for TLS. If set, this creates a [`service.beta.kubernetes.io/aws-load-balancer-ssl-cert`](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/service/annotations/#tls) annotation, and the AWS NLB will terminate TLS.

Multiple certificates can be provided as a comma-separated list of ARNs.

#### loadBalancer.awsNlb.certificateSecretName

Default: `null`

The name of a [`kubernetes.io/tls` Secret](https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets) containing a TLS certificate and key for the cluster load balancer.

If neither this nor `certificateArn` are specified, a self-signed TLS certificate will be generated.

#### loadBalancer.awsNlb.httpPort

Default: `80`

The external port to use for HTTP traffic.

#### loadBalancer.awsNlb.httpsPort

Default: `443`

The external port to use for HTTPS traffic.

### loadBalancer.insecure

Configure the load balancer for http only (no TLS).

#### loadBalancer.insecure.loadBalancerClass

Default: `null`

The value for the `loadBalancerClass` service field.

#### loadBalancer.insecure.annotations

Default: `{}`

Additional annotations for the load balancer service.

#### loadBalancer.insecure.httpPort

Default: `80`

The external port to use for HTTP traffic.

## [Deployment Pools](#deployment-pools)

#### deploymentPools.<id>.title

No Downtime Default: `null`

Human-readable name for the pool.

#### deploymentPools.<id>.platformServerCount

No Downtime Default: `1`

The number of platform servers in the pool.

#### deploymentPools.<id>.downlinkRunnerCount

Default: `1`

The number of downlink runners in the pool.

### deploymentPools.<id>.platformServers

#### deploymentPools.<id>.platformServers.jvmOptions\[\]

No Downtime Default: `null`

A list of JVM options for the platform servers in the pool. If not set, the options from the [`platformServers`](#platform-servers)`.jvmOptions` field will be used.

### deploymentPools.<id>.pods

Configure the Kubernetes pods used in the pool.

Each pod definition has a `resources` and `affinity` field. If neither of these are specified for a pod, the `deploymentPools.<id>.pods.resources` and `deploymentPools.<id>.pods.affinity` will be used.

For example, the following specifies a 2GiB memory request for the containers in the `downlinkRunner` pod, but uses a 1GiB request for the containers in all other pods in the pool:

```yaml
deploymentPools:
  my-pool:
    pods:
      resources:
        requests:
          memory: 1Gi
      downlinkRunner:
        resources:
          requests:
            memory: 2Gi
```

### deploymentPools.<id>.pods.platformServers

No Downtime

Pod configuration (`resources` and `affinity`) for the platform servers in the pool.

### deploymentPools.<id>.pods.databases

### deploymentPools.<id>.pods.databases.dataTables

Pod configuration (`resources` and `affinity`) for the data tables database in the pool. If not set, the parent `deploymentPools.<id>.pods.databases` configuration will be used.

### deploymentPools.<id>.pods.downlinkRunner

Pod configuration (`resources` and `affinity`) for the downlink runners in the pool.

### deploymentPools.<id>.defaultDownlinkLimits

#### deploymentPools.<id>.defaultDownlinkLimits.memory

No Downtime Default: `"1Gi"`

Limit the memory available to the downlink containers. Units must be Ki, Mi, or Gi.

#### deploymentPools.<id>.defaultDownlinkLimits.cpus

No Downtime Default: `1`

Limit the number of CPUs available to the downlink containers.

#### deploymentPools.<id>.defaultDownlinkLimits.workerTimeout

No Downtime Default: `30`

The maximum time in seconds between requests before a worker is retired.

### deploymentPools.<id>.loadBalancer

By default, deployment pools use the same load balancer as the main pool. You can enable a separate load balancer for each pool by configuring this field.

See the top-level [`loadBalancer`](#load-balancer) field for details of the options available.

### deploymentPools.<id>.storage

### deploymentPools.<id>.storage.dataTablesDb

Storage configuration for the deployment pool’s data tables database.

#### deploymentPools.<id>.storage.dataTablesDb.dataPath

Default: `"/data"`

The path inside the PVC to use for storage.

### deploymentPools.<id>.storage.dataTablesDb.pvc

#### deploymentPools.<id>.storage.dataTablesDb.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### deploymentPools.<id>.storage.dataTablesDb.pvc.size

Default: `"4Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### deploymentPools.<id>.storage.dataTablesDb.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### deploymentPools.<id>.storage.downlinkContainerData

Storage configuration for the deployment pool’s downlink runners.

### deploymentPools.<id>.storage.downlinkContainerData.pvc

#### deploymentPools.<id>.storage.downlinkContainerData.pvc.size

Default: `"40Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### deploymentPools.<id>.storage.downlinkContainerData.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

## [Backup](#backup)

If backups are enabled, the operator will periodically back up all database and source code to the configured backup target.

By default, backups are enabled and will be written to a PVC in the cluster.

#### backup.disabled

Default: `false`

Disable all backup functionality.

#### backup.encryptionKeySecretName

Default: `"anvil-<cluster-name>-backup-encryption-key"`

The name of an Opaque Secret containing an encryption key for the backups. If the Secret does not already exist, it will be created automatically with a random key.

#### backup.maxDelta

Default: `30`

The number of delta backups to perform in between full backups. This is the [`WALG_DELTA_MAX_STEPS` setting for WAL-G](https://wal-g.readthedocs.io/PostgreSQL/).

#### backup.frequency

Default: `"24h"`

How often to backup the databases and source code. The database WAL is continuously archived between backups using [PostgreSQL Continuous Archiving](https://www.postgresql.org/docs/10/continuous-archiving.html). Supported units: `d`, `h`, `m`, `s`.

#### backup.retention

Default: `"365d"`

How long to retain backups. If set to `"forever"`, backups will be retained indefinitely. Supported units: `d`, `h`, `m`, `s`.

### backup.target

Configure where the backups will be written. This is one of:

-   `s3`: Write to an S3 bucket. Currently this is only possible when running in an AWS EKS cluster.
-   `ssh`: Write to a remote server via SSH.
-   `nfs`: Write to an NFS volume in the cluster.
-   `pvc`: Write to a PVC in the cluster (default).

### backup.target.s3

#### backup.target.s3.bucketName

Required

The name of the S3 bucket to write backups to.

#### backup.target.s3.pathPrefix

Default: `"/"`

The directory in the S3 bucket used to store the backup files.

### backup.target.ssh

#### backup.target.ssh.hostname

Required

The hostname of the SSH server to write backups to.

#### backup.target.ssh.port

Default: `22`

The port of the SSH server.

#### backup.target.ssh.directory

Required

The directory on the remote server used to store the backup files.

#### backup.target.ssh.username

Default: `"anvil-backup"`

The username to use for the SSH connection.

#### backup.target.ssh.authSecretName

Required

The name of a [kubernetes.io/ssh-auth Secret](https://kubernetes.io/docs/concepts/configuration/secret/#ssh-authentication-secrets) containing an SSH private key to use for the backup.

#### backup.target.ssh.knownHostsSecretName

Required

The name of an Opaque Secret containing a known hosts file entry for the SSH server.

For example, you could create the following Secret and use it with `knownHostsSecretName: my-known-hosts`:

```bash
kubectl create -n anvil secret generic my-known-hosts --from-file="known_hosts"
```

### backup.target.nfs

#### backup.target.nfs.server

Required

The hostname of the NFS server.

#### backup.target.nfs.export

Required

The exported directory on the NFS server.

#### backup.target.nfs.directory

Default: `"/"`

The subdirectory inside the NFS export used to store the backup files.

### backup.target.pvc

#### backup.target.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### backup.target.pvc.size

Default: `"12Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### backup.target.pvc.storageClass

Default: `null`

The storage class to use if creating a new PVC. If not set, the cluster’s `storage.defaultRetainedStorageClass` will be used.

This field is ignored if the PVC already exists.

#### backup.target.pvc.directory

Default: `"/"`

The directory in the PVC used to store the backup files.

## [Database Restore Points](#database-restore-points)

#### dbRestorePoints.enabled

Default: `false`

Enable the ability to perform point-in-time restores of the app databases.

## [PDF Renderer](#pdf-renderer)

The PDF renderer service converts HTML to PDF documents. This is required for the `anvil.pdf.render_form()` server function.

#### pdfRenderer.enabled

Default: `true`

Enable the PDF renderer.

#### pdfRenderer.image

Default: `"<imagePrefixPublic>anvil-pdf-renderer:<versionTag>"`

The container image to use for the PDF renderer.

#### pdfRenderer.disableDevShm

Default: `false`

Disable the use of /dev/shm for the PDF renderer. This reduces memory usage at the expense of performance.

#### pdfRenderer.certificateSecretName

Default: `null`

The name of an Opaque Secret containing a TLS certificate to add to the PDF Renderer’s certificate store. This can be used to render PDFs from a server that uses a self-signed certificate.

For example, you could create the following Secret and use it with `certificateSecretName: my-certificate`:

```bash
kubectl create -n anvil secret generic my-certificate --from-file="tls.crt"
```

#### pdfRenderer.disableCertificateCheck

Default: `false`

Disable the certificate check for the PDF renderer.

## [Agents](#agents)

#### agents.enabled

Default: `false`

Allow the use of AI Agents in the Anvil Editor.

#### agents.agentHostImage

Default: `"<imagePrefixPublic>anvil-agent-host"`

The container image to use for the agent host.

#### agents.agentHostImageTag

Default: `"<versionTag>"`

The tag to use for the agent host image. By default this follows the cluster’s `versionTag`.

### agents.codex

#### agents.codex.enabled

No Downtime Default: `true`

Set to `False` to disable the Codex agent.

### agents.codex.authOverride

If set, override the Codex agent authentication with one of the following preset configurations.

#### agents.codex.authOverride.apiKey

No Downtime Default: `null`

Configure the `CODEX_API_KEY` for the default OpenAI-provided models:

```yaml
agents:
  codex:
    authOverride:
      apiKey:
        valueFrom:
          secretKeyRef:
            name: openai-api-key
            key: value
```

The API key is stored in a Kubernetes secret:

```bash
kubectl create -n anvil secret generic openai-api-key --from-literal="value=<YOUR_API_KEY>"
```

### agents.codex.authOverride.openaiModelProvider

Configure your own OpenAI-compatible model provider:

```yaml
agents:
  codex:
    authOverride:
      openaiModelProvider:
        baseUrl: https://my-model-provider.services.ai.azure.com/openai/v1
        apiKey:
          valueFrom:
            secretKeyRef:
              name: model-provider-api-key
              key: value
```

The API key is stored in a Kubernetes secret:

```bash
kubectl create -n anvil secret generic model-provider-api-key --from-literal="value=<YOUR_API_KEY>"
```

#### agents.codex.authOverride.openaiModelProvider.baseUrl

No Downtime Required

#### agents.codex.authOverride.openaiModelProvider.apiKey

No Downtime Required

#### agents.codex.authOverride.openaiModelProvider.modelAllowlist\[\]

No Downtime Default: `null`

Restrict the models available through the model provider. If the agent offers a model that is not in this list, it will not be shown to the user.

If not set, all models are allowed.

#### agents.codex.authOverride.openaiModelProvider.defaultModel

No Downtime Default: `null`

The model to use by default.

### agents.claude

#### agents.claude.enabled

No Downtime Default: `true`

Set to `False` to disable the Claude agent.

## [Accounting](#accounting)

Configure resource usage accounting.

#### accounting.enabled

Default: `false`

Allow developers to view per-app resource usage through the Anvil Editor.

## [Metrics](#metrics)

Configure metrics collection and monitoring services.

#### metrics.enabled

Default: `false`

Enable metrics services.

#### metrics.domainName

Default: `null`

The domain name for the metrics services. If set, the metrics services will be exposed externally on this domain name.

### metrics.grafana

#### metrics.grafana.image

Default: `"grafana/grafana:12.3.1"`

The container image to use for the Grafana service.

#### metrics.grafana.adminPasswordSecretName

Default: `"anvil-<cluster-name>-grafana-admin-password"`

The name of an Opaque Secret containing the Grafana admin password. If the secret does not already exist, it will be created automatically with a random password.

For example, you could create the following Secret and use it with `adminPasswordSecretName: my-grafana-admin-password`:

```bash
kubectl create -n anvil secret generic my-grafana-admin-password --from-literal="value=<ADMIN_PASSWORD>"
```

#### metrics.grafana.config

Default: `{}`

Additional environment variables for the Grafana service.

### metrics.grafana.pvc

#### metrics.grafana.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### metrics.grafana.pvc.size

Default: `"1Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### metrics.grafana.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### metrics.prometheus

#### metrics.prometheus.image

Default: `"prom/prometheus:v3.9.1"`

The container image to use for the Prometheus service.

#### metrics.prometheus.retention

Default: `"90d"`

How long to retain metrics in Prometheus. If set to `"forever"`, metrics will be retained indefinitely. Supported units: `d`, `h`, `m`, `s`.

### metrics.prometheus.pvc

#### metrics.prometheus.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### metrics.prometheus.pvc.size

Default: `"40Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### metrics.prometheus.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### metrics.loki

#### metrics.loki.image

Default: `"grafana/loki:3.6.3"`

The container image to use for the Loki service.

#### metrics.loki.retention

Default: `"28d"`

How long to retain logs in Loki. After this time, logs will be automatically deleted. Supported units: `d`, `h`, `m`, `s`.

### metrics.loki.pvc

#### metrics.loki.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### metrics.loki.pvc.size

Default: `"4Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### metrics.loki.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### metrics.alloy

#### metrics.alloy.image

Default: `"grafana/alloy:v1.12.2"`

The container image to use for the Alloy service.

### metrics.nodeExporter

Configure the Node Exporter service.

#### metrics.nodeExporter.enabled

Default: `true`

If enabled, a [Prometheus Node Exporter](https://github.com/prometheus/node_exporter) will be created to scrape node metrics from the cluster.

This requires the operator to have permission to manage resources at the cluster scope, which is granted when the `enableNodeMetrics` Helm chart value is set.

If not set, the default value is set by the `ANVIL_ENABLE_NODE_METRICS` environment variable or `enableNodeMetrics` Helm chart value, which is `true` by default.

#### metrics.nodeExporter.image

Default: `"quay.io/prometheus/node-exporter:v1.8.2"`

The container image to use for the Node Exporter pods.

### metrics.queryExporter

Configure the Prometheus postgres query exporter.

#### metrics.queryExporter.image

Default: `"adonato/query-exporter:4.0.1"`

The container image to use for the Prometheus postgres query exporter.

## [Tempo](#tempo)

Configure the Tempo tracing service.

#### tempo.enabled

Default: `true`

Enable the Tempo service.

#### tempo.image

Default: `"grafana/tempo:2.9.1"`

The container image to use for the Tempo service.

#### tempo.config

Default: `{}`

Additional environment variables for the Tempo service.

#### tempo.retention

Default: `"14d"`

How long to retain traces in Tempo. If set to `"forever"`, traces will be retained indefinitely. Supported units: `d`, `h`, `m`, `s`.

### tempo.pvc

#### tempo.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### tempo.pvc.size

Default: `"4Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### tempo.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

## [Pods](#pods)

Configure the Kubernetes pods used in the cluster (excluding Deployment Pools, which have their own `pods` configuration).

Each pod definition has a `resources` and `affinity` field. If neither of these are specified for a pod, the top-level `pods.resources` and `pods.affinity` will be used.

For example, the following specifies a 2GiB memory request for the containers in the `downlinkRunner` pod, but uses a 1GiB request for the containers in all other pods:

```yaml
pods:
  resources:
    requests:
      memory: 1Gi
  downlinkRunner:
    resources:
      requests:
        memory: 2Gi
```

### pods.resources

Configure the resources requests and limits for the containers in the pod. See the [Kubernetes Resource Management documentation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) for more information.

#### pods.resources.requests

Default: `null`

#### pods.resources.limits

Default: `null`

### pods.affinity

#### pods.affinity.node

Default: `null`

Configure the node affinity for the pod by specifying a dictionary of keys and values to be used as `requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms`.

For example, the following specifies that the pod must be scheduled on `anvil-node-0`:

```yaml
pods:
  affinity:
    node:
      kubernetes.io/hostname: anvil-node-0
```

See the [Kubernetes Node Affinity documentation](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#node-affinity) for more information.

#### pods.affinity.pod

Default: `null`

Configure the pod affinity for the pod by specifying a dictionary of keys and values to be used as `requiredDuringSchedulingIgnoredDuringExecution.labelSelector`s.

For example, the following specifies that the pod must be scheduled on the same node as any pods with the label `foo=bar`:

```yaml
pods:
  affinity:
    pod:
      foo: bar
```

See the [Kubernetes Pod Affinity documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) for more information.

### pods.platformServers

No Downtime

Pod configuration (`resources` and `affinity`) for the platform servers.

### pods.platformServers.gitServer

No Downtime

Pod configuration (`resources` and `affinity`) for the git server. If not set, the parent `pods.platformServers` configuration will be used.

### pods.databases

Pod configuration (`resources` and `affinity`) for the databases.

### pods.databases.platform

Pod configuration (`resources` and `affinity`) for the platform database. If not set, the parent `pods.databases` configuration will be used.

### pods.databases.dataTables

Pod configuration (`resources` and `affinity`) for the data tables database. If not set, the parent `pods.databases` configuration will be used.

### pods.databases.appLogs

Pod configuration (`resources` and `affinity`) for the app logs database. If not set, the parent `pods.databases` configuration will be used.

### pods.databases.accountingDb

Pod configuration (`resources` and `affinity`) for the accounting database. If not set, the parent `pods.databases` configuration will be used.

### pods.migrator

Pod configuration (`resources` and `affinity`) for the database migrator.

### pods.loadBalancer

Pod configuration (`resources` and `affinity`) for the load balancer.

### pods.pdfRenderer

Pod configuration (`resources` and `affinity`) for the PDF renderer.

### pods.agentRunner

Pod configuration (`resources` and `affinity`) for the Agent runners.

### pods.legacyDownlink

Pod configuration (`resources` and `affinity`) for the legacy downlink.

### pods.downlinkRunner

Pod configuration (`resources` and `affinity`) for the downlink runner.

### pods.downlinkRegistry

Pod configuration (`resources` and `affinity`) for the downlink registry.

### pods.backupServer

Pod configuration (`resources` and `affinity`) for the backup SSH server.

### pods.grafana

Pod configuration (`resources` and `affinity`) for the Grafana server.

### pods.prometheus

Pod configuration (`resources` and `affinity`) for the Prometheus server.

### pods.tempo

Pod configuration (`resources` and `affinity`) for the Tempo server.

### pods.nodeExporter

Pod configuration (`resources` and `affinity`) for the Prometheus node exporter.

### pods.queryExporter

Pod configuration (`resources` and `affinity`) for the Prometheus postgres query exporter.

### pods.loki

Pod configuration (`resources` and `affinity`) for the Loki server.

### pods.alloy

Pod configuration (`resources` and `affinity`) for the Grafana Alloy server.

### pods.monitor

Pod configuration (`resources` and `affinity`) for the Anvil cluster monitor.

## [Storage](#storage)

#### storage.defaultStorageClass

Default: `null`

Override the default storage class for non-retained PVCs. When these PVCs are deleted, their underlying volumes should also be deleted.

#### storage.defaultRetainedStorageClass

Default: `null`

Override the default storage class for retained PVCs. When these PVCs are deleted, their underlying volumes should not be deleted.

This is used for backup PVCs to prevent accidental deletion of the backup volume.

### storage.appSourceCode

#### storage.appSourceCode.dataPath

Default: `""`

The path inside the PVC to use for storage.

### storage.appSourceCode.pvc

#### storage.appSourceCode.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### storage.appSourceCode.pvc.size

Default: `"4Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### storage.appSourceCode.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### storage.platformDb

#### storage.platformDb.dataPath

Default: `"/data"`

The path inside the PVC to use for storage.

### storage.platformDb.pvc

#### storage.platformDb.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### storage.platformDb.pvc.size

Default: `"4Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### storage.platformDb.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### storage.appLogsDb

#### storage.appLogsDb.dataPath

Default: `"/data"`

The path inside the PVC to use for storage.

### storage.appLogsDb.pvc

#### storage.appLogsDb.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### storage.appLogsDb.pvc.size

Default: `"4Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### storage.appLogsDb.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### storage.accountingDb

#### storage.accountingDb.dataPath

Default: `"/data"`

The path inside the PVC to use for storage.

### storage.accountingDb.pvc

#### storage.accountingDb.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### storage.accountingDb.pvc.size

Default: `"4Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### storage.accountingDb.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### storage.dataTablesDb

#### storage.dataTablesDb.dataPath

Default: `"/data"`

The path inside the PVC to use for storage.

### storage.dataTablesDb.pvc

#### storage.dataTablesDb.pvc.existingClaimName

Default: `null`

The name of an existing PVC to use. If the PVC doesn’t exist, a new one will be created.

#### storage.dataTablesDb.pvc.size

Default: `"4Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### storage.dataTablesDb.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### storage.downlinkContainerData

Storage configuration for the downlink runners.

### storage.downlinkContainerData.pvc

#### storage.downlinkContainerData.pvc.size

Default: `"40Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### storage.downlinkContainerData.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

### storage.downlinkRegistry

Storage configuration for the downlink registry.

### storage.downlinkRegistry.pvc

#### storage.downlinkRegistry.pvc.size

Default: `"40Gi"`

The size of the PVC to create, specified as a [Kubernetes Quantity](https://kubernetes.io/docs/reference/glossary/#term-quantity).

This field is ignored if the PVC already exists.

#### storage.downlinkRegistry.pvc.storageClass

Default: `null`

The storage class to use for the PVC. If not set, the cluster’s `storage.defaultStorageClass` will be used.

This field is ignored if the PVC already exists.

## [Secret Names](#secret-names)

Configure the names of the Kubernetes Secrets used by the cluster. These Secrets are created automatically if they don’t already exist.

#### secretNames.platformServerKeys

Default: `"anvil-<cluster-name>-platform-server-keys-<suffix-token>"`

#### secretNames.platformDbCreds

Default: `"anvil-<cluster-name>-platform-db-creds-<suffix-token>"`

#### secretNames.appLogsDbCreds

Default: `"anvil-<cluster-name>-app-logs-db-creds-<suffix-token>"`

#### secretNames.accountingDbCreds

Default: `"anvil-<cluster-name>-accounting-db-creds-<suffix-token>"`

#### secretNames.dataTablesDbCreds

Default: `"anvil-<cluster-name>-data-tables-db-creds-<suffix-token>"`
