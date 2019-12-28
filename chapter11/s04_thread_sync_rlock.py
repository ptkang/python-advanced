# 线程同步-锁: Lock(不可重入锁), RLock(同一个线程可重入锁)
# 锁的问题-死锁：
#   1. 重复性死锁：
#       Lock, RLock: 加锁和释放锁的次数不对等 => 代码错误，必须修正
#       Lock：重复加锁(包括函数调用导致的嵌套加锁) => 可通过使用RLock来解决
#   2. 竞争性死锁：加锁或释放锁的顺序不相同 ==> 必须按序对称加锁和释放锁
# Lock：非重复性加锁，加锁后必须释放锁才可以再次加锁
# RLock: 同一个线程里面，可以连续多次加锁，但一定注意是同一个线程，且加锁的次数要和释放锁的次数严格对等

import threading
from threading import Lock, RLock

total = 0
# lock = Lock()
lock = RLock()
def do_something():
    global total
    global lock
    lock.acquire()
    print('do something to total={}'.format(total))
    lock.release()

def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        do_something()
        lock.release()

def desc():
    global  total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
