---
title: "segment.client"
url: "/docs/api/segment.client"
doc-id: segment.client
state: Live
date-created: 2026-09-08
---


## `segment.client` Module

#### Functions

[`alias`](#alias) [`group`](#group) [`identify`](#identify) [`page`](#page) [`track`](#track)

## Functions

#### `alias(new_user_id, [previous_id], [options])`

Combines two previously unassociated user identities. (previous_id defaults to the current user)

#### `group(group_id, [traits], [options])`

Identify this user as a member of a group

#### `identify(user_id, [traits], [options])`

Identify a user to associate subsequent actions to a recognisable user ID and traits

#### `page([category], [name], [options])`

Register a virtual page change

#### `track(event, [properties], [options])`

Track an action performed by the current user
