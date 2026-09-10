---
title: "Installation"
url: "/docs/enterprise/deployment/kubernetes/installation"
doc-id: installation
state: Live
date-created: 2026-09-08
---


# [Installation in Kubernetes](#installation-in-kubernetes)

This guide assumes you are comfortable working at a terminal. You should have the necessary [Anvil Enterprise Prerequisites](../prerequisites) and [Kubernetes Prerequisites](k8s-prerequisites) ready.

Make sure your cluster is fully set up before attempting the steps in this section. You can follow one of our guides for the major cloud providers, or our [K3s guide](k3s) if installing directly on a virtual machine. To check that you’re ready, run `kubectl get nodes` and check that it returns without any errors.

Once you have a Kubernetes cluster available, you can go ahead with the installation of Anvil Enterprise. Wherever you see `$VARIABLE_NAME` in the commands below, substitute the appropriate value for your deployment.

## [Prepare the cluster](#prepare-the-cluster)

If you will be installing Anvil in a namespace other than `default`, create that first:

```bash
kubectl create namespace anvil
```

The following commands assume that you are installing into the `anvil` namespace - remove or modify the “`-n anvil`” flag below if not.

Next install secrets containing your Anvil licence key and your Anvil Registry credentials:

```bash
kubectl create -n anvil secret docker-registry anvil-registry-creds \
    --docker-server=anvil.works \
    --docker-username=$ANVIL_DOCKER_USERNAME \
    --docker-password=$ANVIL_DOCKER_PASSWORD

kubectl create -n anvil secret generic anvil-licence-key \
    --from-literal=value=$ANVIL_LICENCE_KEY
```

If you have generated [TLS certificates](../prerequisites/tls-certificates) for your Anvil installation, create Secrets to store those now. You can skip this step if you are using the [AWS Certificate Manager with EKS](eks#domain-names-and-tls-certificates), or if you want Anvil to generate self-signed certificates for you.

Include as many certificates as needed, but there must be a matching `.key` filename for each `.crt` file.

```bash
kubectl create -n anvil secret generic anvil-certs \
    --from-file=tls.key=./privkey.pem --from-file=tls.crt=./fullchain.pem \
    --from-file=tls2.key=./privkey2.pem --from-file=tls2.crt=./fullchain2.pem \
    ...
```

## [Install the Anvil Operator](#install-the-anvil-operator)

Now install the [Anvil Operator](../operator), which will manage your Anvil Cluster for you. If you’re installing on EKS, you should skip the final `helm install` command here and use the [EKS-specific one](eks#install-anvil) instead.

```bash
helm repo add anvil https://charts.anvil.works
helm install -n anvil anvil-crds anvil/anvil-crds
# If using EKS, skip the following and use the EKS-specific command instead (see above)
helm install -n anvil anvil-operator anvil/anvil-operator --set version=$OPERATOR_VERSION
```

The Anvil Operator can be updated at any time by creating a new Helm release with an updated `version` value. Updating the operator will not affect your running Anvil installation inside Kubernetes.

```bash
helm uninstall -n anvil anvil-operator
helm repo update
# If using EKS, skip the following and use the EKS-specific command instead (see above)
helm install -n anvil anvil-operator anvil/anvil-operator --set version=$OPERATOR_VERSION
```

## [Install Anvil Enterprise](#install-anvil-enterprise)

With the operator installed, you are ready to proceed with your Anvil Enterprise installation. Your Anvil cluster is described by a single Kubernetes Custom Resource in a YAML file. This will be pre-configured and provided to you by a member of the Anvil team during the installation. Install it with the following command:

```bash
kubectl apply -f anvil-cluster.yml
```

The [Anvil Operator](../operator) will notice the new Anvil Cluster resource and create all the necessary Kubernetes Resources for your cluster. Once your DNS records are installed, you can visit your local Anvil Enterprise installation by typing your chosen primary domain name into your browser.
