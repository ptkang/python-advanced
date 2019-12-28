# 线程同步-信号量：用于控制进入数量的锁
# 文件，读、写，写一般只是用于一个线程写，读可以允许有多个线程读‘
# 写和其他互斥，读和读不互斥
import threading

class UrlSplider(threading.Thread):
    def __init__(self, url, sem):
        self.url = url
        self.sem = sem
        super().__init__(name=url)
    def run(self) -> None:
        print('UrlSplide {}'.format(self.url))
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self, sem):
        self.sem = sem
        super().__init__(name='UrlProducer')
    def run(self) -> None:
        for i in range(20):
            self.sem.acquire()
            url_splider_thread = UrlSplider('http://www.baidu.com/{}/'.format(i), self.sem)
            url_splider_thread.start()

if __name__ == '__main__':
    semaphore = threading.Semaphore(3)
    url_producer_thread = UrlProducer(semaphore)
    url_producer_thread.start()
    url_producer_thread.join()
