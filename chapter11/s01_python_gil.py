# gil: global interpreter lock: 全局解释锁
# python中一个线程对应C语言中的一个线程，
# gil 使得同一时刻只有一个线程运行在一个CPU上执行字节码,保证了线程是安全的
# 无法将多个线程映射到多个CPU上运行
# gil会根据执行的字节码行数以及时间片释放gil,还会在遇到IO操作时主动释放
#
import dis
def add(a):
    # 1. dosomething1
    # 2. io操作
    # 3. dosomething3
    a += 1
    return a
print(dis.dis(add))

total = 0
def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global  total
    for i in range(1000000):
        total -= 1

import threading
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
