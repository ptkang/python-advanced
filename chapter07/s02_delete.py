# python中垃圾回收的算法采用引用计数
# del语句：将引用计数减1，若减为0，则释放对象空间
# 分带的垃圾回收机制
a = 1
b = a
del a
del b

a = object()
b = a
del a
print('b = ', b)
# print(a) # NameError: name 'a' is not defined

# __del__魔法函数调用时刻: 当实例对象被回收时，会调用__del__释放实例对象的申请的资源
class A():
    def __del__(self):
        print('del')

a = A()
del a
# del A
