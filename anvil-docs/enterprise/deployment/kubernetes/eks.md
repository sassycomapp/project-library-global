---
title: "AWS EKS"
url: "/docs/enterprise/deployment/kubernetes/eks"
---


# [AWS Elastic Kubernetes Service](#aws-elastic-kubernetes-service)

Anvil Enterprise is fully supported in EKS. Once you have collected the [Anvil Enterprise Prerequisites](../prerequisites) and the [Anvil Kubernetes Prerequisites](k8s-prerequisites), the easiest way to get up and running is to use [Terraform](https://developer.hashicorp.com/terraform/install?product_intent=terraform) to create a new EKS cluster using our standard EKS template. Please [get in touch for access to this](mailto:sales@anvil.works).

## [Domain Names and TLS Certificates](#domain-names-and-tls-certificates)

When deploying Anvil to EKS, we recommend using [Route 53](https://aws.amazon.com/route53) and the [AWS Certificate Manager](https://aws.amazon.com/certificate-manager) for your Anvil domains. That way, Anvil can automatically handle DNS and TLS configuration for you.

If you’re using an external DNS provider with Anvil on a subdomain, you can delegate your Anvil domain to Route 53. For example:

-   Create Route 53 Hosted Zones for:
    -   `anvil.example.com`
    -   `apps.example.com`
-   Make a note of the name servers for each Hosted Zone
-   Configure your external DNS provider to point the Anvil domains to Route 53:
    -   NS record for `anvil.example.com` pointing to the corresponding name servers in Route 53
    -   NS record for `apps.example.com` pointing to the corresponding name servers in Route 53

Then use AWS Certificate Manager to create a certificate for the following Anvil domains:

-   `anvil.example.com`
-   `*.apps.example.com`
-   `metrics.anvil.example.com`

Update your [Anvil operator Cluster config](../operator/cluster#load-balancer) to refer to the certificate by its ARN:

```yaml
loadBalancer:
  externalDns: anvil.example.com,*.apps.example.com,metrics.anvil.example.com
  awsNlb:
    certificateArn: arn:aws:acm:eu-west-2:1234567:certificate/ab123-ab123-ab123
```

This will automatically create DNS records pointing to the AWS load balancer, and configure the Anvil reverse proxy to terminate HTTPS using the corresponding certificate credentials.

## [Install the AWS CLI](#install-the-aws-cli)

Before proceeding with an installation in EKS, you will need the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed on your local machine and [configured for access to your AWS account](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html).

## [Create an EKS cluster](#create-an-eks-cluster)

If you don’t have one already, the easiest way to deploy an EKS cluster is to use our standard EKS terraform template. Please contact your Anvil representative for this template.

## [Install Anvil](#install-anvil)

Once logged in to the AWS CLI, and with an EKS cluster deployed, you can [proceed with the Anvil Enterprise installation process](installation). When [installing the Anvil Operator](installation#install-the-anvil-operator), you should use the following `helm install` command. Be sure to substitute your own values for the `version`, `awsAccountId` and `eksClusterName` parameters.

```bash
helm install -n anvil anvil-operator anvil/anvil-operator \
    --set version=$OPERATOR_VERSION \
    --set awsAccountId=$AWS_ACCOUNT_ID \
    --set eksClusterName=$EKS_CLUSTER_NAME \
    --set createStorageClasses=eks
```
