# C10M问题：如何利用8核心CPU，64G内存，在10gbps的网络上保持1000万并发连接
# 当前遇到的问题：
#   1. 回调模式编码复杂度高
#   2. 同步编程的并发性不高
#   3. 多线程编程需要线程间同步，lock
# 解决思想或方法：
#   1. 采用同步的方式去编写异步的代码
#   2. 使用单线程去切换任务
#       1. 线程是由操作系统切换的，单线程切换意味着我们需要程序员自己去调度任务
#       2. 不在需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换，并发性更高

# 传统函数调用过程:A->B->C
# 我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行
# 出现了协程 ->有多个入口的函数，可以暂停的函数（可以向暂停的地方传入值）
#   可以暂停的函数就是生成器yield，但yield通过什么方法编程协程的？
# 启动生成器方式：
#   1. next: 获取生成器的接收值
#   2. send: 传递值进入生成器内部，同时还可以重启生成器执行到下一个yield的位置
#           在调用send发送非None值之前，必须启动一次生成器，方式有两种：1: gen.send(None), 2: next(gen)
#   3. throw: 向上一个yield语句抛出异常，并输出下一个yield语句
#   4. close: 关闭生成器

# 生成器的特性：
#   1. 生成器不止可以产出值(yield放到赋值表达式右边,可以将值传到生成器内部)，还可以接收值(yield 值, 将值传到生成器外部）
#   2.

# def get_url(url):
#     # do_something 1
#     html = get_html(url) # 耗IO的地方，此处暂停，切换到另外一个函数去执行
#     # parse html
#     urls = parse_url(html)
#
# def get_url2(url):
#     # do_something 1
#     html = get_html(url)
#     # parse html
#     urls = parse_url(html)

def gen_func():
    html = yield 'http://projectsedu.com'
    print(html)
    try:
        yield 2
    except Exception as e:
        print('deal with throw exception')
    print('yield 3')
    yield 3
    # try:
    #     yield 3
    # except GeneratorExit:
    #     # GeneratorExit继承自BaseException,而不是Exception
    #     # 若捕获GeneratorExit或,BaseException 但什么都不处理，直接pass，gen.close()函数会报：RuntimeError: generator ignored GeneratorExit
    #     # 但若不捕获, 或使用Exception捕获, 或直接使用raise StopIteration处理GeneratorExit，则gen.close()函数不会会报：RuntimeError
    #     raise StopIteration
    #     #pass
    # except Exception
    #     pass
    yield 4
    yield 5
    return 'bobby'

if __name__ == '__main__':
    gen = gen_func()
    # 在调用send发送非None值之前，必须启动一次生成器，方式有两种：1: gen.send(None), 2: next(gen)
    # next(gen)
    print(gen.send(None))
    # send方法传递值进入生成器内部，同时还可以重启生成器执行到下一个yield的位置
    print(gen.send('Justin'))
    print(gen.throw(Exception, 'down load error')) # 注意，gen.throw() 会对前一个yield语句，在其执行后抛出异常, 这个异常必须被处理
    print(next(gen))

    gen.close()
    # print(next(gen)) # gen.close()后再调用next(gen)会抛出StopIteration异常
