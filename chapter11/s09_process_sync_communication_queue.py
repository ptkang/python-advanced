# 共享全局变量不能用于多进程编程，可以用于多线程（多线程中也必须进行同步）
# 进程间通信：multiprocessing.Queue(不能用于multiprocessing.Pool里面)
#          : Manager().Queue: 用于pool中的进程间通信
#          : Pipe: 只能适用于两个进程间的通信, pipe的性能高于Queue
#          : 共享结构：如Manager.dict等
from multiprocessing import Process, Queue, Pool, Manager, Pipe
# from queue import Queue
import time

def producer(queue):
    queue.put('a')
    print('produce {}'.format('a'))
    time.sleep(2)
    return 'a'

def consumer(queue):
    data = queue.get()
    print('consume {}'.format(data))
    time.sleep(2)
    return data

def pipe_producer(pipe):
    pipe.send('a')
    print('pipe produce {}'.format('a'))
    time.sleep(2)
    return 'a'

def pipe_consumer(pipe):
    data = pipe.recv()
    print('pipe consume {}'.format(data))
    time.sleep(2)
    return data

def add_progress_dict(proc_dict, key, value):
    proc_dict[key] = value

if __name__ == '__main__':
    print('1'*64)
    queue = Queue(10)
    producer(queue)
    consumer(queue)
    # queue.task_done()
    queue.close()

    print('2'*64)
    queue = Queue(10)
    my_producer = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()
    # queue.task_done()
    queue.close()

    print('3'*64)
    # queue = Queue(10)
    queue = Manager().Queue(10)
    pool = Pool(2)
    my_producer_result = pool.apply_async(producer, args=(queue,))
    my_consumer_result = pool.apply_async(consumer, args=(queue,))
    pool.close()
    pool.join()
    print(my_producer_result.get())
    print(my_consumer_result.get())
    #queue.close()

    print('4'*64)
    recv_pipe, send_pipe = Pipe()
    my_producer = Process(target=pipe_producer, args=(send_pipe,))
    my_consumer = Process(target=pipe_consumer, args=(recv_pipe,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()

    print('5'*64)
    progress_dict = Manager().dict()
    first_proc = Process(target=add_progress_dict, args=(progress_dict, 'Bobby1', 22))
    second_proc = Process(target=add_progress_dict, args=(progress_dict, 'Bobby2', 23))
    first_proc.start()
    second_proc.start()
    first_proc.join()
    second_proc.join()
    print(progress_dict)

