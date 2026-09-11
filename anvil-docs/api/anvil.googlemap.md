---
document: "anvil.GoogleMap"
title: "anvil.GoogleMap"
url: "/docs/api/anvil.googlemap"
doc-id: anvil.googlemap
state: Live
date-created: 2026-09-08
---


## `anvil.GoogleMap` Module

#### Classes

[`AbstractOverlay`](#AbstractOverlay) [`Animation`](#Animation) [`Circle`](#Circle) [`ControlPosition`](#ControlPosition) [`Data`](#Data) [`FullscreenControlOptions`](#FullscreenControlOptions) [`GeocoderAddressComponent`](#GeocoderAddressComponent) [`GeocoderGeometry`](#GeocoderGeometry) [`GeocoderLocationType`](#GeocoderLocationType) [`GeocoderResult`](#GeocoderResult) [`Icon`](#Icon) [`IconSequence`](#IconSequence) [`InfoWindow`](#InfoWindow) [`LatLng`](#LatLng) [`LatLngBounds`](#LatLngBounds) [`LatLngBoundsLiteral`](#LatLngBoundsLiteral) [`LatLngLiteral`](#LatLngLiteral) [`MapTypeControlOptions`](#MapTypeControlOptions) [`MapTypeControlStyle`](#MapTypeControlStyle) [`MapTypeId`](#MapTypeId) [`Marker`](#Marker) [`MarkerLabel`](#MarkerLabel) [`MotionTrackingControlOptions`](#MotionTrackingControlOptions) [`Point`](#Point) [`Polygon`](#Polygon) [`Polyline`](#Polyline) [`Rectangle`](#Rectangle) [`RotateControlOptions`](#RotateControlOptions) [`ScaleControlOptions`](#ScaleControlOptions) [`Size`](#Size) [`StreetViewControlOptions`](#StreetViewControlOptions) [`StrokePosition`](#StrokePosition) [`Symbol`](#Symbol) [`SymbolPath`](#SymbolPath) [`ZoomControlOptions`](#ZoomControlOptions)

## Classes

### `AbstractOverlay`

Create a new 'AbstractOverlay' object

##### Base class: anvil.Component

#### Constructor

`AbstractOverlay([clickable=], [draggable=], [visible=], [z_index=])`

#### AbstractOverlay Methods

**add_component(map_component) → anvil.Component instance**

Add a map component to this GoogleMap

**add_event_handler(event_name, handler_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**fit_bounds(lat_lng_bounds, [padding])**

Sets the viewport to contain the given bounds. Adds some padding around the bounds by default - set padding to 0 to match the bounds exactly.

**get_bounds() → anvil.GoogleMap.LatLngBounds instance**

Returns the lat/lng bounds of the current viewport.

**pan_by(dx, dy)**

Changes the center of the map by the given distance in pixels.

**pan_to(position)**

Changes the center of the map to the given LatLng position.

**pan_to_bounds(lat_lng_bounds, [padding])**

Pans the map by the minimum amount necessary to contain the given LatLngBounds. Adds some padding around the bounds by default - set padding to 0 to match the bounds exactly.

**remove_event_handler(event_name, [handler_func])**

Remove a specific event handler function for a given event. Calling remove_event_handler with just the event name will remove all the handlers for this event

**set_event_handler(event_name, handler_func)**

Set a function to call when the 'event_name' event happens on this component. Using set_event_handler removes all other handlers. Setting the handler function to None removes all handlers.

#### AbstractOverlay Properties

**clickable** - *boolean*

True if this overlay raises mouse events.

**draggable** - *boolean*

True if this overlay can be dragged.

**parent**

**visible** - *boolean*

True if this overlay should be displayed.

**z_index** - *number*

The z-index compared to other overlays.

#### AbstractOverlay Events

**show()** — When the anvil.GoogleMap.AbstractOverlay is shown on the screen

**hide()** — When the anvil.GoogleMap.AbstractOverlay is removed from the screen

**click(lat_lng)** — when an overlay is clicked. `lat_lng` - The position that was clicked.

**dblclick(lat_lng)** — when an overlay is double clicked. `lat_lng` - The position that was double-clicked.

**drag(lat_lng)** — while the user drags an overlay. `lat_lng` - The position of the cursor.

**dragend(lat_lng)** — when the user stops dragging an overlay. `lat_lng` - The position of the cursor.

**dragstart(lat_lng)** — when the user starts dragging an overlay. `lat_lng` - The position of the cursor.

**mousedown(lat_lng)** — for a mousedown on an overlay. `lat_lng` - The position of the cursor.

**mouseout(lat_lng)** — when the mouse leaves the area of an overlay icon. `lat_lng` - The position of the cursor.

**mouseover(lat_lng)** — when the mouse enters the area of an overlay icon. `lat_lng` - The position of the cursor.

**mouseup(lat_lng)** — for a mouseup on an overlay. `lat_lng` - The position of the cursor.

**rightclick(lat_lng)** — for a right-click on an overlay. `lat_lng` - The position of the cursor.

---

### `Animation`

An object containing pre-defined animations for use with Markers.

#### Constructor

`Animation()`

---

### `Circle`

Create a new 'Circle' object

##### Base class: anvil.GoogleMap.AbstractOverlay

#### Constructor

`Circle([center=], [radius=], [editable=], [stroke_color=], [stroke_opacity=], [stroke_weight=], [stroke_position=], [fill_color=], [fill_opacity=], [clickable=], [draggable=], [visible=], [z_index=])`

#### Circle Methods

**add_event_handler(event_name, handler_func)** / **remove_event_handler(event_name, [handler_func])** / **set_event_handler(event_name, handler_func)**

#### Circle Properties

**center** - *anvil.GoogleMap.LatLng instance*

The center of the Circle.

**editable** - *boolean*

True if this overlay can be edited by the user.

**fill_color** - *string*

The color to draw the overlay outline.

**fill_opacity** - *number*

The opacity of the overlay outline.

**parent**

**radius** - *number*

The radius of the Circle.

**stroke_color** - *string*

The color to draw the overlay outline.

**stroke_opacity** - *number*

The opacity of the overlay outline.

**stroke_position** - *anvil.GoogleMap.StrokePosition*

The stroke position. Defaults to CENTER.

**stroke_weight** - *number*

The weight of the overlay outline

#### Circle Events

**center_changed()** — When the center position of this circle changes, i.e. when it is moved.

**radius_changed()** — When the radius of this circle changes, i.e. when it is resized.

---

### `ControlPosition`

An object containing pre-defined control positions.

#### Constructor

`ControlPosition()`

---

### `Data`

Create a new Data object with the specified options. Not fully implemented.

#### Constructor

`Data()`

#### Instance Methods

**add([feature], geometry=, id=, properties=) → anvil.GoogleMap.Data.Feature instance**

Adds a feature to the collection, and returns the added feature.

**add_geo_json(geo_json, [id_property_name=id]) → list(anvil.GoogleMap.Data.Feature instance)**

Adds GeoJSON features to the collection. Give this method a parsed JSON. The imported features are returned.

**contains(feature) → boolean**

Checks whether the given feature is in the collection.

**get_feature_by_id(id) → anvil.GoogleMap.Data.Feature instance**

Returns the feature with the given ID, if it exists in the collection.

**load_geo_json(url, [id_property_name=id])**

Loads GeoJSON from a URL, and adds the features to the collection.

**override_style(feature, clickable=, cursor=, draggable=, editable=, fillColor=, fillOpacity=, icon=, shape=, strokeColor=, strokeOpacity=, strokeWeight=, title=, visible=, zIndex=)**

Sets the style for all features in the collection. Styles specified on a per-feature basis via override_style() continue to apply.

**remove(feature)**

Removes a feature from the collection.

**revert_style(feature)**

Removes the effect of previous override_style() calls. The style of the given feature reverts to the style specified by set_style().

**to_geo_json() → string**

Exports the features in the collection to a GeoJSON object.

#### Data Attributes

**control_position** - *anvil.GoogleMap.ControlPosition*

The position of the drawing controls on the map.

**controls** - *list(string)*

Describes which drawing modes are available for the user to select, in the order they are displayed. Possible drawing modes are "Point", "LineString" or "Polygon".

**drawing_mode** - *string*

The current drawing mode of the given Data layer. Possible drawing modes are "Point", "LineString" or "Polygon".

**style** - *anvil.GoogleMap.Data.StyleOptions instance*

Style for all features in the collection. May be a styling function or a GoogleMap.Data.StyleOptions object.

---

### `FullscreenControlOptions`

Construct new FullscreenControlOptions with the specified options.

#### Constructor

`FullscreenControlOptions([position=])`

#### FullscreenControlOptions Attributes

**position** - *anvil.GoogleMap.ControlPosition*

Position of the controls.

---

### `GeocoderAddressComponent`

Create a new 'GeocoderAddressComponent' object

#### Constructor

`GeocoderAddressComponent()`

#### GeocoderAddressComponent Attributes

**long_name** - *string* — The full text of the address component

**short_name** - *string* — The abbreviated, short text of the given address component.

**types** - *list(string)* — An array of strings denoting the type of this address component.

---

### `GeocoderGeometry`

Create a new 'GeocoderGeometry' object

#### Constructor

`GeocoderGeometry()`

#### GeocoderGeometry Attributes

**bounds** - *anvil.GoogleMap.LatLngBounds instance* — The precise bounds of this GeocoderResult, if applicable.

**location** - *anvil.GoogleMap.LatLng instance* — The latitude/longitude coordinates of this result.

**location_type** - *anvil.GoogleMap.GeocoderLocationType* — The type of location returned.

**viewport** - *anvil.GoogleMap.LatLngBounds instance* — The bounds of the recommended viewport for displaying this GeocoderResult.

---

### `GeocoderLocationType`

Describes the type of location returned from a geocode.

#### Constructor

`GeocoderLocationType()`

---

### `GeocoderResult`

Create a new 'GeocoderResult' object

#### Constructor

`GeocoderResult()`

#### GeocoderResult Attributes

**address_components** - *list(anvil.GoogleMap.GeocoderAddressComponent instance)* — An array of GeocoderAddressComponents

**formatted_address** - *string* — A string containing the human-readable address of this location.

**geometry** - *anvil.GoogleMap.GeocoderGeometry instance* — A GeocoderGeometry object

**partial_match** - *boolean* — Whether the geocoder did not return an exact match for the original request, though it was able to match part of the requested address.

**place_id** - *string* — The place ID associated with the location. Place IDs uniquely identify a place in the Google Places database and on Google Maps.

**postcode_localities** - *list(string)* — An array of strings denoting all the localities contained in a postal code. This is only present when the result is a postal code that contains multiple localities.

**types** - *list(string)* — An array of strings denoting the type of the returned geocoded element.

---

### `Icon`

Construct an Icon with the specified options.

#### Constructor

`Icon([anchor=], [label_origin=], [origin=], [scaled_size=], [size=], [url=])`

#### Icon Attributes

**anchor** - *anvil.GoogleMap.Point instance* — The position at which to anchor an image in correspondence to the location of the marker on the map. By default, the anchor is located along the center point of the bottom of the image.

**label_origin** - *anvil.GoogleMap.Point instance* — The origin of the label relative to the top-left corner of the icon image, if a label is supplied by the marker. By default, the origin is located in the center point of the image.

**origin** - *anvil.GoogleMap.Point instance* — The position of the image within a sprite, if any. By default, the origin is located at the top left corner of the image (0, 0).

**scaled_size** - *anvil.GoogleMap.Size instance* — The size of the entire image after scaling, if any. Use this property to stretch/shrink an image or a sprite.

**size** - *anvil.GoogleMap.Size instance* — The display size of the sprite or image. When using sprites, you must specify the sprite size. If the size is not provided, it will be set when the image loads.

**url** - *string* — The URL of the image or sprite sheet.

---

### `IconSequence`

Construct a new IconSequence with the specified options.

#### Constructor

`IconSequence([icon=], [fixed_rotation=], [offset=], [repeat=])`

#### IconSequence Attributes

**fixed_rotation** - *boolean* — If true, each icon in the sequence has the same fixed rotation regardless of the angle of the edge on which it lies. Defaults to false.

**icon** - *anvil.GoogleMap.Symbol instance* — The icon to render on the line.

**offset** - *number* — The distance from the start of the line at which an icon is to be rendered.

**repeat** - *string* — The distance between consecutive icons on the line.

---

### `InfoWindow`

Create a new 'InfoWindow' object

##### Base class: anvil.Component

#### Constructor

`InfoWindow([content=], [disable_auto_pan=], [max_width=], [pixel_offset=], [position=], [z_index=])`

#### InfoWindow Methods

**add_event_handler(event_name, handler_func)** / **remove_event_handler(event_name, [handler_func])** / **set_event_handler(event_name, handler_func)**

**close()**

Hide this InfoWindow. The user can also cause this to happen by clicking the close button in the top-right of the popup.

**open(map, [anchor])**

Display this InfoWindow on the specified map. If anchor is specified, the InfoWindow does not need to have its own position property set.

#### InfoWindow Properties

**content** - *anvil.Component instance* — Content to display in the InfoWindow. Can be a string or an Anvil Component

**disable_auto_pan** - *boolean* — Disable auto-pan on open.

**max_width** - *number* — Maximum width of the infowindow, regardless of content's width.

**parent**

**pixel_offset** - *anvil.GoogleMap.Size instance* — The offset, in pixels, of the tip of the info window from the point on the map at whose geographical coordinates the info window is anchored.

**position** - *anvil.GoogleMap.LatLng instance* — The LatLng at which to display this InfoWindow. Not required if this popup is anchored to a component

**z_index** - *number* — All InfoWindows are displayed on the map in order of their zIndex, with higher values displaying in front of InfoWindows with lower values.

#### InfoWindow Events

**show()** / **hide()**

---

### `LatLng`

Create a new LatLng object at the specified latitude and longitude.

#### Constructor

`LatLng(lat, lng)`

#### Instance Methods

**lat() → number** — Returns the latitude in degrees.

**lng() → number** — Returns the longitude in degrees.

---

### `LatLngBounds`

Create a new LatLngBounds object with the specified corners.

#### Constructor

`LatLngBounds(south_west, north_east)`

#### Instance Methods

**contains(point) → boolean** — Returns True if the given lat/lng is in this bounds.

**equals(other) → boolean** — Returns True if this bounds approximately equals the given bounds.

**extend(point)** — Extends this bounds to contain the given point.

**get_center() → anvil.GoogleMap.LatLng instance** — Computes the center of this LatLngBounds

**get_north_east() → anvil.GoogleMap.LatLng instance** — Returns the north-east corner of this bounds.

**get_south_west() → anvil.GoogleMap.LatLng instance** — Returns the south-west corner of this bounds.

**intersects(other) → boolean** — Returns True if this bounds shares any points with the other bounds.

**is_empty() → boolean** — Returns True if the bounds are empty.

**to_json() → string** — Converts to JSON representation.

**to_span() → anvil.GoogleMap.LatLng instance** — Converts the given map bounds to a lat/lng span.

**to_url_value(precision=6) → string** — Returns a string of the form 'lat_lo,lng_lo,lat_hi,lng_hi' for this bounds.

**union(other) → anvil.GoogleMap.LatLngBounds instance** — Extends this bounds to contain the union of this and the given bounds.

---

### `LatLngBoundsLiteral`

Construct a LatLngBoundsLiteral with the specified edges.

#### Constructor

`LatLngBoundsLiteral([north=], [east=], [south=], [west=])`

#### LatLngBoundsLiteral Attributes

**east** - *number* — The longitude of the east edge of the bounds, in degrees.

**north** - *number* — The latitude of the north edge of the bounds, in degrees.

**south** - *number* — The latitude of the south edge of the bounds, in degrees.

**west** - *number* — The longitude of the west edge of the bounds, in degrees.

---

### `LatLngLiteral`

Create a new LatLngLiteral object at the specified latitude and longitude.

#### Constructor

`LatLngLiteral([lat=], [lng=])`

#### LatLngLiteral Attributes

**lat** - *number* — The latitude in degrees.

**lng** - *number* — The longitude in degrees.

---

### `MapTypeControlOptions`

Construct new MapTypeControlOptions with the specified options.

#### Constructor

`MapTypeControlOptions([position=], [style=], [map_type_ids=])`

#### MapTypeControlOptions Attributes

**map_type_ids** - *list(string)* — IDs of map types to show in the control.

**position** - *anvil.GoogleMap.ControlPosition* — Position of the controls.

**style** - *anvil.GoogleMap.MapTypeControlStyle* — Used to select what style of map type control to display.

---

### `MapTypeControlStyle`

An object containing pre-defined control styles.

#### Constructor

`MapTypeControlStyle()`

---

### `MapTypeId`

An object containing pre-defined map types.

#### Constructor

`MapTypeId()`

---

### `Marker`

Create a new 'Marker' object

##### Base class: anvil.GoogleMap.AbstractOverlay

#### Constructor

`Marker([animation=], [position=], [icon=], [label=], [title=], [cursor=], [opacity=], [clickable=], [draggable=], [visible=], [z_index=])`

#### Marker Methods

**add_event_handler(event_name, handler_func)** / **remove_event_handler(event_name, [handler_func])** / **set_event_handler(event_name, handler_func)**

#### Marker Properties

**animation** - *anvil.GoogleMap.Animation* — The animation of this Marker.

**cursor** - *string* — The cursor to display over this Marker.

**icon** - *anvil.GoogleMap.Symbol instance* — The icon to display at the position of this Marker.

**label** - *anvil.GoogleMap.MarkerLabel instance* — The label to display on this Marker.

**opacity** - *number* — The opacity of this Marker.

**parent**

**position** - *anvil.GoogleMap.LatLng instance* — The LatLng position of this Marker

**title** - *string* — The tooltip text for this Marker.

#### Marker Events

**animation_changed()**, **clickable_changed()**, **cursor_changed()**, **draggable_changed()**, **icon_changed()**, **position_changed()**, **shape_changed()**, **title_changed()**, **visible_changed()**, **z_index_changed()**

---

### `MarkerLabel`

Construct a new MarkerLabel with the specified options.

#### Constructor

`MarkerLabel([color=], [font_family=], [font_size=], [font_weight=], [text=])`

#### MarkerLabel Attributes

**color** - *string* — The color of the label text. Default color is black.

**font_family** - *string* — The font family of the label text.

**font_size** - *string* — The font size of the label text.

**font_weight** - *string* — The font weight of the label text.

**text** - *string* — The text to be displayed in the label.

---

### `MotionTrackingControlOptions`

Construct new MotionTrackingControlOptions with the specified options.

#### Constructor

`MotionTrackingControlOptions([position=])`

#### MotionTrackingControlOptions Attributes

**position** - *anvil.GoogleMap.ControlPosition* — Position of the controls.

---

### `Point`

Create a new Point at the specified coordinates.

#### Constructor

`Point(x, y)`

---

### `Polygon`

Create a new 'Polygon' object

##### Base class: anvil.GoogleMap.AbstractOverlay

#### Constructor

`Polygon([path=], [geodesic=], [editable=], [stroke_color=], [stroke_opacity=], [stroke_weight=], [stroke_position=], [fill_color=], [fill_opacity=], [clickable=], [draggable=], [visible=], [z_index=])`

#### Polygon Methods

**add_event_handler(event_name, handler_func)** / **remove_event_handler(event_name, [handler_func])** / **set_event_handler(event_name, handler_func)**

#### Polygon Properties

**editable** - *boolean* — True if this overlay can be edited by the user.

**fill_color** - *string* — The color to draw the overlay outline.

**fill_opacity** - *number* — The opacity of the overlay outline.

**geodesic** - *boolean* — When true, edges of the polygon are interpreted as geodesic and will follow the curvature of the Earth.

**parent**

**path** - *list(anvil.GoogleMap.LatLng instance)* — The ordered sequence of LatLng coordinates of the Polygon.

**stroke_color** - *string* — The color to draw the overlay outline.

**stroke_opacity** - *number* — The opacity of the overlay outline.

**stroke_position** - *anvil.GoogleMap.StrokePosition* — The stroke position. Defaults to CENTER.

**stroke_weight** - *number* — The weight of the overlay outline

---

### `Polyline`

Create a new 'Polyline' object

##### Base class: anvil.GoogleMap.AbstractOverlay

#### Constructor

`Polyline([icons=], [path=], [geodesic=], [editable=], [stroke_color=], [stroke_opacity=], [stroke_weight=], [clickable=], [draggable=], [visible=], [z_index=])`

#### Polyline Methods

**add_event_handler(event_name, handler_func)** / **remove_event_handler(event_name, [handler_func])** / **set_event_handler(event_name, handler_func)**

#### Polyline Properties

**editable** - *boolean* — True if this overlay can be edited by the user.

**geodesic** - *boolean* — When true, edges of the polygon are interpreted as geodesic and will follow the curvature of the Earth.

**icons** — The icons to be rendered along the polyline.

**parent**

**path** - *list(anvil.GoogleMap.LatLng instance)* — The ordered sequence of LatLng coordinates of the Polyline.

**stroke_color** - *string* — The color to draw the overlay outline.

**stroke_opacity** - *number* — The opacity of the overlay outline.

**stroke_weight** - *number* — The weight of the overlay outline

---

### `Rectangle`

Create a new 'Rectangle' object

##### Base class: anvil.GoogleMap.AbstractOverlay

#### Constructor

`Rectangle([bounds=], [editable=], [stroke_color=], [stroke_opacity=], [stroke_weight=], [stroke_position=], [fill_color=], [fill_opacity=], [clickable=], [draggable=], [visible=], [z_index=])`

#### Rectangle Methods

**add_event_handler(event_name, handler_func)** / **remove_event_handler(event_name, [handler_func])** / **set_event_handler(event_name, handler_func)**

#### Rectangle Properties

**bounds** - *anvil.GoogleMap.LatLngBounds instance* — The bounds of the Rectangle.

**editable** - *boolean* — True if this overlay can be edited by the user.

**fill_color** - *string* — The color to draw the overlay outline.

**fill_opacity** - *number* — The opacity of the overlay outline.

**parent**

**stroke_color** - *string* — The color to draw the overlay outline.

**stroke_opacity** - *number* — The opacity of the overlay outline.

**stroke_position** - *anvil.GoogleMap.StrokePosition* — The stroke position. Defaults to CENTER.

**stroke_weight** - *number* — The weight of the overlay outline

#### Rectangle Events

**bounds_changed()** — When the bounds of this rectangle change, i.e. when it is moved or resized.

---

### `RotateControlOptions`

Construct new RotateControlOptions with the specified options.

#### Constructor

`RotateControlOptions([position=])`

#### RotateControlOptions Attributes

**position** - *anvil.GoogleMap.ControlPosition* — Position of the controls.

---

### `ScaleControlOptions`

Construct new ScaleControlOptions with the specified options.

#### Constructor

`ScaleControlOptions([position=])`

#### ScaleControlOptions Attributes

**position** - *anvil.GoogleMap.ControlPosition* — Position of the controls.

---

### `Size`

Create a new Size at the specified coordinates.

#### Constructor

`Size(x, y)`

---

### `StreetViewControlOptions`

Construct new StreetViewControlOptions with the specified options.

#### Constructor

`StreetViewControlOptions([position=])`

#### StreetViewControlOptions Attributes

**position** - *anvil.GoogleMap.ControlPosition* — Position of the controls.

---

### `StrokePosition`

An object containing pre-defined stroke positions for shape outlines.

#### Constructor

`StrokePosition()`

---

### `Symbol`

Construct a Symbol with the specified options.

#### Constructor

`Symbol([anchor=], [fill_color=], [fill_opacity=], [label_origin=], [path=], [rotation=], [scale=], [strokeColor=], [strokeOpacity=], [strokeWeight=])`

#### Symbol Attributes

**anchor** - *anvil.GoogleMap.Point instance* — The position of the symbol relative to the marker or polyline.

**fill_color** - *string* — The fill color of this symbol.

**fill_opacity** - *number* — The fill opacity of this symbol. Defaults to 0.

**label_origin** - *anvil.GoogleMap.Point instance* — The origin of the label relative to the origin of the path, if label is supplied by the marker.

**path** - *anvil.GoogleMap.SymbolPath* — The symbol's path, which is a built-in symbol path, or a custom path expressed using SVG path notation.

**rotation** - *number* — The angle by which to rotate the symbol, expressed clockwise in degrees.

**scale** - *number* — The amount by which the symbol is scaled in size.

**strokecolor** - *string* — The symbol's stroke color.

**strokeopacity** - *number* — The symbol's stroke opacity.

**strokeweight** - *number* — The symbol's stroke weight.

---

### `SymbolPath`

An object containing pre-defined symbol paths for use on maps.

#### Constructor

`SymbolPath()`

---

### `ZoomControlOptions`

Construct new ZoomControlOptions with the specified options.

#### Constructor

`ZoomControlOptions([position=])`

#### ZoomControlOptions Attributes

**position** - *anvil.GoogleMap.ControlPosition* — Position of the controls.
