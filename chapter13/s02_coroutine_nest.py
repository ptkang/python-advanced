# 1. run_until_complete
# import asyncio
# loop = asyncio.get_event_loop()
# loop.run_until_complete()
# loop.run_forever()

# 1. loop 会被放到future中，future会被放到loop中
# 2. 取消 future(task)

import asyncio

async def get_html(sleep_times):
    print('Waiting')
    await asyncio.sleep(sleep_times)
    print('done after {}s'.format(sleep_times))

if __name__ == '__main__':
    # 如何取消task
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(3)

    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks(loop)
        for task in all_tasks:
            print('cancel task')
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    # finally:
        # loop.close()

    # 如何在协程里面嵌套协程
    # https://docs.python.org/3.6/library/asyncio-task.html
    import asyncio

    async def compute(x, y):
        print("Compute %s + %s ..." % (x, y))
        await asyncio.sleep(1.0)
        return x + y

    async def print_sum(x, y):
        result = await compute(x, y)
        print("%s + %s = %s" % (x, y, result))

    # loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()

