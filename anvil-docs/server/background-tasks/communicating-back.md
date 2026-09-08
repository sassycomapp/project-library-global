---
title: "Communicating with Background Tasks"
url: "/docs/server/background-tasks/communicating-back"
---


# [Communicating with Background Tasks](#communicating-with-background-tasks)

Each instance of a Background Task is associated with a Task object that can be used to get the task’s current status, and any data the task has passed to the main program.

The Task object can also be used to control the running of the task. Background tasks run in a separate session from the code that launched them, so the Task object is the only way to communicate with a task.

## [Communicating back to the main program](#communicating-back-to-the-main-program)

You can use `anvil.server.task_state` to share data with the main program from within the task. The main program gets a Task object as the return value of `anvil.server.launch_background_task()`. This object has a `get_state()` method that returns the `task_state`.

By default, `anvil.server.task_state` is an empty `dict`, so you can immediately set key/value pairs: `anvil.server.task_state['progress'] = 42`. You can store any [portable type](/docs/server/server-modules#valid-arguments-and-return-values) in the `task_state`, except for Media objects. If you want to share Media objects with the main program, store them in a Data Table and retrieve them from there instead.

The Task can also raise exceptions; the main program can access these using the `is_completed` and `get_error` methods of the Task object.

```python
@anvil.server.callable
def launch_my_task():
  task = anvil.server.launch_background_task('train_my_network', 200)

  # Output some state from the task
  print(task.get_state()['false_positive_rate'])

  # Is the task complete yet?
  if task.is_completed():
    return

  # Store the ID of the task so we can see it later
  app_tables.tasks.add_row(
    when=datetime.now(),
    task_id=task.get_id(),
  )

  # If the task raised an exception, re-raise it here
  task.get_error()

  # Otherwise, kill the task
  task.kill()

  # Check the termination status
  if task.get_termination_status() == "killed":
    print("Yes, the task was killed!")

  # Finally, return the task to the client
  return task
```

## [Task object](#task-object)

The Task object reports on task status and gives you control over the task. There are three ways to get the Task object for a particular task:

-   When launching a task. It is the return value of `anvil.server.launch_background_task()`.
-   Later on, using `anvil.server.get_background_task(task_id)`. You need to know the `task_id`, which you can get using `task.get_id()`. You may wish to store this ID in a Data Table or elsewhere.
-   Using `anvil.server.list_background_tasks()`. (See [Listing Background Tasks from code](/docs/background-tasks#list-background-tasks-from-code))

The Task object’s methods are:

-   `get_state()`: returns an object that you can modify from within the task (by modifying `anvil.server.task_state` inside the task).
-   `get_id()`: returns the ID of a task, which is a string.
-   `get_task_name()`: returns the name of the task. Usually the name of the function decorated with `anvil.server.background_task`.
-   `get_start_time()`: returns a `DateTime` representing the time this task was started.
-   `get_return_value()`: returns the return value of the task, or `None` if the task has not yet returned.
-   `get_error()`: re-throws whatever exception caused the task to terminate.
-   `kill()`: stops the task and makes its status `"killed"` rather than `"failed"`. This can only be executed on the server side.
-   `get_termination_status()` returns:
    -   `None` if the task is still running
    -   `"completed"` if the task completed successfully
    -   `"failed"` if the task terminated with an exception
    -   `"killed"` if the task was explicitly killed with `task.kill()`, or by clicking “Kill” in the development environment
    -   `"missing"` if an Uplink disconnection or infrastructure failure caused us to lose track of the task.
-   `is_running()`: returns `True` if the task is still running. Otherwise returns `False`, regardless of how the task ended (completed, killed, failed or missing).
-   `is_completed()`: returns `True` if the task completed successfully, `False` if the task is still running. If the task has failed or been killed, it raises whatever caused the task to terminate.

## [Finding the ID of the current task](#finding-the-id-of-the-current-task)

A running background task can discover its own ID from the [call context object](/docs/api/anvil.server#CallContext), as `anvil.server.context.background_task_id`.

## [Output from Background Tasks](#output-from-background-tasks)

When you call `print()` in a Background Task, the output is visible in the App Logs. When you launch a Background Task while running an app in the Anvil Editor, its output will be displayed live in the [App Console](../../editor#bottom-panel).

## [Advanced](#advanced)

### Timeouts

For those on the Free Plan or using [Basic Python](/docs/server/python-versions), the maximum run-time for a background task is 30 seconds.

Runtime for background tasks is not limited for those on the [Hobby Plan](https://anvil.works/pricing) and up.

### Separation of processes

Background Tasks are run in a separate Python process to your server functions. This means that they’ll never share global variables or `anvil.server.session` with your server calls. (They also do not share implicit session information, such as any user logged in via the [Users Service](/docs/users).)

The reason we run Background Tasks in a separate process is to do with timeouts: If a server call takes too long, we need to kill it rather than letting it spin forever. Background tasks, however, can run for a long time. If we ran them in the same Python interpreter as your standard server functions, we would have to kill your background tasks whenever a server call timed out.

If the Task needs access to information from `anvil.server.session`, then it is the caller’s responsibility to furnish it, via additional parameters passed to `anvil.server.launch_background_task()`.

The `anvil.server.session` object is not [portable](/docs/server#valid-arguments-and-return-values) across server calls. If you need to share session data with a background task, pass only the arguments you need to pass.

### Task object methods

The data in `anvil.server.task_state` is specific to the task - that is, a background task’s own `anvil.server.task_state` is read/write within the Task, and read-only everywhere else, including in the code of other Tasks.

### Tasks on the Uplink

When a background task is defined on the [Uplink](/docs/uplink), it will execute in its own thread on the Uplink, just like a server call, and `anvil.server.task_state` will be a thread-local variable.

If an Uplink is disconnected from Anvil, we lose track of any background tasks running on that uplink. The termination status for those tasks will be `"missing"` or `"failed"`.
