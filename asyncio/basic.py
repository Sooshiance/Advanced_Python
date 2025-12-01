import asyncio


async def say_hello():
    await asyncio.sleep(1)
    print("Hello")


async def main():
    # create_task schedules say_hello immediately
    task = asyncio.create_task(say_hello())

    print("Task created, doing other work...")

    # await pauses until task finishes
    await task
    print("Task finished!")


asyncio.run(main())
