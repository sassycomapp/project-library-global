---
title: "Defining and Running"
url: "/docs/server/background-tasks/defining-and-running"
doc-id: defining-and-running
state: Live
date-created: 2026-09-08
---


# [Defining and Running Background Tasks](#defining-and-running-background-tasks)

## [Defining a Background Task](#defining-a-background-task)

To define a Background Task in a Server Module, decorate a function as `@anvil.server.background_task`

```python
# Defining a Background Task
# In a Server Module:

@anvil.server.background_task
def train_my_network(training_iterations):
  """A long-running neural network training process."""
  for i in range(training_iterations):
    do_one_training_iteration()
    # Report progress percent
    anvil.server.task_state['progress'] = int((i+1 / float(training_iterations)) * 100)
```

Background tasks cannot return [Media objects](/docs/working-with-files/media#media-objects) directly, or pass them in `task_state` - you have to store them in [Data Tables](/docs/data-tables) and retrieve them from there.

### Scripts are also Background Tasks

[Scripts](../scripts) in your app can be invoked as Background Tasks. The name of a Script’s Background task is `script:<name>`.

## [Running a Background Task](#running-a-background-task)

Call `anvil.server.launch_background_task('my_task_name', args...)`

-   First argument: name of function to execute, or `script:` followed by the name of a [Script](../scripts)
-   Other arguments: arguments to pass to the function
-   return value: a Task object for this task (see below).

Background Tasks can only be launched from Server Modules and Uplink scripts.

[Scripts](../scripts) can be launched from client code if their permissions are set to allow it.

```python
# Running a Background Task.
# In a Server Module:

@anvil.server.callable
def launch_training_task():
  """Fire off the training task, returning the Task object to the client."""
  task = anvil.server.launch_background_task('train_my_network', 200)
  return task
```
