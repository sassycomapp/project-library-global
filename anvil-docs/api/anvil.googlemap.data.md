---
title: "anvil.GoogleMap.Data"
url: "/docs/api/anvil.googlemap.data"
---


## `anvil.GoogleMap.Data` Module

#### Classes

[`Feature`](#Feature) [`Geometry`](#Geometry) [`GeometryCollection`](#GeometryCollection) [`LinearRing`](#LinearRing) [`LineString`](#LineString) [`MultiLineString`](#MultiLineString) [`MultiPoint`](#MultiPoint) [`MultiPolygon`](#MultiPolygon) [`Point`](#Point) [`Polygon`](#Polygon) [`StyleOptions`](#StyleOptions)

## Classes

### `Feature`

Create a new Feature.

#### Constructor

`Feature([geometry=None], [id=None], [properties=None])`

#### Instance Methods

**to_geo_json() → string**

Exports this feature as a GeoJSON object.

#### Feature Attributes

**geometry** - *anvil.GoogleMap.Data.Geometry instance*

The feature geometry.

**id** - *string*

Feature ID is optional.

---

### `Geometry`

Create a new 'Geometry' object

#### Constructor

`Geometry()`

#### Instance Methods

**get_type() → string**

Returns the type of the geometry object.

---

### `GeometryCollection`

Constructs a Data.GeometryCollection from the given geometry objects or LatLngs.

##### Base class: anvil.GoogleMap.Data.Geometry

#### Constructor

`GeometryCollection(points)`

#### Instance Methods

**get_array() → list(anvil.GoogleMap.Data.Geometry instance)** — Returns an array of the contained Geometries. A new array is returned each time get_array() is called.

**get_at(n) → anvil.GoogleMap.Data.Geometry instance** — Returns the n-th contained Geometry.

**get_length() → number** — Returns the number of contained Geometries.

---

### `LinearRing`

Constructs a Data.LinearRing from the given LatLngs

##### Base class: anvil.GoogleMap.Data.Geometry

#### Constructor

`LinearRing(points)`

#### Instance Methods

**get_array() → list(anvil.GoogleMap.LatLng instance)** / **get_at(n) → anvil.GoogleMap.LatLng instance** / **get_length() → number**

---

### `LineString`

Create a new LineString geometry from the specified points.

##### Base class: anvil.GoogleMap.Data.Geometry

#### Constructor

`LineString(points)`

#### Instance Methods

**get_array() → list(anvil.GoogleMap.LatLng instance)** / **get_at(n) → anvil.GoogleMap.LatLng instance** / **get_length() → number**

---

### `MultiLineString`

Constructs a Data.MultiLineString from the given Data.LineStrings or arrays of positions.

##### Base class: anvil.GoogleMap.Data.Geometry

#### Constructor

`MultiLineString(points)`

#### Instance Methods

**get_array() → list(anvil.GoogleMap.Data.LineString instance)** / **get_at(n) → anvil.GoogleMap.Data.LineString** / **get_length() → number**

---

### `MultiPoint`

Create a new MultiPoint geometry containing the specified points.

##### Base class: anvil.GoogleMap.Data.Geometry

#### Constructor

`MultiPoint(points)`

#### Instance Methods

**get_array() → list(anvil.GoogleMap.LatLng instance)** / **get_at(n) → anvil.GoogleMap.LatLng instance** / **get_length() → number**

---

### `MultiPolygon`

Constructs a Data.MultiPolygon from the given Polygons or arrays of positions.

##### Base class: anvil.GoogleMap.Data.Geometry

#### Constructor

`MultiPolygon(points)`

#### Instance Methods

**get_array() → list(anvil.GoogleMap.Data.Polygon instance)** / **get_at(n) → anvil.GoogleMap.Data.Polygon instance** / **get_length() → number**

---

### `Point`

Create a new Point at the specified position.

##### Base class: anvil.GoogleMap.Data.Geometry

#### Constructor

`Point(lat_lng)`

#### Instance Methods

**get() → anvil.GoogleMap.LatLng instance** — Returns the contained LatLng.

---

### `Polygon`

Constructs a Data.Polygon from the given LinearRings or arrays of positions.

##### Base class: anvil.GoogleMap.Data.Geometry

#### Constructor

`Polygon(points)`

#### Instance Methods

**get_array() → list(anvil.GoogleMap.Data.LinearRing instance)** / **get_at(n) → anvil.GoogleMap.Data.LinearRing instance** / **get_length() → number**

---

### `StyleOptions`

Create a new 'StyleOptions' object

#### Constructor

`StyleOptions([StyleOptions=], [clickable=], [cursor=], [draggable=], [editable=], [fill_color=], [fill_opacity=], [icon=], [stroke_color=], [stroke_opacity=], [stroke_weight=], [title=], [visible=], [z_index=])`

#### StyleOptions Attributes

**clickable** - *boolean* — If true, the marker receives mouse and touch events. Default value is true.

**cursor** - *string* — Mouse cursor to show on hover. Only applies to point geometries.

**draggable** - *boolean* — If true, the object can be dragged across the map and the underlying feature will have its geometry updated.

**editable** - *boolean* — If true, the object can be edited by dragging control points and the underlying feature will have its geometry updated.

**fill_color** - *string* — The fill color.

**fill_opacity** - *number* — The fill opacity between 0.0 and 1.0.

**icon** - *anvil.GoogleMap.Symbol instance* — Icon for the foreground.

**stroke_color** - *string* — The stroke color.

**stroke_opacity** - *number* — The stroke opacity between 0.0 and 1.0.

**stroke_weight** - *number* — The stroke width in pixels.

**title** - *string* — Rollover text.

**visible** - *boolean* — Whether the feature is visible.

**z_index** - *number* — All features are displayed on the map in order of their zIndex, with higher values displaying in front of features with lower values.
