import asyncio


async def first_function():
    print("First function is running...")
    await asyncio.sleep(5)  # non-blocking delay simulation
    print("First function is done...")
    return 5


async def second_function():
    print("Second function is running...")
    await asyncio.sleep(5)
    print("Second function is done...")
    return 10


async def main():
    task1 = asyncio.create_task(first_function())
    task2 = asyncio.create_task(second_function())

    x = await task1
    y = await task2

    print(x)
    print(y)


if __name__ == "__main__":
    asyncio.run(main())

'''
Output:
First function is running...
Second function is running...
First function is done...
Second function is done...
5
10
'''