---
title: "Configuration Guide"
url: "/docs/enterprise/deployment/kubernetes/configuration"
---


# [Configuration Guide](#configuration-guide)

The Anvil team will provide you with an `anvil-cluster.yml` configuration file to set up your Anvil cluster. This guide provides some tips and best practices for configuring your Anvil cluster.

After modifying your `anvil-cluster.yml` file in each step below, apply the changes to your cluster using the following command:

```bash
kubectl apply -f anvil-cluster.yml
```

For a full reference of the Anvil Cluster configuration options, see the [Anvil Operator documentation](../operator/cluster).

## [Testing with Port-Forwarding](#testing-with-port-forwarding)

Before configuring your DNS records and TLS certificates, you can test your Anvil deployment by port-forwarding from the Anvil load balancer to your local machine.

First, temporarily change the origins in your `anvil-cluster.yml` file:

```yaml
anvilOrigin: http://localhost:8181
appOrigin: http://localhost:8181/apps/{{id-or-alias}}
```

Leave the string `{{id-or-alias}}` intact. This is a placeholder which will be substituted by Anvil to generate the URL for each app.

Apply this change and port-forward from the Anvil load balancer to your local machine:

```bash
kubectl apply -f anvil-cluster.yml
kubectl port-forward -n anvil pod/anvil-wombat-reverse-proxy 8181:trusted-http
```

You can now test your Anvil deployment from your browser at [http://localhost:8181](http://localhost:8181).

## [Load Balancer Setup](#load-balancer-setup)

Now that you have confirmed that your Anvil deployment is working, it’s time to configure your DNS records and TLS certificates.

The exact steps for this will depend on your deployment environment. The [Anvil Operator documentation](../operator/cluster#load-balancer) contains a detailed reference for configuring the load balancer.

If you are deploying into EKS, refer to the [AWS EKS instructions](eks#domain-names-and-tls-certificates).

The Anvil team can provide detailed guidance for your specific environment.

Once your DNS records and TLS certificates are configured, update the origin configuration in your `anvil-cluster.yml` file to use the correct domain names:

```yaml
anvilOrigin: https://anvil.example.com
appOrigin: https://{{id-or-alias}}.apps.example.com
```

After applying this change, you should see your Anvil deployment at [https://anvil.example.com](https://anvil.example.com).

## [Email Setup](#email-setup)

To configure your email settings, modify your `anvil-cluster.yml` file to include the following:

```yaml
platformServers:
  config:
    # Uncomment the following line to bypass email verification for new users
    # noVerifyEmail: true

    emailFrom: server-notifications@example.com
    smtpHost: smtp.sendgrid.net
    smtpPort: 587
    smtpTls: true
    smtpUser: apikey
    smtpPass: {valueFrom: {secretKeyRef: {name: "anvil-smtp-password", key: "value"}}}
```

Replace the values above with your own SMTP service’s settings, then apply the change to your cluster. You can use the `anvil-smtp-password` secret to store your SMTP password securely in Kubernetes:

```bash
kubectl apply -f anvil-cluster.yml
kubectl create -n anvil secret generic anvil-smtp-password --from-literal=value=$SMTP_PASSWORD
```

Now try signing up as a new user in the Anvil Editor, and check that you receive a verification email. Once verified, you will be told that your account needs to be enabled by an administrator. Let’s do that now.

## [User Management](#user-management)

When a new user signs up in the Anvil Editor for the first time their account is disabled by default. You can manage your user accounts in the admin app at `https://admin.apps.example.com` (replace `apps.example.com` with your app domain name).

The Anvil Operator will automatically create a password for the admin app and store it in a Kubernetes Secret. You can view it with the following command (replace `<cluster-name>` with the `name` field in your `anvil-cluster.yml` file):

```bash
kubectl get -n anvil secret anvil-<cluster-name>-admin-app-password \
  -o jsonpath='{.data.value}' | base64 -d
```

Enable a user by clicking the “Enable” button next to their email address in the Users table. Now when they log in they will have full access to the Anvil Editor.

## [SSO Setup](#sso-setup)

You can configure Anvil Enterprise with SSO credentials for logging in to the Anvil Editor, and for use with your Anvil apps. Once you have [registered for each service](../prerequisites#sso-credentials-optional) that you want to use, add the credentials to your `anvil-cluster.yml` file in the settings below.

Refer to the [Operator documentation](../operator/cluster#platform-servers) for more details on the available SSO settings.

```yaml
platformServers:
  config:
    # For the Anvil Editor only
    anvilGoogleIdeClientId: YOUR_GOOGLE_CLIENT_ID
    anvilGoogleIdeClientSecret: {valueFrom: {secretKeyRef: {name: "anvil-google-ide-client-secret", key: "value"}}}
    # For your Anvil apps
    anvilGoogleClientId: YOUR_GOOGLE_CLIENT_ID
    anvilGoogleClientSecret: {valueFrom: {secretKeyRef: {name: "anvil-google-client-secret", key: "value"}}}

    # For the Anvil Editor only
    anvilMicrosoftIdeAppId: YOUR_MICROSOFT_APP_ID
    anvilMicrosoftIdeAppSecret: {valueFrom: {secretKeyRef: {name: "anvil-microsoft-ide-app-secret", key: "value"}}}
    anvilMicrosoftIdeTenantId: YOUR_MICROSOFT_TENANT_ID  # If required
    # For your Anvil apps
    anvilMicrosoftAppId: YOUR_MICROSOFT_APP_ID
    anvilMicrosoftAppSecret: {valueFrom: {secretKeyRef: {name: "anvil-microsoft-app-secret", key: "value"}}}
    anvilMicrosoftTenantId: YOUR_MICROSOFT_TENANT_ID  # If required

    anvilGithubAppUrl: YOUR_GITHUB_APP_URL
    anvilGithubClientId: YOUR_GITHUB_CLIENT_ID
    anvilGithubClientSecret: {valueFrom: {secretKeyRef: {name: "anvil-github-client-secret", key: "value"}}}
    anvilGithubWebhookSecret: {valueFrom: {secretKeyRef: {name: "anvil-github-webhook-secret", key: "value"}}}
    anvilGithubEnterpriseHostname: YOUR_GITHUB_ENTERPRISE_HOSTNAME  # If required
```

Secrets can be stored in Kubernetes with the following command (replace `$SECRET_NAME` and `$SECRET_VALUE` with your own values):

```bash
kubectl create -n anvil secret generic $SECRET_NAME --from-literal=value=$SECRET_VALUE
```

### GitHub Enterprise

If you’re using GitHub Enterprise with a self-signed certificate, add a DER-formatted certificate file as a Kubernetes Secret:

```bash
kubectl create -n anvil secret generic anvil-extra-certs --from-file=./github_cert.pem
```

Then reference it in your `anvil-cluster.yml` configuration:

```yaml
platformServers:
  config:
    extraCertsSecret: anvil-extra-certs
```

### Anvil Editor Login Methods

Once you have configured your SSO credentials, select which services to use for logging in to the Anvil Editor:

```yaml
platformServers:
  config:
    # Enable one or more of the following:
    anvilEnableEmailLogin: true
    anvilEnableGoogleLogin: true
    anvilEnableMicrosoftLogin: true
    anvilEnableGithubLogin: true
```

## [Backups](#backups)

By default, Anvil Enterprise will automatically back up your databases and source code every 24 hours.

You can configure the [backup settings](../operator/cluster#backup) in your `anvil-cluster.yml` file. For example, if you’re using AWS EKS then you can store your backups in S3:

```yaml
backup:
  target:
    s3:
      bucketName: anvil-eks-backup-example
      pathPrefix: example-backup
```

## [Metrics](#metrics)

When debugging problems with your Anvil deployment, it’s helpful to collect metrics and logs from your cluster. The [metrics settings](../operator/cluster#metrics) can be configured in your `anvil-cluster.yml` file:

```yaml
metrics:
  enabled: true
  domainName: metrics.anvil.example.com
```

If you have configured your DNS and TLS certificates for this domain, you can login to the Grafana dashboard at [https://metrics.anvil.example.com](https://metrics.anvil.example.com). The auto-generated password for the `admin` user is stored in a Kubernetes Secret (replace `<cluster-name>` with the `name` field in your `anvil-cluster.yml` file):

```bash
kubectl get -n anvil secret anvil-<cluster-name>-grafana-admin-password \
  -o jsonpath='{.data.value}' | base64 -d
```
