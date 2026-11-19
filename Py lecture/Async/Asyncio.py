import asyncio

async def greet(name):
    print(f"hello {name}")
    await asyncio.sleep(3)
    print("Good Evening!!")

asyncio.run(greet("Atharv"))
    
