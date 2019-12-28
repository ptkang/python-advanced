# 线程池和进程池：futures
# futures 专门用来做线程池和进程池编程的
# futures使用场景或功能：
#   1. 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
#   2. 当一个线程完成的时候，我们主线程能够立即知道
#   3. futures可以让多线程和多进程编码接口一致
# future.done() 判断一个线程的完成状态
# future.cancel() 在一个线程开始前取消线程的运行，注意：线程已经开始，运行或完成后，该线程无法取消
# future.result() 等待线程完成，并获取其返回值
# Future: 未来对象，task的返回容器

import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future

def get_html(seconds):
    time.sleep(seconds)
    print('get html {} page'.format(seconds))
    return seconds

if __name__ == '__main__':
    exec = ThreadPoolExecutor(2)
    print('1'*64)
    future1 = exec.submit(get_html, 4)
    future2 = exec.submit(get_html, 2)
    future3 = exec.submit(get_html, 1)
    future4 = exec.submit(get_html, 6)
    print('submit all finished')
    print(future1.done())
    print(future3.cancel())
    print(future1.result())

    # 通过as_completed获取已经完成的线程并返回,谁先完成就处理谁
    print('2'*64)
    html_lists = [4, 2, 1, 6]
    all_futures = [ exec.submit(get_html, seconds) for seconds in html_lists ]
    wait(all_futures, return_when=FIRST_COMPLETED)
    print('main')
    for future in as_completed(all_futures):
        print('get future html {} page success'.format(future.result()))

    # 通过exec获取已经完成的线程并返回，按html_list的顺序返回
    print('3'*64)
    for future_result in exec.map(get_html, html_lists):
        print('get future html {} page success'.format(future_result))



