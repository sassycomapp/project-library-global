---
title: "Pricing plans"
url: "/docs/plans-and-accounts/free-vs-paid"
---


# [Pricing plans](#pricing-plans)

It is free to use Anvil, even for commercial purposes. However, certain features are only unlocked for users of one of our [paid plans](/pricing). These include:

-   Removing the Anvil branding banner from your apps
-   Using your own domain name for your apps
-   Using scheduled tasks

You can also upgrade to higher plans for higher performance, to collaborate with multiple developers in an organisation, receive private support from our team, or even to deploy Anvil on-site within your organisation.

Regardless of your plan, all Anvil users are welcome to ask and answer questions on the [Anvil community forum](https://anvil.works/forum). For more information on our price plans, see our [pricing page](/pricing), or contact [sales@anvil.works](mailto:sales@anvil.works).

## [Shared Hosting](#shared-hosting)

Free, Hobby and Business plans all use fully shared hosting. All your traffic is handled by shared servers; your Server Modules run in the same place as everyone else’s; your Data Tables data lives in shared databases.

Below is a rough guide of the computational capacity of these paid plans:

-   The **Free** plan has performance suitable for one or two low throughput/bandwidth apps.
-   The **Hobby** plan has performance suitable for a few hobby projects or a single production app.
-   The **Business** plan is for business use by a 1+ developers. It has performance suitable for one or two production apps.
-   The **Production** plan supports scaling to thousands of concurrent users for typical apps, and allows you to add extra capacity at AWS cost price.

## [Production Plan](#production-plan)

For customers who need extra performance and support, we offer the Production plan. This includes **private email support** and **high performance server resources**.

### Priority Support

Developers on the Production plan receive direct support from our team – drop us a line at [support@anvil.works](mailto:support@anvil.works) and we will reply within one business day. Ask us questions like:

-   What’s the best way to do using Anvil?

-   How should we optimise this app’s performance?

-   This application is behaving strangely; can you help me debug this?

### High-Performance Server Modules and Tables

For customers on the Production plan, your apps’ Data Tables and Server Modules are hosted on specially reserved compute resources within our cloud infrastructure, making them lightning fast, while still sharing the same cloud editor and serving infrastructure as other plans. This is great for high-traffic, high-performance applications, or for extra assurance that your apps are isolated from other users of the Anvil platform. It also offers you [direct SQL access](../data-tables/indexing-and-sql) to your Data Tables.

-   Increased performance (reserved CPU and RAM for your apps)
-   Improved isolation from other users
-   Direct SQL access to your [Data Tables](/docs/data-tables)

By default, a Production plan includes 2 CPU cores, 4GB of RAM and 50GB of backed-up storage, but you can also specify any compute instance supported by AWS at cost price. We’ll pass on the AWS price with no added markup.

Production plans still share some resources with our other shared-hosting plans. If you would like to host an entirely isolated instance of Anvil, consider [Anvil Enterprise](#anvil-enterprise). Anvil Enterprise instance is exclusively for one customer’s use, and entirely isolated from other users.

### Get Started with Production

Production pricing is fixed, but you’ll need to talk to us to coordinate migration of your data to your new reserved resources.

To switch to Production, or to ask further questions, email [sales@anvil.works](mailto:sales@anvil.works) to get started.

[Get in touch](mailto:sales@anvil.works?subject=Starting+a+Business+Plus+plan)

---

## [Anvil Enterprise](#anvil-enterprise)

If you are interested in our Enterprise Plan, please get in touch by sending an email to [sales@anvil.works](mailto:sales@anvil.works).

Enterprise customers often need to keep their data within their own network, and this is a fully-supported deployment option. Customers who want to manage their own hosting can install Anvil on their own servers. This could be your own network, a private cloud, or an account in a public cloud. On-site installations provide the following benefits:

-   Protection for highly sensitive data that must remain within your network
-   On-site or private cloud (eg AWS) deployment
-   Direct SQL access to your [data tables](/docs/data-tables)
-   Complete control over the server environment your apps run in
-   Isolation from other users, with dedicated hardware

We will help with the installation or perform it for you. In a typical installation, Anvil is three Docker containers and installing is usually as simple as running a single shell command (`docker-compose up`). We can also provide custom installation packages where Docker is not an option, or for integration with existing services.

Anvil does not need an Internet connection - you can even use it on a network completely airgapped from the Internet to give you an even greater guarantee of security.

Get in touch with us at [contact@anvil.works](mailto:contact@anvil.works) to discuss further - we would be happy to talk you through the Enterprise deployment options and offer advice about your specific use-cases.

[Get in touch](mailto:contact@anvil.works)

## [Hosting Standalone Applications](#hosting-standalone-applications)

This section is for hosting standalone applications only. If you are interested in a full on-site installation, including the Anvil editor, see Anvil Enterprise.

### Open-source App Server

Users who want to set up their own server to host their Anvil apps can use our open source [Anvil Runtime Engine](https://github.com/anvil-works/anvil-runtime). This allows you to export Anvil apps and run them on any computer, without depending on our hosting platform. This option is available on all plans.

### Enterprise App Server

The Enterprise App Server is the supported version of the Open-source App Server. It offers the ability to host your apps on any machine with no AGPL licence. It also includes extra features for scalability, such as integrated Backup and Restore and Multi-node Clustering.

If you’re interested or want more details, please get in touch by sending an email to [sales@anvil.works](mailto:sales@anvil.works)

Volume licensing for IoT is available. If you’re interested in distributing the Enterprise App Server for IoT devices send us an email at [sales@anvil.works](mailto:sales@anvil.works).
