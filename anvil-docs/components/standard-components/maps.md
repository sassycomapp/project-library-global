---
document: "Maps"
title: "Maps"
url: "/docs/components/standard-components/maps"
doc-id: maps
state: Live
date-created: 2026-09-08
---


# [Google Maps](#google-maps)

You can display interactive Google Maps on your Anvil Form with the GoogleMap component. Drag and drop onto your Form, or create one in code with the `GoogleMap` constructor.

```python
map = GoogleMap()

map.center = GoogleMap.LatLng(52.2053, 0.1218)
map.zoom = 13
```

## [Markers and other overlays](#markers-and-other-overlays)

GoogleMap components are containers. You can add various Map Overlay components to a map. In this example, we add a marker at a particular position and with a ‘drop’ animation.

```python
marker = GoogleMap.Marker(
  animation=GoogleMap.Animation.DROP,
  position=GoogleMap.LatLng(52.2053, 0.1218)
)

map.add_component(marker)
```

### Customising markers

You can customise Markers using their `icon` property. This can be set to a [`GoogleMap.Symbol`](https://anvil.works/docs/api/anvil.googlemap#Symbol) or [`GoogleMap.Icon`](https://anvil.works/docs/api/anvil.googlemap#Icon) object:

-   `GoogleMap.Symbol` objects are used to [display particular shapes rather than icons](#data-visualisation).

-   `GoogleMap.Icon` objects are used to draw custom icons, which can be constructed with the URL of the image to display:

```python
green_icon = GoogleMap.Icon(
      url="http://maps.google.com/mapfiles/kml/paddle/grn-blank.png"
    )

marker = GoogleMap.Marker(
  animation=GoogleMap.Animation.DROP,
  position=GoogleMap.LatLng(52.2053, 0.1218),
  icon = green_icon
)

map.add_component(marker)
```

You can find all sorts of useful icon images [here](http://kml4earth.appspot.com/icons.html).

### Overlays and mouse events

Markers (and other overlays) can respond to mouse events. In the code snippet below, we display an `InfoWindow` anchored to the marker when the marker is clicked.

`InfoWindows` have a `content` property, which can be set to a string or an Anvil Component such as a [Label](basic#label) or an entire Form - in this case we use a Label saying “This is Cambridge!”.

```python
def marker_click(sender, **event_args):
  i =GoogleMap.InfoWindow(content=Label(text="This is Cambridge!"))
  i.open(map, sender)

marker.add_event_handler("click", marker_click)
```

### Drawing lines

To draw a line between positions on a map, add a `GoogleMap.Polyline` component to the map. In this example, we also add an arrow icon.

```python
  p = GoogleMap.Polyline(
    path=[
      GoogleMap.LatLng(52.215, 0.14),
      GoogleMap.LatLng(52.195, 0.12),
      GoogleMap.LatLng(52.21, 0.10),
    ],
    stroke_color='blue',
    stroke_weight=2,
    icons=[
      GoogleMap.IconSequence(
        icon=GoogleMap.Symbol(
          path=GoogleMap.SymbolPath.FORWARD_OPEN_ARROW,
          scale=2
        )
      )
    ]
  )
```

### Complete list of overlay components

Here is a complete list of the available map overlay components, and their most important properties and methods. See the [API Docs](/docs/api/anvil.googlemap) for complete lists of properties and events.

Each property is listed in the format **`property_name`:** `argument_type`

#### `GoogleMap.Marker`

Mark a particular point on the map. Draws a red pin by default.

**Properties**

-   **`animation`:** `GoogleMap.Animation` - Specifies the animation of this marker. Set to `GoogleMap.Animation.DROP`, or `GoogleMap.Animation.BOUNCE`.

-   **`icon`:** can be either of the following:
    -   `GoogleMap.Symbol` - Specifies the shape to display. If unset, a red pin is displayed.
    -   `GoogleMap.Icon` - Specifies a custom icon, constructed using the `url` property.

-   **`label`:** `GoogleMap.MarkerLabel | String` - Describes the text label of this marker.

-   **`position`:** `GoogleMap.LatLng` - Specifies the position of this marker.

[Learn more about Markers in the Google Maps documentation](https://developers.google.com/maps/documentation/javascript/reference#Marker)

#### `GoogleMap.InfoWindow`

Display a popup on the map at a particular position.

**Properties**

-   **`position`:** `GoogleMap.LatLng` - Specifies the position of the popup. Not required if this popup is anchored to a component (see the `open` method, below).
-   **`content`:** `anvil.Component | string` - The content of the popup. Can be a string, or an Anvil Component.

**Methods**

-   **`open(map, [anchor])`** - Display this InfoWindow on the specified map. If `anchor` is specified, the InfoWindow does not need to have its own `position` property set.
-   **`close()`** - Hide this InfoWindow. The user can also cause this to happen by clicking the close button in the top-right of the popup.

[Learn more about InfoWindows in the Google Maps documentation](https://developers.google.com/maps/documentation/javascript/reference#InfoWindow)

#### `GoogleMap.Polyline`

Draw a line on the map.

**Properties**

-   **`icons`:** `list of GoogleMap.IconSequence` - Specifies the icons to display along this line.
-   **`path`:** `list of GoogleMap.LatLng` - A list of points along the line.
-   **`geodesic`:** `boolean` - Whether this line should follow the curvature of the Earth. Default `False`.

[Learn more about Polylines in the Google Maps documentation](https://developers.google.com/maps/documentation/javascript/reference#Polyline)

#### `GoogleMap.Polygon`

Draw a closed polygon on the map.

**Properties**

-   **`path`:** `list of GoogleMap.LatLng` - A list of vertices.
-   **`geodesic`:** `boolean` - Whether the outline of this polygon should follow the curvature of the Earth. Default `False`.

[Learn more about Polygons in the Google Maps documentation](https://developers.google.com/maps/documentation/javascript/reference#Polygon)

#### `GoogleMap.Rectangle`

Draw a rectangle on the map.

**Properties**

-   **`bounds`:** `GoogleMap.LatLngBounds` - Specifies the position and size of this rectangle.

[Learn more about Rectangles in the Google Maps documentation](https://developers.google.com/maps/documentation/javascript/reference#Rectangle)

#### `GoogleMap.Circle`

Draw a circle on the map.

**Properties**

-   **`center`:** `GoogleMap.LatLng` - The position of the circle.
-   **`radius`:** `number` - The radius of the circle, in meters.

[Learn more about Circles in the Google Maps documentation](https://developers.google.com/maps/documentation/javascript/reference#Circle)

In addition to the properties specified above, all overlays have `clickable`, `draggable`, and `visible` properties. Overlays with outlines also have `editable`, `stroke_color`, `stroke_weight` and `stroke_opacity` properties.

Those with area have `fill_color` and `fill_opacity` properties.

See [the official Google Maps documentation](https://developers.google.com/maps/documentation/javascript/reference#MarkerOptions) for more details.

## [Data visualisation](#data-visualisation)

It is possible to use [the Data Layer](https://developers.google.com/maps/documentation/javascript/datalayer) to visualise location-based data instead of Overlays. In this example, we add point features to the `map_data` object, then set a rendering styles for all features at once.

```python
map.map_data.add(GoogleMap.Data.Feature(
  geometry=GoogleMap.Data.Point(
    GoogleMap.LatLng(52.2,0.1))))

map.map_data.add(GoogleMap.Data.Feature(
  geometry=GoogleMap.Data.Point(
    GoogleMap.LatLng(52.21,0.12))))

map.map_data.add(GoogleMap.Data.Feature(
  geometry=GoogleMap.Data.Point(
    GoogleMap.LatLng(52.201,0.135))))

map.map_data.style = GoogleMap.Data.StyleOptions(
  icon=GoogleMap.Symbol(
    path=GoogleMap.SymbolPath.CIRCLE,
    scale=30,
    fill_color='red',
    fill_opacity=0.3,
    stroke_opacity=1,
    stroke_weight=1
  )
)
```

We could also generate feature styles dynamically by assigning a ‘styling function’ to the `map_data.style` property. The function will be called once for every feature, and should return a corresponding style. In this example, we choose the color of the circle based on the longitude of the feature.

```python
def get_style(feature):
  point = feature.geometry.get()
  color = 'red' if point.lng() < 0.12 else 'blue'

  return GoogleMap.Data.StyleOptions(
    icon=GoogleMap.Symbol(
      path=GoogleMap.SymbolPath.CIRCLE,
      scale=30,
      fill_color=color,
      fill_opacity=0.3,
      stroke_opacity=1,
      stroke_weight=1
    )
  )

map.map_data.style = get_style
```

### Feature geometries

There are many tools available to define shapes on the map. In the example above, we were interested in points, so we used `GoogleMap.Data.Point`. There are several others available, listed below.

See [the official Google Maps documentation](https://developers.google.com/maps/documentation/javascript/reference#Data.Geometry) for more information.

#### `GoogleMap.Data.Point(lat_lng)`

Features are respresented by a particular position.

#### `GoogleMap.Data.MultiPoint([lat_lng_1, lat_lng_2, ...])`

Features are respresented by a set of positions.

#### `GoogleMap.Data.LineString([lat_lng_1, lat_lng_2, ...])`

Features are respresented by a line with specified vertices.

#### `GoogleMap.Data.MultiLineString([line_string_1, line_string_2, ...])`

Features are respresented by a multiple LineString geometries.

#### `GoogleMap.Data.LinearRing([lat_lng_1, lat_lng_2, ...])`

Features are respresented by a closed loop of vertices.

#### `GoogleMap.Data.Polygon([linear_ring_1, linear_ring_2, ...])`

Features are respresented by a set of closed loops. Additional loops denote ‘holes’ in the polygon.

#### `GoogleMap.Data.MultiPolygon([polygon_1, polygon_2, ...])`

Features are respresented by multiple polygons.

#### `GoogleMap.Data.GeometryCollection([geometry_1, geometry_2, ...])`

Features are respresented by an arbitrary set of geometries defined above.

## [Address lookup (geocoding)](#address-lookup-geocoding)

You can look up addresses from locations, and vice-versa, using the `GoogleMap.geocode` function. This function returns a `GoogleMap.GeocoderResult` array. In this example, we look up a location from an address, then display a marker.

```python
results = GoogleMap.geocode(address="Cambridge, UK")

m = Marker(position=results[0].geometry.location)
map.add_component(m)
```

In this example, we look up an address for a given lat/long.

```python
results = GoogleMap.geocode(
  location=GoogleMap.LatLng(52.2053, 0.1218)
)

print(results[0].formatted_address)
```

There are several other properties available on the `GoogleMap.GeocoderResult` object. See [the official Google documentation](https://developers.google.com/maps/documentation/javascript/reference#GeocoderResult) for details.

If you want to do geocoding in Server Modules, you can use the `geopy` library ([learn how to install it in your server environment here](https://anvil.works/docs/server/custom-packages)). Here’s a simple server function that does a reverse geocode lookup using a free API:

```python
from geopy.geocoders import ArcGIS

@anvil.server.callable
def geocode(lat, lng):
  geolocator = ArcGIS()
  location = geolocator.reverse((lat, lng))
  print(location.address)
```

### Geocoding API quota

A shared Google Maps API key is provided to allow easy testing of your geocoding code. This is shared between all Anvil users for free, so the request quota may run out. This can cause your request to produce an error like this:

```
ExternalError: Geocode failed: REQUEST_DENIED
```

To use your own API key, [obtain an API key for your app](https://developers.google.com/maps/documentation/javascript/get-api-key), add the [Google API Service](/docs/integrations/google/quickstart) to your app, then enter your API key in the Maps API Key box.

## [Calculating length and area](#calculating-length-and-area)

The GoogleMap Component provides utilities for calculating length and area:

#### `GoogleMap.compute_length([pos_1, pos_2, ...])`

Returns the length of the line going through the specified points.

#### `GoogleMap.compute_area([vertex_1, vertex_2, ...])`

Returns the area of the polygon with the specified vertices.

```python
# Calculate the length of the line.
GoogleMap.compute_length([
  GoogleMap.LatLng(52.215, 0.14),
  GoogleMap.LatLng(52.195, 0.12),
  GoogleMap.LatLng(52.21, 0.10),
])

# Calculate the area of the polygon.
GoogleMap.compute_area([
  GoogleMap.LatLng(52.215, 0.14),
  GoogleMap.LatLng(52.195, 0.12),
  GoogleMap.LatLng(52.21, 0.10),
])
```

## [Google Maps in production](#google-maps-in-production)

To use Google Maps in production with a [custom domain](/docs/deployment/choosing-urls#using-your-own-domain-name), you should [obtain an API key for your app](https://developers.google.com/maps/documentation/javascript/get-api-key).

To add this API key to your app, add the [Google API Service](/docs/integrations/google), then expand the ‘Maps API Key’ section.
