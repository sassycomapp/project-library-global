---
title: "Python Directory Structure"
url: "/docs/workflows/app-architecture/python-directory-structure"
---


# [Python directory structure](#python-directory-structure)

Your app is stored as a directory structure that you can [clone using Git](/docs/version-control). Each Package, Module and Form consists of files and directories within this structure.

### Packages

Packages (and Server Packages) are Python packages - directories containing an `__init__.py` file:

```
Package1
└── __init__.py
```

### Forms

Each Form is also a Python package: the `__init__.py` contains what you see in the Code View for that Form. There’s also an html file that describes the UI design for the Form, named `form_template.html`:

```
Form1
├── __init__.py
└── form_template.html
```

### Modules

Modules (and Server Modules) are simply ordinary files; a Module named `Module1` is a Python file named `Module1.py`.

```
Package1
├── __init__.py
└── Module1.py
```

## [Server vs. Client](#server-vs-client)

Server-side and client-side code are stored in separate directories in the repo. When you check out your app using Git, you’ll see directories named `server_code` and `client_code`:

```
MyApp
├── __init__.py
├── anvil.yaml
├── client_code
├── server_code
└── theme
```

## [Example](#example)

Here’s an example of the structure of an app in Anvil, and the underlying directory structure in the Git repo. The Anvil representation is this:

Its repo has the following directory structure:

```
MachineInventory
├── __init__.py
├── anvil.yaml
├── client_code
│   ├── DataProcessor.py
│   ├── Machines
│   │   ├── Detail
│   │   │   ├── __init__.py
│   │   │   └── form_template.html
│   │   ├── List
│   │   │   ├── ItemTemplate1
│   │   │   │   ├── __init__.py
│   │   │   │   └── form_template.html
│   │   │   ├── __init__.py
│   │   │   └── form_template.html
│   │   └── __init__.py
│   └── Navigation
│       ├── __init__.py
│       └── form_template.html
├── server_code
│   ├── Exporters
│   │   ├── Excel.py
│   │   ├── GoogleDrive.py
│   │   └── __init__.py
│   └── Importers
│       ├── Excel.py
│       ├── GoogleDrive.py
│       └── __init__.py
└── theme
    ├── assets
    │   ├── standard-page.html
    │   └── theme.css
    ├── parameters.yaml
    └── templates.yaml
```
