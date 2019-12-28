# 线程通信：Queue(消息队列）
import time
import threading
from queue import Queue

def get_detail_html(msg_queue, name):
    # 抓取文章详情页
    while True:
        try:
            url = msg_queue.get(timeout=2)
            print('[name]: reptile {url} start'.format(name=name, url=url))
            time.sleep(1)
            print('[name]: reptile {url} stop'.format(name=name, url=url))
        except Exception as e:
            print("[name]: TimeOut".format(name = name), e)
            break
    print('[name] thread finished'.format(name=name))

def get_detail_url(msg_queue, pos, step, max_list_count):
    # 抓取文章列表页
    # pos = 1
    # step = 20
    while True:
        if pos >= max_list_count:
            break
        print('[url] reptile {start} ->{end} list start'.format(start=pos, end = pos + step))
        for url_id in range(pos, pos + step + 1):
            msg_queue.put('http://www.projectsedu.com/{id}'.format(id=url_id))
        print('[url] reptile {start} ->{end} list end'.format(start=pos, end = pos + step))
        pos += step
        # time.sleep(4)
    print('[url] thread finished')

if __name__ == '__main__':
    msg_queue = Queue(20)
    html_thread_list = []
    start_time = time.time()
    url_thread = threading.Thread(target=get_detail_url, args=(msg_queue, 1, 20, 100))
    url_thread.start()
    for tid in range(5):
        html_thread = threading.Thread(target=get_detail_html, args=(msg_queue, 'html_thread{}'.format(tid),), name='html_thread{}'.format(tid))
        html_thread.start()
        html_thread_list.append(html_thread)

    for html_thread in html_thread_list:
        print('join thread:{name} start'.format(html_thread.name))
        html_thread.join()
        print('join thread:{name} end'.format(html_thread.name))
    print('join url thread start')
    url_thread.join()
    print('join url thread end')
    msg_queue.task_done()
    print('join msg_queue start')
    msg_queue.join()
    print('join msg_queue end')
    print('last time {}'.format(time.time() - start_time))
