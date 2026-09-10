---
title: "AWS Lightsail"
url: "/docs/how-to/app-server/cloud-deployment-guides/aws-lightsail-app-server-deployment"
doc-id: aws-lightsail-app-server-deployment
state: Live
date-created: 2026-09-08
---


# [How to use Anvil’s open-source App Server on an AWS Lightsail instance](#how-to-use-anvils-open-source-app-server-on-an-aws-lightsail-instance)

## [Introduction](#introduction)

[Anvil](https://anvil.works/) is a platform for building full-stack web apps with nothing but Python. No need to wrestle with JS, HTML, CSS, Python, SQL and all their frameworks – just build it all in Python.

Anvil also offers [one-click deployment](https://anvil.works/docs/deployment/quickstart) to the cloud. Cloud deployment is, in the vast majority of scenarios, the quickest and easiest way to get apps up and running. However, we understand that there are scenarios in which you require your app to be deployed to your own server. To deploy your app to your own server, Anvil provides the open source [Anvil App Server](https://anvil.works/docs/deployment/quickstart).

In this guide, we will demonstrate how to deploy an Anvil app to [Amazon Lightsail](https://aws.amazon.com/lightsail/). We will start by creating an environment on your server and installing the Anvil App Server. Then, we will configure our domain name for the server. Next, we will clone your Anvil app from the [Anvil editor](https://anvil.works/docs/editor). We will then run your Anvil app and access it via your domain.

## [Prerequisites](#prerequisites)

### Initial Server Setup

For this guide, we will use an Amazon Web Services (AWS) Lightsail instance. We are using a Lightsail with a fresh **Ubuntu 18.04** server install.

I will also be using the provided `ubuntu` user that comes with a fresh AWS Lightsail instance. We can use any user that has `sudo` privileges.

On this server we are using Python version 3.6.5, although any **Python version >=2.7 or >=3.6** will work with the Anvil App Server.

### Updating the server package list

To start, we are going to run:

```bash
~$ sudo apt-get update
```

This updates the package list on my server. For more information on `apt-get update`, there is a good summary [provided here](https://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do).

### Installing the Java virtual machine and Python virtual environment package

Next, we need to install the Java virtual machine for the Anvil App Server and the Python venv (virtual environment) package. On our Lightsail instance, we can run:

```bash
~$ sudo apt-get install python3-venv openjdk-8-jdk
```

### Allowing our user to create a service on 443

The next commands require `root`, so let’s start by changing to our user to root:

```bash
~$ sudo su -
```

On many Linux systems unprivileged users cannot create services on port 443. This is a somewhat archaic restriction, and there are a few ways around it. The simplest is to turn it off, with the commands:

```bash
~# echo 'net.ipv4.ip_unprivileged_port_start=0' > /etc/sysctl.d/50-unprivileged-ports.conf
~# sysctl --system
```

(There are all sorts of other configurations you can use for HTTPS; see the [README file](https://github.com/anvil-works/anvil-runtime/blob/master/README.md) for all the gory details.)

We have now installed and configured everything we need as the root user. It’s time to switch back to the user we logged onto our server with and install the App Server in a virtual environment in their home directory.

## [Creating your virtual environment](#creating-your-virtual-environment)

Let’s start by switching to the user we logged onto our server with:

```bash
~# su ubuntu
```

We are going to start by creating a virtual environment for the Anvil Standalone Runtime to be contained in. The directory I’m creating my environment in is my users [home directory](https://help.ubuntu.com/community/HomeFolder). To navigate there we can run:

```bash
~$ cd ~
```

We create a [Python virtual environment](https://docs.python.org/3/library/venv.html) by running:

```bash
~$ python3 -m venv env
```

Creating a virtual environment provides us with an isolated environment separate from any other apps we may install or develop on this server. Our virtual environment will contain the Anvil App Server, its dependencies and any other Python packages we want to install for our Anvil app.

To activate our virtual environment, we run the following command:

```bash
~$ source env/bin/activate
```

We are now ready to install the Anvil App Server, along with its dependencies and packages.

## [Installing the Anvil App Server](#installing-the-anvil-app-server)

Next we are going to install the Anvil App Server. The Anvil app server is available on [PyPI](https://pypi.org/project/anvil-app-server/), so we can install it with pip:

```bash
(env) ~$ pip install anvil-app-server
```

If you want to use additional Python packages (e.g. numpy, pandas) in your app’s server-side code, you should make sure these are installed too!

Now the Anvil App Server is installed, let’s configure our domain name.

## [Adding your own domain name](#adding-your-own-domain-name)

To set up a domain name, we first need to purchase a domain name from a domain name registrar.

Once we have purchased the domain name, we need to update the name servers used by the domain registrar to use AWS instead. Each registrar should have documentation on how to change your domain’s name servers.

The name servers we need to update our domain provider to use can be found by creating a DNS zone in our Lightsail homepage.

Select **Create DNS zone** and enter the domain name we have registered. Create the DNS zone and we will be brought to the Details page which lists the Name servers at the bottom. Copy the name servers and add them to your domain name registrar.

Our next step is to create the type A DNS records required by Anvil, this can be done on the same DNS zone details tab. For this guide I’m going to add two A type DNS records.

| Type | Subdomain | Resolves to |
|---|---|---|
| A | www | server_IP |
| A | @ | server_IP |

For more information, Amazon provides a useful tutorial that covers [creating DNS records here](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/lightsail-how-to-create-dns-entry).

DNS changes take a while to propagate around the internet, so you may need to wait up to 48 hours before your changes fully take effect.

Once the changes have been made, we’re ready to start the app server.

## [Adding your Anvil app](#adding-your-anvil-app)

### Creating an Anvil App

For this guide, we are going to use the News Aggregator app from [one of our tutorials](https://anvil.works/learn/tutorials/database-backed-apps). If you already have an Anvil app you want to deploy to this server, you can skip straight to Cloning your app to the server with git.

[Click this link](https://anvil.works/build#clone:AOYS4NM7A3XTUODP=NPX5JHZSHDISHBWLSIGAKBXW) to clone the finished News Aggregator app to your Anvil account; you’ll need to [sign up for a free Anvil account](https://anvil.works/sign-up) if you don’t have one yet.

### Cloning your app to the server with git

For this example, I will be cloning the News Aggregator app from my Anvil account to my Lightsail instance.

Each Anvil app is represented by a Git repository. If we click the Clone with Git button in the [Version History dialog](https://anvil.works/docs/version-control), we can see the command to clone our desired app onto our server.

Paste the command into the command line window to clone the desired app onto your server. It will look something like this:

```bash
# Clone your Anvil app onto your machine
$ git clone ssh://ryan%40anvil.works@anvil.works:2222/AOYS4NM7A3XTUODP.git CRUDnewsappwalkthrough
```

You will be asked for your Anvil account password to clone the app.

Alternatively, you can set up an SSH key for your server and add it to your anvil app settings by [following this guide](/docs/how-to/app-server/linux-ssh-key-setup).

When cloned, the Git repository will be placed in a directory named using the app’s package name. The example above would clone the app into a directory named `CRUDnewsappwalkthrough`.

## [Make our app accessible to the world!](#make-our-app-accessible-to-the-world)

Now it’s time to deploy our app to our Anvil App Server for the whole world to access. The best part is, with the Anvil App Server, we can do it all with one command:

```bash
(env)$ anvil-app-server --app CRUDnewsappwalkthrough --origin https://ryans-test-app.xyz/
```

Thanks to Anvil’s built-in integration with Let’s Encrypt, we can specify an https:// origin, and Anvil will take care of the rest.

Let’s Encrypt enforces [rate limits](https://letsencrypt.org/docs/rate-limits/) for certificates. To avoid exceeding these limits while you are testing your setup, you can deploy your app with the [`--letsencrypt-staging`](https://github.com/anvil-works/anvil-runtime#advanced-configuration) flag. This flag produces an invalid ‘staging’ certificate that is not subject to rate limits.

Once you are finished testing your deployment, simply remove the flag to deploy with a production certificate.

We can now browse to our app via our domain and it’s ready to go!

### Edit your app

Once you’ve launched the web server with the anvil-app-server command, you can simply refresh your browser to see changes you make locally - there’s no need to restart the web server!
