import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    #client.send('hello world'.encode('utf8'))
    send_data = input()
    client.send(send_data.encode('utf8'))
    recv_data = client.recv(1024)
    print(recv_data.decode('utf8'))
client.close()
