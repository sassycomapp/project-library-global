---
title: "Dealing with Timezones"
url: "/docs/workflows/dealing-with-timezones"
doc-id: dealing-with-timezones
state: Live
date-created: 2026-09-08
---


# [Dealing with timezones](#dealing-with-timezones)

### Datetime object timezones

Anvil ‘stamps’ `datetime.datetime` objects with timezones as they pass across interfaces. This creates a timezone-aware `datetime` object, so you don’t lose track of what timezone a `datetime` object was created in:

-   Any timezone-aware `datetime` object retains its timezone when transferred in any direction between client, server and Data Tables.
-   Any naïve `datetime` object that is transferred between client and server gets automatically ‘stamped’ with the timezone of the place where it was created before it is transferred. This means that `datetime` objects generated on the client are automatically ‘stamped’ with the timezone of the browser, while those generated on the server are ‘stamped’ with the timezone of the server, which is always guaranteed to be UTC.

These simple rules mean that you can always compare `datetime` objects, no matter where they were created and no matter how much you’ve moved them around or stored them in data tables.

You can explicitly create timezone-aware `datetime` objects if you wish, using helper classes from the [`anvil.tz`](/docs/api/anvil.tz) module:

```python
import anvil.tz

naive_local = datetime.now()
# 2019-08-09 10:10:00.406000
aware_local = datetime.now(anvil.tz.tzlocal())
# 'stamped' with the timezone of the browser
# 2019-08-09 10:10:00.418000+01:00

naive_utc = datetime.utcnow()
# 2019-08-09 09:10:00.426000
aware_utc = datetime.now(anvil.tz.tzutc()) # note: NOT datetime.utcnow()
# 'stamped' with the UTC timezone (timezone of the server)
# 2019-08-09 09:10:00.433000+00:00

aware_custom = datetime(2017,11,16,23,45,15,0, anvil.tz.tzoffset(hours=3))
# 'stamped' with the UTC+3 timezone
# 2017-11-16 23:45:15+03:00
```
