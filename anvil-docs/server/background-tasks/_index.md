---
title: "Background Tasks"
url: "/docs/server/background-tasks"
---


# [Running tasks in the background](#running-tasks-in-the-background)

Background Tasks allow you to fire off a function to run in the background, leaving your main program to continue executing while the function is running.

In other words, the function is run asynchronously; it does not block the control flow. Check the [Quickstart](background-tasks/quickstart) to get up and running.

For those on the Free Plan or using legacy [Basic Python](../server/python-versions), the maximum run-time for a background task is 30 seconds.

Runtime for background tasks is not limited for those on the [Hobby Plan](https://anvil.works/pricing) and up.

## [Defining and Running](#defining-and-running)

Any function decorated as `@anvil.server.background_task` can be run in the background. For example:

```python
@anvil.server.background_task
def my_task_name(some_args):
    ... # do something
```

To run a Background Task, call

```python
anvil.server.launch_background_task('my_task_name', args...)
```

You can also launch [Scripts](scripts) as background tasks: a Script called `MyScript` can be launched with `anvil.server.launch_background_task("script:MyScript")`.

See [Defining and Running](background-tasks/defining-and-running) for more information.

## [Communicating with Background Tasks](#communicating-with-background-tasks)

When a Background Task is launched, `anvil.server.launch_background_task` returns a Task object that can be used to send data from the Background Task to the main program. You can also get a Background Task’s status and stop it running using the Task object.

See [Communicating Back](background-tasks/communicating-back) for more information.

## [View Background Task status visually](#view-background-task-status-visually)

You can view the status of all your Background Tasks in the [Background Tasks tab](../editor/app-logs#background-tasks) in App Logs.

## [List Background Tasks from code](#list-background-tasks-from-code)

To see all your Background Tasks, call `anvil.server.list_background_tasks()`, which will return a list of `Task` objects.

Running this function from the published version of your app will return only those Background Tasks that were started from the published version, and running from the development version (i.e. by clicking “Run” in the designer) will only return tasks started in that environment. To return all tasks regardless of environment, set the `all_environments` keyword argument to `True`:

```python
anvil.server.list_background_tasks(all_environments=True)
```

This function can only be run from the server side.

## [Scheduled Tasks](#scheduled-tasks)

You can trigger Background Tasks automatically according to a schedule. Users familiar with Cron will find this familiar.

Open the Scheduled Tasks dialog in the Gear Menu to set up your Scheduled Tasks.

See [Scheduled Tasks](scheduled-tasks) for more information.

## [Suppressing the spinner](#suppressing-the-spinner)

To suppress the spinner when launching or communicating with a Background Task, put your code in a `with anvil.server.no_loading_indicator:` block.

```python
  def launch_button_click(self, **event_args):
    with anvil.server.no_loading_indicator:
      self.task = anvil.server.call('launch_task')
```
