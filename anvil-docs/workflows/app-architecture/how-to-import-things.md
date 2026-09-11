---
document: "How to Import Things"
title: "How to Import Things"
url: "/docs/workflows/app-architecture/how-to-import-things"
doc-id: how-to-import-things
state: Live
date-created: 2026-09-08
---


# [How to import things](#how-to-import-things)

Imports can be confusing in Python, especially when you have a mixture of modules and packages. If in doubt, use the autocompleter to help you get it right!

Just type “`from .`”, then see the suggestions.

## [Importing from the same Package](#importing-from-the-same-package)

Imagine you have a Package with two Modules inside it.

This is how you import the Modules from the Package:

```python
# In MyPackage
from . import Foo
from . import Bar
```

This is how you import the Modules from each other:

```python
# In the Module named Bar
from . import Foo
```

Importing variables from the Package is similar:

```python
# In the Module named Bar,
# To import a variable from MyPackage
from . import my_variable
```

To import the Package itself, you must use an extra dot:

```python
# In the Module named Bar
from .. import MyPackage
```

## [Importing from a nested Package](#importing-from-a-nested-package)

Imagine you have a Package containing a Module and a Package, which in turn contains a Module.

This is how you import the Module that’s in the **child Package**:

```python
# In Foo.py
from .MyChildPackage import Bar

# or, to import a variable from inside the Module:
from .MyChildPackage.Bar import my_function
```

This is how you import the Module that’s in the **parent Package**:

```python
# In Bar.py
from .. import Foo

# or, to import a variable from inside the Module:
from ..Foo import my_function
```

If you move a Form, Module or Package, be sure to rewrite its imports and the imports of things that refer to it - the [all-app search function](/docs/editor/keyboard-shortcuts#in-the-form-editor) can help you here.

## [Importing Forms](#importing-forms)

You will often see Forms imported like this:

```python
# From the Package called Form1, import the class called Form1
from ..Form1 import Form1
```

This works because of the way Forms are represented in code: Form1 is a *Package* named `Form1` that contains a *class* named `Form1`. You can use this to create instances of the Form:

```python
from ..Form1 import Form1

my_form_instance = Form1()
alert(my_form_instance)
```

You should not use this approach when importing Modules:

```python
# This is not the correct way to import a Module
from ..Module1 import Module1
```

This will cause an ImportError (unless `Module1` happens to contain a variable named `Module1`).

This is how to import a Module:

```python
from .. import Module1
```
