---
title: "Prerequisites"
url: "/docs/enterprise/deployment/prerequisites"
doc-id: prerequisites-_index
state: Live
date-created: 2026-09-08
---


# [Prerequisites](#prerequisites)

However you choose to deploy Anvil Enterprise, there are a few things you’ll need to set up first.

## [Domain Names](#domain-names)

Anvil requires two domain names to operate:

-   A primary domain (`anvil.example.com`). This is where your developers will access the Anvil development environment.
-   A wildcard app domain (`*.apps.example.com`). This is where your Anvil Apps will be deployed — each app gets its own subdomain.

We also recommend provisioning a third domain to use for metrics and monitoring (`metrics.anvil.example.com`).

Once you’ve chosen your domain names, make sure you are able to configure DNS records to point them to your deployment environment. If you’re deploying to AWS, then [Anvil can automatically handle DNS and TLS configuration for you](kubernetes/eks#domain-names-and-tls-certificates).

For trial purposes, it is possible to configure Anvil Enterprise to run from a single hostname. **Do not do this in production** as it removes the security barriers between applications and the Anvil editor.

## [TLS Certificates](#tls-certificates)

You have a choice of using an Anvil-supplied service to perform HTTPS termination, or using your own infrastructure (e.g. an HTTP load balancer). See the [TLS Certificates](prerequisites/tls-certificates) page for more details.

If you’re deploying to AWS, then [Anvil can automatically handle DNS and TLS configuration for you](kubernetes/eks#domain-names-and-tls-certificates).

## [SMTP Credentials](#smtp-credentials)

Anvil requires the ability to send email. You’ll need credentials for an SMTP service — if you need an external provider, we recommend Sendgrid or AWS SES.

## [Licence Key and Registry Credentials](#licence-key-and-registry-credentials)

In order to run Anvil Enterprise, you will need a licence key and credentials for the Anvil Registry in order to pull the necessary container images. These will be shared with you by a member of the Anvil team during the installation process.

## [SSO Credentials (Optional)](#sso-credentials-optional)

Anvil includes native integrations for a number of external services. Each of these features is optional, but if you want to use them with Anvil Enterprise you will need to obtain credentials:

-   [Google SSO](prerequisites/google)
-   [Microsoft SSO](prerequisites/microsoft)
-   [GitHub SSO](prerequisites/github)
