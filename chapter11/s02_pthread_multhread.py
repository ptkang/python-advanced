# 对于IO操作来说，多线程和多进程性能差别不大
# 1. 通过Thread类实例化
# 2. 通过继承Thread类来实现多线程

import time
import threading
def get_detail_html(url):
    print('get detail html started')
    time.sleep(2)
    print('get detail html end')

def get_detail_url(url):
    print('get detail url started')
    time.sleep(4)
    print('get detail url end')

class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        return super().__init__(name=name)
    def run(self) -> None:
        print(self.name + 'get detail html started')
        time.sleep(2)
        print(self.name + 'get detail html end')

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        return super().__init__(name=name)
    def run(self) -> None:
        print(self.name + 'get detail url started')
        time.sleep(2)
        print(self.name + 'get detail url end')


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=('',))
    thread2 = threading.Thread(target=get_detail_url, args=('',))

    # The entire Python program exits when no alive non-daemon threads are left
    # 使得当主线程退出的时候子线程被直接kill掉
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    start_time = time.time()
    thread1.start()
    thread2.start()
    # 等待线程退出
    thread1.join()
    thread2.join()
    print('last time {}'.format(time.time() - start_time))

    print('2'*32)
    thread3 = GetDetailHtml('[Html Thread]')
    thread4 = GetDetailUrl('[Url Thread]')
    start_time = time.time()
    thread3.start()
    thread4.start()
    thread3.join()
    thread4.join()
    print('last time {}'.format(time.time() - start_time))

