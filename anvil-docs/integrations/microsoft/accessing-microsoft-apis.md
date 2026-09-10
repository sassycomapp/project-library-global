---
title: "Accessing Azure APIs"
url: "/docs/integrations/microsoft/accessing-microsoft-apis"
doc-id: accessing-microsoft-apis
state: Live
date-created: 2026-09-08
---


# [Accessing Microsoft Azure APIs](#accessing-microsoft-azure-apis)

Microsoft provides a huge range of REST APIs to give you machine-readable access to Azure services. The full list at the time of writing is [further down this page](#full-list-of-microsoft-rest-apis).

For documentation on any particular Microsoft Azure REST API, head to [the Microsoft documentation](https://docs.microsoft.com/en-us/rest/api/azure/).

## [Using Microsoft Azure APIs from Anvil](#using-microsoft-azure-apis-from-anvil)

Anvil gives you an OAuth token you can use to access Microsoft APIs from client-side or server-side code.

You need to link Anvil to your Azure account as described in [Connecting Azure to Anvil](linking-azure-and-anvil). It only takes a few minutes.

Once you’ve done that, you can allow users to log in with their Microsoft accounts by calling this function from the client side code:

```python
anvil.microsoft.auth.login()
```

You can get a Microsoft API token for the currently logged-in user by calling [`anvil.microsoft.auth.get_user_access_token()`](/docs/api/anvil.microsoft.auth#get_user_access_token) in client-side or server-side code:

```python
token = anvil.microsoft.auth.get_user_access_token()
```

You can use the [`anvil.http` library](/docs/http-apis/making-http-requests) to make HTTP requests against your chosen API. You can do this from client-side or server-side code. Put your API token in an `Authorization` header, as in the following example:

```python
    import anvil.http

    anvil.microsoft.auth.login()
    token = anvil.microsoft.auth.get_user_access_token()

    me = anvil.http.request(
      'https://graph.microsoft.com/v1.0/me/',
      headers={'Authorization': f'Bearer {token}'},
      json=True,
    )
    self.headline_1.text = f"Hello, {me['displayName']}!"
```

This example uses the [Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview) API, which allows you to access a range of Microsoft 365 application data such as user accounts, calendar events and emails. Here we’ve used it to display the user’s real name in our Anvil app.

## [OAuth Scopes](#oauth-scopes)

Many of the Microsoft Azure REST APIs require you to request particular OAuth scopes to gain access.

OAuth scopes are particular sets of permissions that you request when logging in. The API token becomes associated with those scopes, so once your user has logged in, you can use the token to make any API requests allowed under the scopes you’ve requested.

To set up the scopes you wish to request, go to the Microsoft API Service in the Anvil Editor and select ‘Yes’ under ‘Request extra OAuth Scopes’. You can then enter any number of OAuth scopes in the text box. To request multiple scopes, enter each scope **separated by a space**.

In our example, making a GET request to `https://graph.microsoft.com/v1.0/me/` requires the `User.Read` scope, so we have instructed Anvil to request it.

## [Full list of Microsoft REST APIs](#full-list-of-microsoft-rest-apis)

The full list of [Microsoft Azure REST APIs](https://docs.microsoft.com/en-us/rest/api/azure/) at the time of writing is:

```
Advisor
AKS
Analysis Services
Anomaly Detector
API Management
App Service
Application Gateway
Application Insights
Authorization
Automation
Azure Net
App Files
Azure Resource Graph
Azure Stack Admin
Batch AI
Batch Management
Batch Service
Billing
Blockchain
Blueprints
CDN
Cognitive Services
Cognitive Services - Bing Search
Compute
Consumption
Container Instances
Container Registry
Container Service
Cosmos DB
Cosmos DB Resource Provider
Cost Management
Data Box Edge/Data Box Gateway
Data Catalog
Data Factory
Data Lake Analytics
Data Lake Storage Gen1
Data Migration
Databricks
Deployment Manager
Dev Test Labs
DNS
Event Grid
Event Hubs
Express
Route
Firewall
Front Door Service
Guest Configuration
HDInsight
HDInsight Spark
Intune
IoT Hub
IoT Hub Device Provisioning Service
Key Vault
Lab Services
Load balancer
Log Analytics
Logic Apps
Machine Learning
Managed Services
Maps
Maps Management
MariaDB
Media Services
Migrate
Mixed Reality
Monitor
MySQL
Network Gateway
Network Watcher
Networking Operations
Notification Hubs
Policy Insights
PostgreSQL
Power BI Embedded
Power BI Workspace Collections
Recovery Services
Recovery Services - Backup
Recovery Services - Site Recovery
Red Hat Open
Shift
Redis Cache
Relay
Reserved VM Instances
Resource Health
Resource Management
Scheduler
Search Management
Search Service
Security Center
Serial Console
Service Bus
Service Fabric
Service Map
SignalR Service
SQL Database
SQL VM
Storage Import-Export
Storage Resource Provider
Storage Services
Stor
Simple
Stream Analytics
Time Series Insights
Traffic Manager
Virtual Networks
Virtual WAN
Visual Studio
```

Take a look at the [Microsoft Azure REST API documentation](https://docs.microsoft.com/en-us/rest/api/azure/) for specifics on how to use each one.

## [Next up](#next-up)

You can also use the Microsoft API Service for user authentication and authorization. Read [Microsoft Single Sign-On](microsoft-single-sign-on) to log users in with their global Microsoft accounts or [Connecting Entra ID to Anvil](linking-azure-and-anvil) to restrict access to users within your organization.
