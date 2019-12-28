# 多进程编程
# 耗cpu的操作，用多线程编程无法达到并行的操作
# 多进程：因GIL锁导致多线程无法利用多核的优势，多进程操作可以利用多进程的优势
# 多线程：多io操作，使用多线程的操作
# 进程切换代价要高于线程

# 1. 对于耗费cpu的操作：计算类型的操作，如数学计算，图像处理，机器学习的算法，挖矿等，多进程优于多线程
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import time


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    # 对于耗费CPU的操作，多进程优于多线程
    with ThreadPoolExecutor(3) as exec:
        all_futures = [exec.submit(fib, num) for num in range(25, 35)]
        start_time = time.time()
        for future in as_completed(all_futures):
            print('exe result {}'.format(future.result()))
        print('ThreadPoolExecutor cost time {} seconds'.format(time.time() - start_time))

    with ProcessPoolExecutor(3) as exec:
        all_futures = [exec.submit(fib, num) for num in range(25, 35)]
        start_time = time.time()
        for future in as_completed(all_futures):
            print('exe result {}'.format(future.result()))
        print('ProcessPoolExecutor cost time {} seconds'.format(time.time() - start_time))
    # 对于io操作，多线程优于多进程
    with ThreadPoolExecutor(3) as exec:
        all_futures = [exec.submit(random_sleep, num) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_futures):
            print('exe result {}'.format(future.result()))
        print('ThreadPoolExecutor cost time {} seconds'.format(time.time() - start_time))

    with ProcessPoolExecutor(3) as exec:
        all_futures = [exec.submit(random_sleep, num) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_futures):
            print('exe result {}'.format(future.result()))
        print('ProcessPoolExecutor cost time {} seconds'.format(time.time() - start_time))


