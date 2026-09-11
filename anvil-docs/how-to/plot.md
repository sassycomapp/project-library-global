---
document: "Making plots"
title: "Making plots"
url: "/docs/how-to/plot"
doc-id: plot
state: Live
date-created: 2026-09-08
---


# [Making plots in Anvil](#making-plots-in-anvil)

The recommended way to make plots in Anvil is to use Anvil’s [Plot component](/docs/client/components/plots). This uses Anvil’s client-side Python Plotly library, so you can configure and reconfigure the plot dynamically without making a round-trip to the server.

[Plot component documentation](/docs/client/components/plots)

## [Using Other Plotting Libraries](#using-other-plotting-libraries)

Because Anvil code is just Python, it’s simple to use lots of different plotting libraries with Anvil. This page gives instructions for some of the most popular.

There’s also a comprehensive [comparison of the best-known Python plotting libraries](/blog/plotting-in-python) on the Anvil blog.

### Contents

There are three main types of plotting library in Python. We’ll show you how to use each of them:

1.  **The Matplotlib family:** [Matplotlib, Seaborn and Pandas](#seaborn-pandas-and-matplotlib)

2.  **The HTML generators:** [Bokeh, Altair and Pygal](#bokeh-altair-and-pygal)

3.  **The client-side library:** [Plotly](#plotly)

If you want to use `plotly.express` with Anvil, check out our [Plotly Express in Anvil](/docs/how-to/plotly-express) how-to guide.

## [Matplotlib, Seaborn and Pandas](#matplotlib-seaborn-and-pandas)

Matplotlib, Seaborn and Pandas all render plots on the server-side. To display a plot on the client, you can export it as an image in a [Media object](/docs/working-with-files/media).

There’s a simple function to do this – and it’s the same for all three libraries, since Seaborn and Pandas are based on Matplotlib. Instead of calling `plt.show()` to display the plot on your screen, in Anvil you call `anvil.mpl_util.plot_image()` to render it as an image.

That function returns a Media object, so you can return it to the client code and display it in an Image component. You could also offer the image for download (with the [`Link` component](/docs/ui/components/basic#link)), or even add it to a database.

### Full example: Matplotlib

Matplotlib is included in Anvil’s Python 3.10 server environment as part of the [Data Science Base Environment](https://anvil.works/docs/server/custom-packages#data-science).

Here’s the server function that makes our plot:

```python
import anvil.mpl_util

import numpy as np
import matplotlib.pyplot as plt

@anvil.server.callable
def make_plot():
  # Make a nice wiggle
  x = np.arange(0.0, 5.0, 0.02)
  y = np.exp(-x) * np.cos(2*np.pi*x)

  # Plot it in the normal Matplotlib way
  plt.figure(1, figsize=(10,5))
  plt.plot(x, y, 'crimson')

  # Return this plot as a PNG image in a Media object
  return anvil.mpl_util.plot_image()
```

This returns an Anvil [Media object](/docs/working-with-files/media#media-objects).

Here’s the client-side code to display that plot and make it downloadable:

```python
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
    media_obj = anvil.server.call('make_plot')
    self.image_1.source = media_obj
    self.download_link.url = media_obj
```

Click here to open the full source code for that example in your Anvil Editor:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:GLKW46UN63NSCM4G%3dRGSIUVO3NHNTIY743ASFACKM)

Here’s a clone link for the same example using **Seaborn**:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:2YMHJH6HXJKQSZOF%3dF2XC5TIHTCJIPMCNKPM4PDHL)

Here’s a clone link for the same example using **Pandas**:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:A5CPK67IDMIHRYAM%3d2L7QSZDFHIMEHUNCKXBQXGWV)

## [Bokeh, Altair and Pygal](#bokeh-altair-and-pygal)

Bokeh, Altair and Pygal produce HTML or SVG plots that you can display in an IFrame. This gives you dynamic plots in the browser.

You will need an IFrame component to display them in. Here’s a clone link that gives you an IFrame component you can [use as a dependency](/docs/deployment/dependencies):

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:CFRUWSM6PQ6JUUXH%3dSX4SACDSXBB4UOIVEVPWXH55)

These libraries write out their plots as an HTML or SVG file. In Anvil you can turn this file into a [Media object](/docs/working-with-files/media) using `anvil.media.from_file`:

```python
  # Generate a Media object containing the plot
  media_object = anvil.media.from_file('/tmp/altair.html', 'text/html')
```

You can then set the `src` of the IFrame to a “data URL” obtained from the [Media object](/docs/working-with-files/media). See below for a full example.

### Full example: Bokeh

First, we include the IFrame component as a [dependency](/docs/deployment/dependencies). This makes it available in the [Toolbox](/docs/editor/form-editor#toolbox) so we can drag-and-drop it onto our main Form.

Then we add some lines to the Form’s `__init__` method that fetch a [Media object](/docs/working-with-files/media) from the server. The Media object contains the HTML of the plot. We assign its URL to the `url` of the IFrame component:

```python
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
    media_obj = anvil.server.call('make_plot')
    self.i_frame_1.url = media_obj.get_url(True)
```

Here’s the server function that makes the plot and returns it as a [Media object](/docs/working-with-files/media) to the client:

```python
import anvil.server
import anvil.media

import numpy as np
from bokeh.plotting import figure, output_file, show

@anvil.server.callable
def make_plot():
  # Point Bokeh at a file
  output_file("/tmp/bokeh.html")

  # Make a nice wiggle
  x = np.arange(0.0, 5.0, 0.02)
  y = np.exp(-x) * np.cos(2*np.pi*x)

  # Plot it in the usual Bokeh way
  p = figure(width=600, height=300)
  p.line(x, y)

  # Save the plot
  show(p)

  # Return this plot as HTML in a Media object
  return anvil.media.from_file('/tmp/bokeh.html', 'text/html')
```

Here’s a clone link for that example:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:CFRUWSM6PQ6JUUXH%3dSX4SACDSXBB4UOIVEVPWXH55%7c2SLX3DWJ3JX6CG7W%3dTISIRDSQ3YSBWKFOKKVFSIEW)

Here’s a clone link for the same example using **Altair**:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:CFRUWSM6PQ6JUUXH%3dSX4SACDSXBB4UOIVEVPWXH55%7cCGRHCQWKA44IMZI2%3dOSDATSKED6H2EZ5P4U52BSUH)

Here’s a clone link for the same example using **Pygal**:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:CFRUWSM6PQ6JUUXH%3dSX4SACDSXBB4UOIVEVPWXH55%7cFUAWJQ26OTRWNGYJ%3dS5SGMC4N5AEOSQ6WJDQTG2AN)

The Pygal example doesn’t need to write to a file, since Pygal has a `render` method to output an SVG as a bytestring:

```python
  c = pygal.Line(show_dots=False, width=400, height=200)

  # ...

  return anvil.BlobMedia(content=c.render(), content_type='text/html', name='pygal.svg')
```

## [Plotly](#plotly)

Anvil has Plotly’s Graph Objects built into its client-side Python, so you can construct Plotly plots on the client side in the same way you would construct them using Graph Objects locally. Use Anvil’s Plot component to show the plot in your app. For full details, see the [Plot component documentation](/docs/client/components/plots).

Here’s a clone link for that app:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:7ATCWN42A5HBHZNV%3dJ6MZY35JAMIV7VFJMNFVMFB6)

On the client side, it’s simply:

```python
class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
    x, y = anvil.server.call('get_data')
    self.plot_1.data = go.Scatter(x=x, y=y, mode='lines')
```

and the data is fetched from the server using this server function:

```python
import anvil.server
import numpy as np


@anvil.server.callable
def get_data():
  x = np.arange(0.0, 5.0, 0.02)
  y = np.exp(-x) * np.cos(2*np.pi*x)

  return x, y
```
