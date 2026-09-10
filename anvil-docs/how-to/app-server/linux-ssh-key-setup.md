---
title: "Set up an SSH key on Linux"
url: "/docs/how-to/app-server/linux-ssh-key-setup"
doc-id: linux-ssh-key-setup
state: Live
date-created: 2026-09-08
---


# [Setting up an SSH key to clone your Anvil app with Git](#setting-up-an-ssh-key-to-clone-your-anvil-app-with-git)

### Introduction

If you want to `git clone` an Anvil app from the editor onto your machine, you’ll need to prove who you are. The most robust way to authenticate Git access is to set up an SSH key.

This guide will show you how to set up an SSH key on an Linux server, add the SSH key to your [Anvil account](https://anvil.works/login) and clone your Anvil app onto your server with Git. (This guide was written for **Ubuntu 20.04**, but the instructions should be the same for any modern Linux distribution.)

## [Step 1 - Generating the key pair](#step-1---generating-the-key-pair)

First, let’s create a key pair on your Ubuntu server. Start by running the command:

```bash
$ ssh-keygen
```

You should see the following output:

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/your_home/.ssh/id_rsa):
```

Press enter to save the key pair into the `.ssh/` subdirectory in your [home directory](https://help.ubuntu.com/community/HomeFolder).

You will then be prompted for a passphrase. It’s recommended that you enter one, however it isn’t compulsory.

```bash
Enter passphrase (empty for no passphrase):
```

Next you will see an output similar to:

```bash
Your identification has been saved in /your_home/.ssh/id_rsa
Your public key has been saved in /your_home/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:+tHymFI4fMGcyKZ8DPUbGZekbnZZM2tVXYelf5Vwzt4 user@host
The key's randomart image is:
+---[RSA 3072]----+
|         ... . +B|
|      . ..o   *o+|
|     o =.=  + o+.|
|    . +.O  o =..o|
|   . * .S+o o  .E|
|    o *++o .    .|
|     ..+o .      |
|      .. *       |
|       .+ .      |
+----[SHA256]-----+
```

Now you have a public and private key that we can use for authentication between your server and Anvil (or any other Git server).

## [Step 2 - Copying your Public key](#step-2---copying-your-public-key)

Next, let’s get your Public key: `$ cat ~/.ssh/id_rsa.pub`

That will show you the public key, which you can then copy to your clipboard:

```bash
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDhgXxI+HhUJwrYgO2ASMj0hGAtzDYDj0DGNCYF8At7
+3seJjHPl45wMdFe1oUexMRcegcKpYL0gpdtfE34zN8CapbQcmNaRmdCaXxL50cbZRIlWn2OaDxUgbbpH
KzqJdzEuLbTIrYIcvf6OLheTjR7lj/j+342matgOxnKjqJJkFDb226zwxgCAUxhLw+HMuc1LbSM+S0G/N5
UWd1KtO6D0MiiUDZjPKjhdtJ3bpyiV9sJkEGIa5tSWLv/6zBEj4zjWKsyti/OA8UekuRdknVmNDYMNNCkD
bWtRwR4xUdi2wePPkTdA6EMdWmHq9UwAT5F2oCX9KDHvZ5a6JHZzSnQ9O4kUHyT/9uqgZJx4Y
CRZCFBIdCF9eK9HFmFJ9IOywZqjvKjLtm7RRKYP3DkWlVzPo10FGB6EUbeHjV5LZpmJmPBAhcdJRsJAbT
Z4YYm8SeFcmTTo8Ji07UslhmOapGh6frDUZGRWiznuxpHp2AUcCt6uH2uUxuQxwoQhkzUHE= user@host
```

We will then add this public key to your Anvil account.

## [Step 3 - Adding the public key to your Anvil account](#step-3---adding-the-public-key-to-your-anvil-account)

[Login](https://anvil.works/login) to your Anvil account and open the app you would like to clone to your Ubuntu server.

Open your account settings, from the menu in the top-right of the Anvil Editor.

Open the **SSH Keys** tab, and paste the public key into the SSH public key box.

## [Step 4 - Cloning your Anvil app onto your server](#step-4---cloning-your-anvil-app-onto-your-server)

Now we have our keys set up, we can clone our Anvil app onto our server. Click the **Clone with Git** button in the [Version History dialog](https://anvil.works/docs/version-control). This dialog will give us the command line to check out our app with Git.

If you entered a passphrase when creating your SSH key in step 1, you will be prompted for the passphrase.

Your app will now be cloned to your Linux machine and is ready to use with the [Anvil App Server](https://github.com/anvil-works/anvil-runtime/blob/master/doc/getting-started.md).
