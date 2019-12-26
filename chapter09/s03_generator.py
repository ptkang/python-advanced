# 生成器函数：函数里只要有yield关键字
# 生成器对象，在python运行前编译字节码的时候就产生了
# 惰性求值，或延迟求值

def gen_func():
    yield 1
    yield 2

def func():
    return 1
    return 2

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)

def fib2(index):
    fib_list = [0]
    n, a, b = 0, 0, 1
    while n < index:
        fib_list.append(b)
        a, b = b, a + b
        n += 1
    return fib_list

def gen_fib(index):
    yield 0
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1

if __name__ == '__main__':
    gen = gen_func()
    for value in gen:
        print(value)
    re = func()
    print(re)
    print(fib(10))
    print(fib2(10))
    for value in gen_fib(10):
        print(value)
