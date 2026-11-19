import asyncio

async def Task1():
    print("Task 1 is started!!")
    await asyncio.sleep(3)
    print("Task 1 is completed!!")
    return("Task1")

async def Task2():
    print("Task 2 is started!!")
    await asyncio.sleep(2)
    print("Task 2 is completed!!")
    return("Task2")

async def Task3():
    print("Task 3 is started!!")
    await asyncio.sleep(1)
    print("Task 3 is completed!!")  
    return("Task3")

async def main():
    result = await asyncio.gather(
        Task1(),
        Task2(),
        Task3()
    )
    print(result)
asyncio.run(main())