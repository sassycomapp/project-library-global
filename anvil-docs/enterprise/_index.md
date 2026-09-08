---
title: "Anvil Enterprise"
url: "/docs/enterprise"
---


# [Anvil Enterprise](#anvil-enterprise)

Enterprise customers often need to keep their data within their own network, and this is a fully-supported deployment option. Customers who want to manage their own hosting can install Anvil on their own servers. This could be your own network, a private cloud, or an account in a public cloud. Enterprise installations provide the following benefits:

-   Protection for highly sensitive data that must remain within your network
-   Direct access from your Anvil Apps to resources inside your network
-   On-site or private cloud (eg AWS) deployment
-   Direct SQL access to your [data tables](/docs/data-tables)
-   Complete control over the server environment your apps run in
-   Isolation from other users, with dedicated hardware

Deploy with [Kubernetes](enterprise/deployment/kubernetes), [Docker](enterprise/deployment/docker), or with a [Custom deployment package](enterprise/deployment/custom). Not sure which you need? [Get in touch to discuss the options](mailto:sales@anvil.works).

## [Recommended Deployment Patterns](#recommended-deployment-patterns)

We recommend different deployment options depending on your use-case and the type of infrastructure you usually run.

> **“We run everything on-prem on our own hardware, and provision Virtual Machines as required”**

**Recommended deployment**: [K3s](enterprise/deployment/kubernetes/k3s). This lightweight Kubernetes environment will allow you to get up and running with minimal fuss, while still supporting high-availability and zero-downtime updates if required.

> **“We already use Azure AKS, AWS EKS, or Google GKE”**

**Recommended deployment**: [AKS](enterprise/deployment/kubernetes/aks), [EKS](enterprise/deployment/kubernetes/eks) or [GKE](enterprise/deployment/kubernetes/gke). If you’re already using one of these managed Kubernetes environments, you can deploy Anvil there. You may choose to create a dedicated cluster just for Anvil, or deploy it to a particular namespace of an existing cluster. Either way, the [Anvil Operator](enterprise/deployment/operator) will take care of everything for you.

> **“We already use Azure, AWS or GCP, but not Kubernetes”**

**Recommended deployment**: [AKS](enterprise/deployment/kubernetes/aks), [EKS](enterprise/deployment/kubernetes/eks) or [GKE](enterprise/deployment/kubernetes/gke) are easy to get up and running with our standard Terraform configurations, even if you’re not a Kubernetes expert. Start with our deployment guides, and [get in touch](mailto:sales@anvil.works) if you need any help.

> **“I really don’t want to deploy in Kubernetes”**

**Recommended deployment**: For simple, single-node deployments, you can use Docker Compose. See [our deployment guide here](enterprise/deployment/docker).

> **“I’m not sure”**

**No problem!** [Get in touch](mailto:sales@anvil.works) and we’ll be glad to discuss the options with you.
