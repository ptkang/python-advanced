# request -> urllib -> socket
# 通过IO多路复用select实现http请求
# select(poll, epool) + 回调+事件循环
# 单线程
# 并发性很高
# 回调导致的问题：
#   1. 如果回调函数执行不正常该如何？
#   2. 如果回调函数里面还要嵌套回调怎么办？要嵌套很多层怎么办？
#   3. 如果嵌套了多层，其中某一个环节出错了，会造成什么后果
#   4. 如果有个数据需要被每个回调都处理怎么办？
#   5. 怎么使用当前函数中的局部变量？
#   。。。
# 回调之痛： ==>通过协程解决
#   1. 可读性差
#   2. 共享状态管理困难
#   3. 异常处理困难


import socket
from urllib.parse import urlparse
# import select
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import time

selector = DefaultSelector()
# urls = ['http://www.baidu.com/']
urls = []
stop = False
class Fetcher():
    def connect(self, key):
        selector.unregister(key.fd)
        self.client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(self.path, self.host).encode('utf8'))
        selector.register(key.fd, EVENT_READ, self.readable)

    def readable(self, key):
        recv_data = self.client.recv(1024)
        if recv_data:
            self.url_data += recv_data
        else:
            selector.unregister(key.fd)
            self.url_data = self.url_data.decode('utf8')
            print(self.url_data)
            # html_data = self.url_data.split('\r\n\r\n')[1]
            # print(html_data)
            # 关掉socket连接
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    def get_url(self, url):
        # 通过socket请求html
        # urlparse Return a 6-tuple: (scheme, netloc, path, params, query, fragment).
        self.spider_url = url
        self.url_data = b''
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        if self.path == '':
            self.path = '/'
        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        selector.register(self.client.fileno(),EVENT_WRITE,self.connect)
def loop():
    # 回调+事件循环+select(poll, epool)
    # 事件循环，不停地请求socket状态并调用对应函数
    # 1. select 本身是不支持register模式
    # 2. socket状态变化以后的回调是由程序员完成
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back=key.data
            call_back(key)

if __name__ == '__main__':
    #fetcher = Fetcher()
    start_time = time.time()
    #fetcher.get_url('http://www.baidu.com/')
    for i in range(20):
        url = 'http://shop.projectsedu.com/goods/{}'.format(i)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print('cost time {}'.format(time.time() - start_time))
