---
title: "Roles"
url: "/docs/client/customisation/using-css/roles"
doc-id: roles
state: Live
date-created: 2026-09-08
---


# [Roles](#roles)

Roles work by applying [CSS classes](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Type_Class_and_ID_Selectors#class_selectors) to components. For example, a component with a role named `foo` will get the `.anvil-role-foo` CSS class applied to it.

If you’re new to CSS, we have an [introductory guide](https://anvil.works/articles/using-css), which explains how to use it to change the appearance of web pages.

## [Creating Roles](#creating-roles)

You can add new roles by clicking “Theme” in the [Sidebar Menu](/docs/editor#sidebar-menu), then choosing “Roles”. This will bring up the Roles Editor in a new tab.

To add a new role, click on “+ Add a new role” button and choose a name for the role. Then, press enter.

Once added, you can change the roles name, restrict which component types a role can be added to (e.g. you can limit a role to only be available to Image Components) and delete the role entirely.

## [Setting a component’s role](#setting-a-components-role)

When you set a component’s role property, Anvil will give the component a CSS class. The class name will be the Role name with the prefix `anvil-role-`. For example, a `Role` named `"submit"`, would have the class name of `.anvil-role-submit`.

### Setting a component’s role in the design view

To set the role of a component, select the desired component in the [Form Editor](https://anvil.works/docs/editor) and go to the Properties Panel. Scroll down in the Properties Panel to the `appearance` section and click on the `role` dropdown. This will display the list of available roles the component has.

Components can have multiple roles. To enable it for a selected component, use the toggle at the side of the `role` dropdown in the Properties Panel.

### Setting a component’s role in code

You can set the role of a component in code. In the [Form Editor](https://anvil.works/docs/editor), open the Code view and set the `role` property of your component to the desired role.

```python
# Setting the role of a component in client-code
self.button_1.role = "submit"
```

If you want to add multiple roles to one component via code, add them as a list of strings:

```python
# Setting multiple roles for a component in client-code
self.button_1.role = ["submit", "outlined"]
```

## [Changing the component’s style in CSS](#changing-the-components-style-in-css)

You can write [CSS rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Syntax#css_rulesets) in a CSS file uploaded under Assets to define how Roles affect components. In the [Material Design](https://anvil.works/learn/tutorials/using-material-design) theme, `theme.css` is the default CSS file that you can write CSS in.

For example, to select the `anvil-role-submit` class and change the background color, the font color and the font size you could write something like:

```python
.anvil-role-submit {
  background-color: lightblue;
  color: white;
  font-size: 22px;
}
```
