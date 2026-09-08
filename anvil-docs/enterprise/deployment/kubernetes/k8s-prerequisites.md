---
title: "K8s Prerequisites"
url: "/docs/enterprise/deployment/kubernetes/k8s-prerequisites"
---


# [Kubernetes Prerequisites](#kubernetes-prerequisites)

To get Anvil up and running in Kubernetes, you’ll need a few tools installed on your local machine. These will allow you to manage the deployment.

## [Kubectl](#kubectl)

Kubectl is the Kubernetes command-line tool, allowing you to run commands against Kubernetes clusters. [Download it here](https://kubernetes.io/docs/tasks/tools/#kubectl).

## [Helm](#helm)

Helm allows you to manage versioned releases inside Kubernetes. We use it to install and manage the [Anvil Operator](../operator). [Download it here](https://helm.sh/docs/intro/install/).

## [Kubernetes UI](#kubernetes-ui)

While it is possible to manage all aspects of a Kubernetes cluster via `kubectl` directly, there are many management tools that offer higher-level control over your cluster resources. You’ll need one of them - we recommend [Freelens](https://freelensapp.github.io/) or [K9s](https://github.com/derailed/k9s/releases).
