import asyncio


################################################## tiny! ##################################################

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


################################################## await affect ##################################################


async def do_a():
    print("A started")
    await asyncio.sleep(2)
    print("A finished")


async def do_b():
    print("B started")
    await asyncio.sleep(1)
    print("B finished")


async def do_double():
    await do_a()
    await do_b()

asyncio.run(do_double())


################################################## ##################################################
