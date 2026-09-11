---
document: "FAQ"
title: "FAQ"
url: "/docs/overview/faq"
doc-id: faq
state: Live
date-created: 2026-09-08
---

# [FAQ](#faq)

Find quick answers to common questions about building apps with Anvil.

If you can’t find an answer to your question here or anywhere else on our website, ask on our [Community Forum](https://anvil.works/forum).

## [Getting Started](#getting-started)

---

### What can I build with Anvil?

Anvil lets you build a wide range of full-stack web applications using only Python, with no JavaScript, HTML, or CSS required.

People use Anvil to build:

-   SaaS products
-   Minimum Viable Products (MVPs)
-   Machine learning applications
-   Web Portals
-   eCommerce and retail websites
-   Dashboards
-   Data Analytics tools
-   Progressive web apps
-   Mobile apps

For inspiration, check out our [case studies](../../case-studies) and [examples page](../../learn/examples). You can also browse the [Show and Tell forum](https://anvil.works/forum/c/show-and-tell/) to see what the community has been building or share your own projects.

---

### How do I start learning Anvil?

The best place to begin is our [Get Started guide](../get-started). From there, you can explore:

-   [Tutorials](../../learn/tutorials)
-   [Reference Docs](../overview)
-   [Community Forum](https://anvil.works/forum)

For community-created projects, demos, blogs, and tutorials, check out the [Awesome Anvil page](https://github.com/anvil-works/awesome-anvil).

---

### Do I need to know Python or web development before using Anvil?

No prior web development knowledge is needed. Anvil lets you build full-stack web apps with just Python, without needing to learn JavaScript, HTML, or CSS.

If you are new to Python or web development, our [Get Started guide](../get-started) has resources to get you up and running regardless of your background.

If you’d like to understand the basics of how web apps work, we also recommend MDN’s guide on [How the Web Works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works).

---

## Building Apps with Anvil

---

### Which browsers does Anvil support?

Anvil apps support all major browsers currently receiving updates, including Chrome, Firefox, Safari, and other Chromium-based browsers on both desktop and mobile.

The Anvil Editor supports up-to-date desktop versions of Chrome and Firefox.

---

### What’s the difference between server side and client side code?

In an Anvil app, code runs in two places:

-   **[Client](../client)**: runs in the user’s browser and handles the interface and user interactions.
-   **[Server](../server)**: runs in a secure cloud environment and handles business logic and sensitive operations.

Learn more about client-server architecture [here](../../articles/client-vs-server).

---

### Does Python really run in the browser? How does that work?

Yes – the Python you write in client-side Anvil Forms is compiled to JavaScript using the open-source framework [Skulpt](https://skulpt.org/).

For a deeper dive into how this works, check out our blog post on [Python in the browser](../../blog/python-in-the-browser-talk).

---

### Do Anvil apps work on mobile?

Yes, Anvil apps are responsive by default and work well on phones and tablets.

Anvil apps are also [Progressive Web Apps](../server/offline-apps#installing-anvil-apps), so they can be installed on Android, iPhone, or ChromeBook and work offline.

---

### Can I use JavaScript with Anvil?

You do not need to know JavaScript to use Anvil.

However, if you want to integrate with a low-level browser API or an existing JavaScript library, see our documentation on [Using JavaScript](../client/customisation/javascript).

---

### Can I use Python packages in my Anvil app?

Yes – you can install Python packages in your app’s **server code**. See [Adding packages](../server/custom-packages#adding-packages).

However, not all Python packages are available in **client code**. If you run an app that imports a package that isn’t available in the client, you may see an error like:

`NotImplementedImportError: logging is not yet implemented in Skulpt`

To learn more, see our documentation on [The Client-side Python Environment](../client/client-code/the-python-environment).

---

### Can I build APIs with Anvil?

Yes, Anvil lets you build HTTP APIs for your apps.

To get started, read our [HTTP APIs documentation](../external-resources/http-apis) or follow our [HTTP APIs tutorial](../../learn/tutorials/http-apis-in-python).

---

### Can I use Anvil with my own IDE or text editor?

Yes, you can use your IDE of choice with the [**Anvil CLI**](/docs/using-another-ide#using-anvil-from-a-local-ide).

Anvil’s IDE is web-based and includes many built-in features you’ll find in popular IDEs, but if you prefer working locally, the **Anvil CLI** lets you use your favourite editor and sync changes bidirectionally with the Anvil Editor. Check out the [CLI docs](/docs/using-another-ide#using-anvil-from-a-local-ide) to get started.

---

### Does Anvil support version control?

Yes, Anvil has built-in version control.

Every Anvil app is a Git repository, so you can:

-   [Push it to external Git repositories like GitHub](/docs/workflows/version-control/git).
-   [Clone it to your local machine](/docs/workflows/version-control/git/direct-checkout) and edit it there with any text editor or IDE.
-   Use a local IDE alongside the Anvil Editor with the live-syncing [Anvil CLI](../using-another-ide#using-anvil-from-a-local-ide).

---

## Hosting & Deployment

---

### Can I host my Anvil app on my own server?

Of course you can!

The Anvil framework is [open source](https://anvil.works/open-source), and you can self-host your apps anywhere using the [open-source Anvil App Server](https://github.com/anvil-works/anvil-runtime). See our [deployment guides](../how-to/app-server/cloud-deployment-guides) for hosting on popular cloud services.

---

### Where are Anvil’s servers located?

Anvil’s infrastructure is hosted in London (AWS eu-west-2).

If you require a specific location, the [Enterprise Plan](../plans-and-accounts/enterprise) gives you private Anvil infrastructure hosted wherever you want, in a public cloud, private cloud or on-site.

If you want to develop in the cloud but deploy on-site, you can also use our [open-source app server](https://github.com/anvil-works/anvil-runtime).

---

### What are Anvil’s server IPs?

If you’re on a [paid plan](../../pricing) and need a list of our egress IP addresses, please get in touch via [contact@anvil.works](mailto:contact@anvil.works).

We will reply with the current list of IPs and update you if they change.

---

### My custom domain shows an SSL certificate error. What do I do?

This is expected when setting up a custom domain. SSL provisioning can take up to **24-48 hours**. During this time, your browser may show a privacy error stating that the connection is not secure.

If the error persists after 48 hours, contact us at [support@anvil.works](mailto:support@anvil.works).

For more information, see our [Custom Domains documentation](../deployment/custom-domains).

---

### How do I fix the error message: `anvil.server.RuntimeUnavailableError: Server resources not available for 'python3-full'`?

Full Python 3 is now our legacy environment, and we recommend using the [Python 3.10 environment](../server/custom-packages) instead, which lets you install any package you like.

This error can be caused by a delay in activating a paid plan or 7-day trial for the legacy Full Python environment.

![Server code dropdown in the Anvil Editor](../server/img/custom-packages/python-310.png)

Switch to Python 3.10 in the Editor for instant activation.

---

## Security & Privacy

---

### Who owns my app?

You own your app and all of its content, even if you cancel your Anvil account.

For full details, see our [Terms of Service](../../terms-of-service).

---

### Does Anvil have a bug bounty program?

We take security very seriously, but we do not currently run a bug bounty program.

If you’ve found a security issue, report it to [security@anvil.works](mailto:security@anvil.works).

---

## Plans, Support & Community

---

### How many apps can I build?

You can build an unlimited number of apps with your Anvil account, even on the Free Plan.

---

### Where can I get a quote for an Enterprise plan?

For a quote on our [Enterprise Plan](../plans-and-accounts/enterprise), contact us at [sales@anvil.works](mailto:sales@anvil.works).

---

### How do I sign up for Production?

Moving your account to Production involves transferring your data to your new isolated database. Contact us at [sales@anvil.works](mailto:sales@anvil.works) to activate your new plan and schedule the changeover.

---

### Can I use Anvil for teaching or education?

Yes – Anvil is free for classroom use and is widely used by lecturers and students to teach and learn Python and web development.

For more details and how to apply, see our [education page](../../for/education).

---

### Does Anvil offer training, consulting or contractors?

The best place to find contractors and consultants is on the [Anvil Jobs Board](https://anvil.works/forum/c/job-adverts).

We don’t offer consulting or from-scratch training, but we do offer a development support as part of the [Production plan](../plans-and-accounts/free-vs-paid#production-plan) or [Anvil Enterprise](../plans-and-accounts/enterprise) which guarantees a 24-working-hour response to your development questions. Contact us at [support@anvil.works](mailto:support@anvil.works) to find out more.

---

### Can I make money as an Anvil developer?

Yes, many developers use Anvil professionally.

You can find contractor and job opportunities on our [jobs board](https://anvil.works/forum/c/job-adverts).

---

### I am a content creator. Will Anvil sponsor my work?

We are happy to explore high-quality sponsored content. If you are interested in working with us, get in touch at [contact@anvil.works](mailto:contact@anvil.works).

---

### How do I give feedback or request a feature?

We’d love to hear from you. Share your feedback on our [Community Forum](https://anvil.works/forum).

To request a feature, post in the [Feature Requests category](https://anvil.works/forum/c/feature-requests). We prioritise requests that get the most community interest.

If you’re on the [Production plan](../plans-and-accounts/free-vs-paid#production), you can also send feature requests directly to [support@anvil.works](mailto:support@anvil.works).
