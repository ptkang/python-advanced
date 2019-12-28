# 进程的数据是完全隔离的
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time

def get_html(n):
    time.sleep(n)
    print('sub process{}'.format(n))
    return n

if __name__ == '__main__':
    print('1'*64)
    process = multiprocessing.Process(target=get_html, name='get_html', args=(2,))
    process.start()
    print('process(name={name}, pid={pid}'.format(name=process.name, pid=process.pid))
    process.join()
    print('main process')

    print('2'*64)
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    result = pool.apply_async(get_html, args=(2,))
    pool.close()
    pool.join()
    print('main pool success')

    print('3'*64)

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    #for result_data in pool.imap(get_html,[1, 5, 3]):
    for result_data in pool.imap_unordered(get_html, [1, 5, 3]):
            print('sub process result {}'.format(result_data))
    pool.close()
    pool.join()
    print('main pool imap success')

