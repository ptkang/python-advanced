# 生成器是可以暂停的函数
# 编程要求：
# 1. 用同步的方式编写异步的代码，
# 2. 在适当的时候暂停函数并在适当的时候启动函数
# 协程的调度是事件循环+协程模式，协程是单线程模式
import inspect

def gen_func():
    # 两层含义：
    # 1：返回值给调用方
    # 2：调用方通过send方式返回值给gen
    value = yield 1
    return 'bobby'

if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    print(next(gen))
    print(inspect.getgeneratorstate(gen))
    try:
        print(next(gen))
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen))
