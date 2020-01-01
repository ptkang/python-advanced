# async with lock 调用__await__()和__aenter__()魔法函数
# Queue的get()和put()方法前面一定要加await，因其实一个协程
# Lock用于两个协程共同调用一个子协程的情况
# Queue用于两个协程生产者和消费者共同操作同一资源的情形，主要用于限流等场景
import asyncio
from asyncio import Lock, Queue

total = 0
async def add():
    global total
    for i in range(1000000):
        total += 1

async def desc():
    global  total
    for i in range(1000000):
        total -= 1

if __name__ == '__main__':
    # 这个例子说明协程不需要锁任然可以得到正确的结果
    tasks = [add(), desc()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(total)
