# 线程通信：共享变量(线程不安全)
import time
import threading
# 这种导入另一个文件线程对html_sync_list的修改本线程可以看到，
# 但若from chapter11.s03_variable import html_sync_list，另一个线程对html_sync_list的修改本线程会看不到
# 这点请注意
from chapter11 import s03_variable as vaiable
def get_detail_html(name):
    # 抓取文章详情页
    while True:
        url = vaiable.html_sync_list.pop()
        if len(url):
            print('[name]: reptile {url} start'.format(name=name, url=url))
            time.sleep(2)
            print('[name]: reptile {url} stop'.format(name=name, url=url))
        else:
            time.sleep(1)

def get_detail_url(pos, step):
    # 抓取文章列表页
    # pos = 1
    # step = 20
    while True:
        print('[url] reptile {start} ->{end} list start'.format(start=pos, end = pos + step))
        for url_id in range(pos, pos + step + 1):
            vaiable.html_sync_list.append('http://www.projectsedu.com/{id}'.format(id=url_id))
        pos += step
        time.sleep(4)
        print('[url] reptile {start} ->{end} list end'.format(start=pos, end = pos + step))

if __name__ == '__main__':
    start_time = time.time()
    url_thread = threading.Thread(target=get_detail_url, args=(1, 20,))
    url_thread.start()
    for tid in range(5):
        html_thread = threading.Thread(target=get_detail_html, args=('html_thread{}'.format(tid),), name='html_thread{}'.format(tid))
        html_thread.start()
    time.sleep(10)
    print('last time {}'.format(time.time() - start_time))
