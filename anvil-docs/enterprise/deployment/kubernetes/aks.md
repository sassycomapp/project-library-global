---
document: "Azure AKS"
title: "Azure AKS"
url: "/docs/enterprise/deployment/kubernetes/aks"
doc-id: aks
state: Live
date-created: 2026-09-08
---


# [Azure Managed Kubernetes Service](#azure-managed-kubernetes-service)

Anvil Enterprise is fully supported in AKS. Once you have collected the [Anvil Enterprise Prerequisites](../prerequisites) and the [Anvil Kubernetes Prerequisites](k8s-prerequisites), the easiest way to get up and running is to use [Terraform](https://developer.hashicorp.com/terraform/install?product_intent=terraform) to create a new AKS cluster using our standard AKS template. Please [get in touch for access to this](mailto:sales@anvil.works).

If you’ve never used AKS before, this [tutorial from Microsoft](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster?tabs=azure-cli) will help you install the Azure CLI tools and create a new AKS cluster.

## [Install the Azure CLI](#install-the-azure-cli)

Before proceeding with an installation in AKS, you will need the [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed on your local machine. (If you followed the tutorial, you’ve already done this!)

## [Create an AKS cluster](#create-an-aks-cluster)

If you don’t have one already, the easiest way to deploy an AKS cluster is to follow the [Microsoft tutorial](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster?tabs=azure-cli).

If you prefer to manage your deployment with code, you should instead use our standard AKS terraform template. Please contact your Anvil representative for this template.

## [Optional Configuration](#optional-configuration)

When working in the US Government Azure Cloud, initialise the Azure CLI with the following commands:

```bash
az cloud set --name AzureUSGovernment
az login
az account set --subscription 'YOUR_SUBSCRIPTION_ID'
```

## [Install Anvil Enterprise](#install-anvil-enterprise)

Once logged in to the Azure CLI, and with an AKS cluster deployed, you can [proceed with the Anvil Enterprise installation process](installation).
