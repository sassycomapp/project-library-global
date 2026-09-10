---
title: "Installing Packages"
url: "/docs/server/custom-packages"
doc-id: custom-packages-_index
state: Live
date-created: 2026-09-08
---


# [Custom Python packages](#custom-python-packages)

To import a third-party package into your app’s Server Modules, you need to install it into that app’s server environment. Packages in Anvil are installed on a per-app basis, meaning that you can add only the necessary packages for each app.

## [Available Python versions](#available-python-versions)

Anvil provides multiple options for server environments. You can select one from the **Python version** drop-down menu in your app’s Settings.

-   **Python 3.10** is the default Anvil server environment. This version lets you install custom packages into your app’s server environment.
-   **Basic Python 3** includes only the Python Standard library.
-   **Legacy Full Python 3** and **Full Python 2** are legacy server environments with [many packages already installed](/docs/server/python-versions/packages).

### Basic Python 3

Basic Python is a [PyPy Sandbox](https://doc.pypy.org/en/latest/sandbox.html) - this is a Python 3.6 interpreter with extra security features that allow us to provide the server environment for free to everybody.

### Legacy Full Python

The Legacy Full Python server environment is an ordinary CPython interpreter - the standard version of Python that you probably have on your own machine. This is available on all paid tiers.

For each app, you can choose between Python 3.7 or Python 2.7 for your Server Modules. These environments have a number of packages already installed. For a full list, see [here](/docs/server/python-versions/packages).

## [Available base environments](#available-base-environments)

There are currently 4 Base Environments available. Choose a Base Environment that best suits your needs, to minimise the number of custom packages you will have to install yourself. For example, if you need the `pandas` package, we recommend starting from the **Standard** Base Environment, which already includes this package. If you also need `tensorflow`, choose the **Machine Learning** Base Environment.

#### Minimal

This is a lightweight environment, containing only the necessary packages to run Anvil server code (such as, for example, [ws4py](https://ws4py.readthedocs.io/en/latest/)).

#### Standard

This image contains everything from the Minimal environment, along with the following packages and all their dependencies:

-   [numpy](https://pypi.org/project/numpy/)
-   [pandas](https://pypi.org/project/pandas/)
-   [pytest](https://pypi.org/project/pytest/)
-   [requests](https://pypi.org/project/requests/)

#### Data Science

This image contains everything from the Standard environment, along with the following packages and all their dependencies:

-   [matplotlib](https://pypi.org/project/matplotlib/)
-   [scipy](https://pypi.org/project/scipy/)
-   [sympy](https://pypi.org/project/sympy/)
-   [jupyter](https://pypi.org/project/jupyter/)

#### Machine Learning

This image contains everything from the Data Science environment, along with the following packages and all their dependencies:

-   [tensorflow](https://pypi.org/project/tensorflow)
-   [torch (PyTorch)](https://pypi.org/project/torch)
-   [scikit-learn](https://pypi.org/project/scikit-learn)
-   [keras](https://pypi.org/project/keras)
-   [h5py](https://pypi.org/project/h5py)

## [Adding packages](#adding-packages)

Packages can be added to your app’s server environment by entering a package name (as it appears in [PyPI](https://pypi.org/)) in the left-hand box underneath the ‘Package’ section of the Python version settings. For each package, a version can be specified in the right-hand box, or left blank to use the latest version.

After adding packages to your app, you can interact with them in the [Server Console](/docs/debugger/additional-debugging-tools#server-console).

To install packages from somewhere other than PyPI, see [Advanced Options](#advanced-options).

## [Build output](#build-output)

Once you add custom packages to the list, Anvil will install those packages to create a new server environment.

Underneath the ‘Package’ installation section is a collapsible section which details the output of this process.

### Possible errors

Anvil presents the output from pip’s install process directly. The two most common causes of build failures happen when a requested package could not be found, and when there is a conflict in dependency versions.

#### Package does not exist

```python
ERROR: Could not find a version that satisfies the requirement `bad-package` (from versions: none)
ERROR: No matching distribution found for `bad-package`
Error: Build failed
```

This typically happens due to a typo. Double-check that the package you have requested is spelled correctly, and that the requested version (if any) is correct.

#### Conflicting dependencies

```python
ERROR: Cannot install pymongo==4.1.0 and pymongo==4.1.1 because these package versions have conflicting dependencies.
ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
Error: Build failed
```

This happens when the dependencies you have requested have incompatible requirements. For help resolving this, visit [pip’s dependency conflict management page](https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts).

## [Checking for Vulnerabilities](#checking-for-vulnerabilities)

Once a server environment has been built, Anvil will use [pip-audit](https://pypi.org/project/pip-audit/) to check the installed dependencies of that environment for vulnerabilities. The output of this can be seen below the Build Output section.

If security vulnerabilities are detected, a button will appear, linking a report of which packages are affected.

## [Advanced options](#advanced-options)

### Editing your app’s `requirements.txt` directly

Anvil’s package management uses pip, so packages can be installed from PyPI, a GitHub repository, or a URL using pip’s [Requirements File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/). Your app’s `requirements.txt` file can also be edited directly, by clicking the link at the lower left of the Package section.

This will open up a text editor in which you can type your package list directly, just as you would into a `requirements.txt` file. This allows you to specify more nuance in your version dependencies, such as using the `<=` operator.

### Running bash scripts

You can add pre-install or post-install bash scripts to run in your app’s server environment by clicking the ‘advanced settings…’ and adding the scripts in the relevant field.
