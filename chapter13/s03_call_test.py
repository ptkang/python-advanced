# loop里面调用函数call_soon, call_soon_threadsafe, call_at, call_later
import asyncio

def callback(sleep_times, loop):
    print('[{}]:sleep {} success'.format(loop.time(), sleep_times))

def loop_stop(loop):
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(2, callback, 2, loop)
    loop.call_later(1, callback, 1, loop)
    loop.call_later(3, callback, 3, loop)
    loop.call_soon(callback, 2, loop)
    now = loop.time()
    loop.call_at(now + 2, callback, 4, loop)
    loop.call_at(now + 1, callback, 5, loop)
    loop.call_at(now + 3, callback, 6, loop)

    # loop.call_soon(loop_stop, loop)
    loop.run_forever()
