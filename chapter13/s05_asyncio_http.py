# asyncio 没有提供http协议的接口, aiohttp是专门做http协议的,可以用来搭建http服务器，也可以做爬虫使用

import asyncio
import socket
from urllib.parse import urlparse
import time
from concurrent.futures import ThreadPoolExecutor

async def get_url(url):
    # 通过socket请求html
    # urlparse Return a 6-tuple: (scheme, netloc, path, params, query, fragment).
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    # 建立socket连接
    reader, writer = await asyncio.open_connection(host, 80)
    writer.write('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))

    lines = []
    async for raw_line in reader:
        line = raw_line.decode('utf8')
        lines.append(line)
    html = ''.join(lines)
    html = html.split('\r\n\r\n')[1]
    # print(html)
    return html

async def completed():
    futures = []
    for i in range(20):
        url = 'http://shop.projectsedu.com/goods/{}/'.format(i)
        future = asyncio.ensure_future(get_url(url))
        futures.append(future)
    for future in asyncio.as_completed(futures):
        html = await future
        print('get future html {} page success'.format(html))


if __name__ == '__main__':
    # 测试asyncio http
    loop = asyncio.get_event_loop()
    print('1'*32)
    start_time = time.time()
    tasks = []
    for i in range(20):
        url = 'http://shop.projectsedu.com/goods/{}/'.format(i)
        tasks.append(get_url(url))
    loop.run_until_complete(asyncio.wait(tasks))
    print('cost time {}'.format(time.time() - start_time))

    # 获取asyncio http的返回值ensure_future
    print('2'*32)
    start_time = time.time()
    futures = []
    for i in range(20):
        url = 'http://shop.projectsedu.com/goods/{}/'.format(i)
        future = asyncio.ensure_future(get_url(url))
        futures.append(future)
    loop.run_until_complete(asyncio.wait(futures))
    for future in futures:
        print(future.result())
    print('cost time {}'.format(time.time() - start_time))

    # 获取asyncio http的返回值 as_completed
    print('3'*32)
    start_time = time.time()
    loop.run_until_complete(completed())
    print('cost time {}'.format(time.time() - start_time))
