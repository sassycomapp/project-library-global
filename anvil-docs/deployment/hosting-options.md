---
document: "Hosting options"
title: "Hosting options"
url: "/docs/deployment/hosting-options"
doc-id: hosting-options
state: Live
date-created: 2026-09-08
---


# [Hosting options](#hosting-options)

## [Hosting by us (default)](#hosting-by-us-default)

By default, Anvil apps are hosted in our cloud servers without requiring any configuration from you.

We handle the scaling of your app. The amount of compute and storage you can use is [decided by your pricing plan](https://anvil.works/pricing). Your compute limit is expressed in terms of **compute units**. One compute unit corresponds to a single server function running continuously. How that is used depends on your application - it could be tens of thousands of users performing lightweight operations, or a single user running heavy-duty simulation code.

We will let you know if you are anywhere near your usage limit, and we won’t deny your users access the instant you exceed your limit - we will simply make you aware and discuss how to proceed.

Anvil’s infrastructure currently lives in London (AWS eu-west-2).

## [Deploy on your own hardware, develop in the cloud](#deploy-on-your-own-hardware-develop-in-the-cloud)

If you want to host your Anvil apps on your own computers, but don’t mind developing in the cloud, you can use the open-source [Anvil App Server](https://github.com/anvil-works/anvil-runtime). Develop in the cloud using any of our cloud pricing plans, then export your app from the cloud editor to your machine and launch it as a standalone server.

See our [how-to guides](/docs/how-to/app-server) or find the App Server’s [documentation on GitHub](https://github.com/anvil-works/anvil-runtime) to learn more.

## [On-site Enterprise installations](#on-site-enterprise-installations)

Customers who want to manage their own hosting can install Anvil **[on-site](/docs/overview/enterprise)**. This could be on your own network, a private cloud, or an account in a public cloud. We will help with the installation or perform it for you. Anvil runs as three Docker containers and installing is usually as simple as running a single shell command (`docker-compose up`).

Anvil Enterprise does not require connection to the internet, so you can run it behind restrictive firewalls (or even with an air-gap) for even greater security.

Contact us at [enterprise@anvil.works](mailto:enterprise@anvil.works) to discuss further.

## [Managed Enterprise instances](#managed-enterprise-instances)

If you want the advantages of an on-site installation without managing things yourself, we can manage your installation for you in a public cloud provider like AWS or Azure. You still get a whole Anvil system dedicated to your organisation.

Contact us at [enterprise@anvil.works](mailto:enterprise@anvil.works) to discuss further.
