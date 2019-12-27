import socket
import threading

def handle_sock(sock, addr):
    while True:
        # 获取从客户端发送的数据
        # 一次获取1K的数据
        recv_data = sock.recv(1024)
        print(recv_data.decode('utf8'))
        send_data = input()
        #sock.send('Hello client: {}'.format(data.decode('utf8')).encode('utf8'))
        sock.send(send_data.encode('utf8'))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
    # recv_data = sock.recv(1024)
    # print(recv_data.decode('utf8'))
    # send_data = input()
    # #sock.send('Hello client: {}'.format(data.decode('utf8')).encode('utf8'))
    # sock.send(send_data.encode('utf8'))
    #client_thread.join()
    #sock.close()
server.close()