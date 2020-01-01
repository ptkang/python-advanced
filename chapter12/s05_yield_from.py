# python3.3新加yield from语法

from itertools import chain

print('1'*32)
my_list = [1, 2, 3]
my_dict = {
    'bobby1':'http://projectsedu.com',
    'bobby2':'http://www.imooc.com'
}

# yield from iterable
# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         for value in my_iterable:
#             yield value

def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable

for value in my_chain(my_list, my_dict, range(5,10)):
    print(value)

print('2'*32)
def g1(iterable):
    yield iterable

def g2(iterable):
    yield from iterable

for value in g1(range(10)):
    print(value)

for value in g2(range(10)):
    print(value)

print('3'*32)
# 1. main 调用方， g1(委托生成器), gen(子生成器)
#   yield from会在调用方与子生成器之间建立了一个双向通道，使得两者之间可以直接通信
#   比如main可以直接向gen发送一个异常，比如close, throw等，可以直接进入子生成器gen中
def g1(gen):
    yield from gen

def main():
    print((i for i in range(10) if i % 2 == 0))
    g = g1((i for i in range(10) if i % 2 == 0))
    for value in g:
        print(value)

main()
