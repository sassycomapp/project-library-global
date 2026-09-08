---
title: "K3s"
url: "/docs/enterprise/deployment/kubernetes/k3s"
---


# [K3s: Lightweight Kubernetes](#k3s-lightweight-kubernetes)

[K3s](https://k3s.io/) provides a single-binary Kubernetes implementation suitable for production workloads with minimal overhead.

Start by collecting the [Anvil Enterprise Prerequisites](../prerequisites), and the [Anvil Kubernetes Prerequisites](k8s-prerequisites), then install K3s directly on your virtual machine:

```bash
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --disable=traefik" sh -s -
```

Then copy the kubeconfig file to your local machine and verify that you can connect to the cluster using [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl):

```bash
scp root@hostname:/etc/rancher/k3s/k3s.yaml ~/.kube/config
ssh -L6443:localhost:6443 hostname
kubectl get nodes
```

## [Network Access](#network-access)

When running in K3s, Anvil will make itself available on ports 80 and 443 of the host machine by default. Add DNS records for your [primary and wildcard domains](../prerequisites#domain-names) pointing to the machine where you installed K3s.

## [Storage](#storage)

Anvil will store your App source code and database contents in the default K3s Local Path Provisioner storage location on the local disk unless configured otherwise. It is possible to customise this - please discuss with your Anvil representative for full details.

## [Install Anvil](#install-anvil)

Once K3s is installed and configured, you can [proceed with the Anvil Enterprise installation process](installation).
