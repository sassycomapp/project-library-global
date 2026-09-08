---
title: "Custom Domains"
url: "/docs/deployment/custom-domains"
---


# [Using your own domain name](#using-your-own-domain-name)

Custom domains are available on the [Hobby Plan](https://anvil.works/pricing) and above

To use a custom domain, you will need to configure your DNS records and your Anvil app. Anvil will take care of the SSL certificate, so you **do not** need to purchase your own SSL or TLS certificate.

## [Configuring your Anvil app](#configuring-your-anvil-app)

First, switch an [environment](environments) to a custom domain.

## [Configuring the DNS records](#configuring-the-dns-records)

Next, create a DNS `A` record pointing your domain to `52.56.203.177`. If you wish to use a subdomain of the domain you purchased (such as `app.mydomain.com`), you can simply configure an `A` record pointing that subdomain to the IP address above. To configure a subdomain, just enter the subdomain in place of the `@` symbol when configuring the `A` record.

If you want to use `www.mydomain.com` as well as `mydomain.com`, you can configure a second `A` record for `www`. In this case, configuring your app to use `mydomain.com` will cause both `www.mydomain.com` and `mydomain.com` to work for your app.

Make sure there are no `AAAA` records for your domain, as these will prevent us from issuing a certificate for your domain.

DNS changes take a while to propagate around the internet, so you may need to wait up to 48 hours before your changes fully take effect.

## [Help and tips](#help-and-tips)

Here are some tips on using a custom domain for some common domain registrars:

### Squarespace Domains

In your domains dashboard, go to ‘DNS’, then ‘DNS settings’ and delete the default records. Click ‘Add’ next to ‘Custom Records’ and find `A` in the Type dropdown.

Advanced note: If you’re using a domain forwarding as a redirect, you need to ensure that “SSL On” is selected. This because Anvil uses HSTS to enforce SSL as part of its security model (so non-SSL connections will not work by design).

### GoDaddy

In the GoDaddy DNS Management page for your domain, you can create an `A` record in the ‘Records’ card.

### Cloudflare

In Cloudflare’s DNS settings tab, add an `A` record in the ‘add record’ tool.

**Cloudflare and SSL**

The cloud icon next to the ‘add’ button toggles Cloudflare’s CDN and other features on or off. Anvil apps will work with either setting. If you’re using Cloudflare’s SSL support, you need change the SSL Support setting from ‘Flexible’ to ‘Full Strict’. See [this article from Cloudflare](https://www.siteground.com/kb/website-goes-redirect-loop-enabling-cloudflare/) for more info. It will take a few minutes to take effect.

## [TLS/SSL Certificates](#tlsssl-certificates)

SSL certificates for hosted apps are managed by Anvil. There will be a delay between setting up your custom domain and the certificates being registered.

You **do not** need to purchase your own SSL or TLS certificate.
