# aysncio
# 包含各种特定系统实现的模块化事件循环
# 传输和协议抽象
# 对TCP, UDP, SSL, 子进程，延时调用以及其他的具体支持
# 模仿futures模块但适用于事件循环使用的Future类
# 基于yield from的协议和任务，可以让你用顺序的方式编写并发代码
# 必须使用一个将产生阻塞IO的调用时，有接口可以把这个事件转移到线程池
# 模仿threading模块中的同步原语，可以用在单线程内的协程之间

# 协程编码模式三个要点：事件循环 + 函数回调(驱动生成器) + io多路复用(epoll)
# asyncio 是python 用于解决异步IO编程的一整套方法
# 常见基于asyncio的python外部框架：tornado、gevent、 twisted(scrapy + django channels)
# tornado(实现web服务器）， 可以直接部署，一般使用nginx + tornado 搭配, 但tornado数据库驱动不能简单使用平常的阻塞IO驱动
# django + flask 传统阻塞io的开发模型，本身不提供web服务器，只是实现了简单socket编码的方便我们调试，实际中搭配(uwsgi, gunicorn + nginx) 部署web服务器

# asyncio可以简单的理解为相当于一个协程池

# 一个线程一般只有一个loop

# wait 和 gather的区别:
# gather能够实现wait功能，是wait功能的高级抽象
# gather能够实现对协程的分组，当然能够实现协程的分组取消

import asyncio
import time
from functools import partial

async def get_html(url):
    print('start get url')
    # 同步阻塞的接口不能使用到协程里面的，要使用协程内部的接口
    # time.sleep(2)
    # 下面必须加await
    await asyncio.sleep(2)
    print('end get url')
    return 'bobby'

def callback(url, futrue):
    print(url)
    print('send email to bobby')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # 使用asyncio
    print('1'*32)
    start_time = time.time()
    tasks = [get_html('http://www.imooc.com') for i in range(10)]
    # loop.run_until_complete(get_html('http://www.imooc.com'))
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)

    # 使用asyncio.ensure_future获取协程的返回值
    print('2'*32)
    start_time = time.time()
    get_future = asyncio.ensure_future(get_html('http://www.imooc.com'))
    loop.run_until_complete(get_future)
    print(get_future.result())
    print(time.time() - start_time)

    # 使用loop.create_task获取协程的返回值和使用task.add_done_callback添加任务完成时的回调函数
    print('3'*32)
    start_time = time.time()
    task = loop.create_task(get_html('http://www.imooc.com'))
    task.add_done_callback(partial(callback, 'http://www.imooc.com'))
    loop.run_until_complete(task)
    print(task.result())
    print(time.time() - start_time)

    # 使用gather和wait的区别
    print('4'*32)
    start_time = time.time()
    group1 = [get_html('http://www.imooc.com') for i in range(4)]
    group2 = [get_html('http://projectsedu.com') for i in range(4)]
    # loop.run_until_complete(asyncio.gather(*group1, *group2))
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    # group2.cancel()
    loop.run_until_complete(asyncio.gather(group1, group2))
    print(time.time() - start_time)

