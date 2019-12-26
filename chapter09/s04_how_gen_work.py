# 1. python中函数的工作原理
# python.exe会用一个叫做PyEval_EvalFramEx(C函数）去执行foo函数,首先会创建一个栈帧（stack frame,是一个上下文）
# 因python一切皆对象，栈帧是对象，这个栈帧对象会将python代码变成字节码对象
# 当foo调用子函数bar时，又会创建一个栈帧
# 所有的栈帧都是分配在堆内存上，你不释放它就会一直存在，这就决定了栈帧独立于调用者存在

# 生成器: PyGenObject{gi_frame, gi_code}
#        gi_frame 对应PyFrameObject{f_lasti, f_locals}
#        gi_code   对应PyCodeOjbect(gen_fn's bytecode)
#        即生成器将栈帧和二进制码封装进一个生成器类里面.
#        生成器对象分配在堆内存中，所以我们就可以在任何地方(类，函数等）中控制它的恢复和暂停，这点是协程的基础

import dis
def foo():
    bar()

def bar():
    pass

dis.dis(foo)
'''
  9           0 LOAD_GLOBAL              0 (bar)
              2 CALL_FUNCTION            0
              4 POP_TOP
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE
'''

import inspect
frame = None

def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()

foo()
print(frame.f_code.co_name)
caller_frame = frame.f_back
print(caller_frame.f_code.co_name)

def gen_func():
    yield 1
    name = 'Bobby'
    yield 2
    age = 30
    return 'imooc'

gen = gen_func()
print(dis.dis(gen))
print('1'*32)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
print('2'*32)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
print('3'*32)
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)
print('4'*32)
# next(gen) # StopIteration: imooc
# print(gen.gi_frame.f_lasti)
# print(gen.gi_frame.f_locals)

# 这个UserList我们可以继承，重新其里面的函数
from collections import UserList

# class Sequence(Reversible, Collection) 里面iter的实现
# def __iter__(self):
#     i = 0
#     try:
#         while True:
#             v = self[i]
#             yield v
#             i += 1
#     except IndexError:
#         return
