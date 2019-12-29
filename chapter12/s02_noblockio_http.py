# request -> urllib -> socket
# 通过非阻塞IO实现http请求
import socket
from urllib.parse import urlparse

def get_url(url):
    # 通过socket请求html
    # urlparse Return a 6-tuple: (scheme, netloc, path, params, query, fragment).
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass
    while True:
        try:
            client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path,host).encode('utf8'))
            break
        except OSError as e:
            pass
    url_data = b''
    while True:
        try:
            recv_data = client.recv(1024)
        except BlockingIOError as e:
            continue
        if recv_data:
            url_data += recv_data
        else:
            break
    url_data = url_data.decode('utf8')
    html_data = url_data.split('\r\n\r\n')[1]
    print(html_data)
    # 关掉socket连接
    client.close()

if __name__ == '__main__':
    get_url('http://www.baidu.com/')
