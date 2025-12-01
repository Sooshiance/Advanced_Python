# Concurrent Python

Here we will discuss about ***`asyncio`***, ***`threading`*** and other concurrent contents in python. Before we dive into this, you must have basic knowledge about some concepts like `coroutines`, `event`, `tasks` & `awaitables`.

## Coroutine

***`Coroutines`*** are the heart of async programming in Python.

- 1. It can be pause and resume execution process.
- 2. Unlike **Subroutines**, ***Coroutines*** can have many entry points for pausing/resuming execution.
- 3. There is no ***specific*** order to run ***Coroutines***.

## Event

1. It’s a scheduler inside your *`Python`* program. 
2. More like a timetable or traffic controller for coroutines.

## Tasks

Wrapper around coroutines for concurrent execution.

## Awaitables

Objects that can be used with **`await`** keyword.

# asyncio

It's used for I/O-bound operations (network requests, file operations, etc.) where waiting for external resources is the bottleneck. We will discus about most important functions & classes of it.

- 1. ***`async`***: Calling an async function doesn’t run it immediately—it returns a coroutine object that must be `awaited` or `scheduled` to run.
- 2. ***`await`***: Suspends execution of the current `coroutine` until the awaited coroutine or task completes.
- 3. ***`create_task()`***: Schedules a coroutine to run concurrently as an `asyncio` Task.

# threading

# concurrent
