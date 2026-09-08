---
title: "Plots"
url: "/docs/components/standard-components/plots"
---


# [Plots](#plots)

[Properties](/docs/api/anvil#Plot_attributes) | [Events](/docs/api/anvil#Plot_events)

The Plot component is a Plotly Plot. Drag and drop onto your Form, or create one in code with the `Plot` constructor.

Plots are interactive - move the mouse over a plot to see the available tools.

```python
# Create a plot

b = Plot()
```

## [Configuring plots](#configuring-plots)

Plots are configured using utility classes from the `plotly.graph_objects` module. Display a plot by setting the `data` and `layout` properties of the Plot component, and style it using the `template` property.

### `data` property

The `data` property should be set to a list of traces as [described in the Plotly documentation](https://plot.ly/python/reference/).

```python
from plotly import graph_objects as go

# Plot some data
self.plot_1.data = [
  go.Scatter(
    x = [1, 2, 3],
    y = [3, 1, 6],
    marker = dict(
      color= 'rgb(16, 32, 77)'
    )
  ),
  go.Bar(
    x = [1, 2, 3],
    y = [3, 1, 6],
    name = 'Bar Chart Example'
  )
]
```

### `layout` property

The `layout` property should be set to a dictionary describing the layout of the plot. You can also set layout properties as attributes, such as `self.plot_1.layout.yaxis.title = 'carbon emissions'`.

```python
# Configure the plot layout
self.plot_1.layout = {
  'title': {'text': 'Simple Example'},
  'xaxis': {
    'title': {'text': 'Time'}
  }
}
self.plot_1.layout.yaxis.title.text = 'Carbon Emissions'
self.plot_1.layout.annotations = [{
  'text': 'Simple annotation',
  'x': 1,
  'xref': 'x',
  'y': 3.2,
  'yref': 'y'
}]
```

### `template` property

The `templates` property allows you to set your app’s plot styling. You can set it to one of the [pre-set Plotly templates](https://plotly.com/python/templates/) or one of Anvil’s. Anvil’s defined templates correspond with the Material 3 colour schemes: `material_light`, `material_dark` `rally_light`, `rally_dark`, `mykonos_light`, `mykonos_dark`, `manarola_light` and `manarola_dark`.

By default, Plotly plots created on the server have a default template of `plotly` whereas plots created on the client have no default template. You can make your client plots match your server plots by adding `Plot.templates.default = "plotly"` to your client-side code.

The available pre-set Plotly templates defined by Plotly are: `plotly`, `plotly_white`, `plotly_dark`, `presentation`, `ggplot2`, `seaborn`, `simple_white`, `gridon`, `xgridoff`, and `ygridoff`.

```python
# Setting the app's default plot styling

Plot.templates.default = "material_light"
```

Templates can also be set for each individual plot, rather than the whole app:

```python
# Setting an individual plot's template

self.plot_1.layout.template = "material_light"
```

You can also save your own custom template, as long as it’s written in object form:

```python
Plot.templates["my_template"] = {"layout": {"plot_bgcolor": "bisque"}}

Plot.templates.default = "my_template"
```

If you are using plotly on the server to build plots, you can set your plot’s template by importing `plotly_templates`.

```python
from anvil import plotly_templates

plotly_templates.set_default("rally")
```

## [Handling events](#handling-events)

You can handle events raised when the user clicks, selects or hovers over data points. The `click`, `select`, `hover` and `unhover` events all provide a `points` keyword argument. This is a list of dictionaries, each with the following keys:

-   `curve_number` - the index of the data series that was clicked.
-   `point_number` - the index of the data point that was clicked. Not available for histograms.
-   `point_numbers` - a list of indices of the points aggregated into the clicked bin. Only available for histograms.
-   `x`, `y`, `z`, `lat`, `lon` - the position of the point that was clicked, depending on the plot type.

For example, to print the x and y coordinates when a user hovers over a data point:

```python
def plot_1_hover(self, points, **event_args):
  """This method is called when a data point is hovered."""
  print(f"User hovered over x:{points[0]['x']} and y:{points[0]['y']}")
```

See [the Plotly documentation](https://plot.ly/python/) for more details and examples.

## [Default interactivity](#default-interactivity)

Plots are interactive by default: the user can zoom in on sections, save images, or open the data in the new tab via the Plotly toolbar in the corner of the plot.

If you don’t want this interactivity, you can create a static plot by setting the Plot component’s `interactive` property to `False`.

## [Other plotting libraries](#other-plotting-libraries)

You can use other plotting libraries with Anvil. Many libraries such as Alatair, Bokeh and Pygal produce dynamic plots that work fully interactively in Anvil.

For more detail, see the How-to Guide on [Making Plots in Anvil](/docs/how-to/plot).
