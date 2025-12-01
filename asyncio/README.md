# Explanation

Here I will create some example of how use `asyncio` important features.

## basic.py

We create a task in background using `create_task` and than `wait` until gets done.

***`create_task()`***: It takes a coroutine and schedules it on the event loop to run soon, but not immediately.

    > Schedules it on the running event loop

    > Starts it immediately (as soon as the loop cycles)

    > Returns a Task object

    > Does NOT block the current coroutine
