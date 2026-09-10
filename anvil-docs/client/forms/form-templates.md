---
title: "Form Templates"
url: "/docs/client/forms/form-templates"
doc-id: form-templates
state: Live
date-created: 2026-09-08
---


# [Form Templates](#form-templates)

Every Form in Anvil inherits from a template class called `<<FormName>Template`. For example, `Form1` inherits from `Form1Template`. This class is defined by an HTML file which represents the UI of your Form. When you build a Form visually in Design view, the Anvil Designer updates this file for you. You can also view and edit this file directly in the [HTML view](/docs/editor/form-editor#html-view) of the Form Editor.

Form templates are of three types:

1.  [Forms that use a Layout](#forms-with-a-layout)
2.  [Forms that use a Container](#forms-with-a-container)
3.  [HTML Forms](#html-forms)

## [Forms with a Layout](#forms-with-a-layout)

When a Form uses a Layout, it inherits from `WithLayout` and behaves like the Layout it uses. In terms of component placement, rather than placing components anywhere on the Form, you place them into slots defined by the Layout.

A Form using a Layout will have a `layout` attribute on its `<anvil-form>` element in HTML view:

```html
<anvil-form layout="form:HomePage">
    ...
</anvil-form>
```

See [Layouts](/docs/client/forms/layouts) for more details on creating and using Layouts.

## [Forms with a container](#forms-with-a-container)

When a Form uses a container, it inherits from a container type that determines how components are placed and arranged. For example, a Form that inherits from a `ColumnPanel` will stack components vertically.

A Form using a container will have a `container` attribute on its `<anvil-form>` element in HTML view:

```html
<anvil-form container="ColumnPanel">
    ...
</anvil-form>
```

### Blank Panel Forms

Blank Panel Forms are the simplest. Their templates inherit from [ColumnPanel](/docs/ui/components/containers#columnpanel). In terms of component placement, they behave exactly like a ColumnPanel.

### RepeatingPanel templates

When you add a [RepeatingPanel](/docs/ui/components/repeating-panel), to a Form, Anvil automatically creates a new Form called `ItemTemplateN`. (where `N` is a number). This Form is repeated once for each element in the RepeatingPanel’s `items` list, and inherits from [ColumnPanel](/docs/ui/components/containers#columnpanel). In terms of component placement, they also behave exactly like a ColumnPanel.

### Data Grid row templates

When you add a [DataGrid](/docs/ui/components/data-grids) to a Form, it contains a RepeatingPanel by default. The Form associated with this RepeatingPanel will be called `RowTemplateN` and inherits from [DataRowPanel](/docs/ui/components/data-grids#the-datarowpanel-component). In terms of component placement, they behave exactly like a DataRowPanel.

## [HTML Forms](#html-forms)

You do not need to know HTML to use Anvil. HTML Forms are useful if you want to combine HTML with Anvil components, or create custom layouts and components from HTML.

When a Form’s top-level element is an HTML element or an `<anvil-component>`, rather than an `<anvil-form>`, it is an HTML Form and inherits from [HtmlComponent](/docs/components/standard-components/html-component). HTML Forms are useful for creating [custom components](/docs/client/customisation/custom-components/html-components) and reusable [layouts](/docs/client/forms/layouts/html-layouts) with HTML. See [Forms as HTML in the Editor](/docs/editor/form-editor#html-view) for more information about editing your Form’s HTML.

Built-in themes come with pre-defined HTML Form layouts. For example, when you create a Minimal Theme app, you get a Form with an app bar at the top and a main content area. The app bar and main content area are defined in the BaseLayout, which is an HTML Form. The BaseLayout contains slots for the app title, app bar actions, and the main content area. This replaces the older theme pattern where the Standard Page Form used an `HtmlTemplate` with its `html` property set to a `standard-page.html` file in Assets.

HTML Forms are the recommended replacement for [Legacy HTMLTemplate Forms](#legacy-htmltemplate-forms).

## [Legacy HTMLTemplate Forms](#legacy-htmltemplate-forms)

While Legacy HTMLTemplate Forms continue to work in existing apps, [HTML Forms](#html-forms) are the recommended way to use HTML in Anvil.

Some older apps and built-in themes use Legacy HTMLTemplate Forms. These Forms inherit from `HtmlTemplate` and have an `html` property that points to an HTML file in Assets, such as `standard-page.html` or a Custom HTML file.

Legacy HTMLTemplate Forms are different from HTML Forms. An HTML Form inherits from HtmlComponent because its top-level template element is ordinary HTML, which can contain both HTML elements and Anvil components. A Legacy HTMLTemplate Form uses an `HtmlTemplate` container whose HTML is defined separately.
