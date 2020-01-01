# 使用多线程：协程里面不能加入阻塞IO，但需要集成阻塞IO时可以使用多线程

import asyncio
import socket
from urllib.parse import urlparse
import time
from concurrent.futures import ThreadPoolExecutor

def get_url(url):
    # 通过socket请求html
    # urlparse Return a 6-tuple: (scheme, netloc, path, params, query, fragment).
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    #不停的询问连接是否建立好， 需要while循环不停的去检查状态
    #做计算任务或者再次发起其他的连接请求
    client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
    url_data = b''
    while True:
        recv_data = client.recv(1024)
        if recv_data:
            url_data += recv_data
        else:
            break
    url_data = url_data.decode('utf8')
    # print(url_data)
    html_data = url_data.split('\r\n\r\n')[1]
    print(html_data)
    # 关掉socket连接
    client.close()

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(3)
    tasks = []
    for i in range(20):
        url = 'http://shop.projectsedu.com/goods/{}/'.format(i)
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print('cost time {}'.format(time.time() - start_time))
