---
title: "Host apps on your own server"
url: "/docs/how-to/app-server"
---


# [Host your Anvil Apps on your own computer](#host-your-anvil-apps-on-your-own-computer)

You can export any Anvil app from the Anvil Editor and run it on your computer using the open-source [Anvil App Server](https://github.com/anvil-works/anvil-runtime).

To learn more about the Anvil App Server, take a look at the project on GitHub:

[See the code](https://github.com/anvil-works/anvil-runtime)

## [Features](#features)

-   **Full-stack apps with nothing but Python** - The Anvil App Server runs your client-side code in the web browser, and the server-side code in server-side Python. It even has a built-in database, with rows that can be passed freely between server- and client-side code.

-   **HTTPS out of the box** - If launched with an HTTPS origin, the Anvil App Server will launch an HTTPS reverse proxy and obtain a certificate from [Let’s Encrypt](https://letsencrypt.org).

-   **No configuration required** - The Anvil App Server includes its own database (Postgres) and reverse proxy (Traefik), so all you need to do is launch it. No need to spend half an hour setting up your environment.

-   **Connect code from anywhere** - The Anvil [Uplink](https://anvil.works/docs/uplink) allows you to connect scripts, Jupyter notebooks, or anything else with a Python interpreter to your app.

-   **Interactive shell** - Just launch the server with `--shell` to connect a fresh Python interpreter via the Uplink.

## [How-to Guides for Popular Cloud Services](#how-to-guides-for-popular-cloud-services)

Want to deploy your Anvil app to popular cloud hosting services like AWS? We’ve got [step-by-step guides](/docs/how-to/app-server/cloud-deployment-guides) for a bunch of popular providers.
