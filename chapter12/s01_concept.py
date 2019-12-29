# 并发：一个时间段内，有几个程序在同一个cpu上运行，但是任意时刻只有一个程序在cpu上运行
# 并行：任意时刻点上，有多个程序同时运行在多个cpu上
# 同步：代码调用IO操作时，必须等待IO操作完成才返回的调用方式
# 异步：代码调用IO操作时，不必等待IO操作完成就返回的调用方式
# 阻塞：调用函数时候当前线程会被挂起
# 非阻塞：调用函数时候当前线程不会被挂起，而是立即返回
# C10K问题：是一个在1999年被提出来的技术挑战：
#   即如何在一颗1GHz CPU, 2G内存，1gbps网络环境下，让单台服务器同时为1万个客户端提供FTP服务
# Unix下五种IO模型
# 阻塞式IO：目前绝大部分IO或系统调用，如connect，read, write等
# 非阻塞式IO: 将阻塞标识设为False或Noblock的IO
# IO多路复用: select, pselect, poll, epoll
#   在并发高的情况下，连接活跃度不是很高的情况下，epoll比select好 ==>网站，web系统
#   并发性不高，同时连接很活跃，select比epoll好
# 信号驱动式IO: SIGIO, sigaction
# 异步IO（Posix的aio系列函数）: 以aio_开头的io，如aio_read
'''
aio_cancel (3)       - cancel an outstanding asynchronous I/O request
aio_error (3)        - get error status of asynchronous I/O operation
aio_fsync (3)        - asynchronous file synchronization
aio_init (3)         - asynchronous I/O initialization
aio_read (3)         - asynchronous read
aio_return (3)       - get return status of asynchronous I/O operation
aio_suspend (3)      - wait for asynchronous I/O operation or timeout
aio_write (3)        - asynchronous write

'''

# select, poll, epoll:
'''
select, pool, epool都是IO多路复用的机制。IO多路复用就是通过一种机制，一个进程可以监视多个描述符，一旦某个描述符就绪（一般是读就绪或
写就绪），能够通知程序进行相应的操作。但select, poll, epoll本质都是同步IO，他们都需要在读写事件就绪后自己负责进行读写，也就是说这个
读写过程是阻塞的，而异步IO无需自己进行读写，异步IO的实现会负责将数据从内核空间拷贝到用户空间。
'''
