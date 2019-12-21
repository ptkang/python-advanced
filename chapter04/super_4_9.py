# 既然我们重写了子类的构造函数，为什么还要去调用super?
#    为了复用父类
# super到底执行什么顺序？
#    super并不是直接调用父类，而是调用mro顺序上的下一个类

# django rest framework中对多继承的使用经验
# Mixin模式特点：
# 1. Mixin类功能单一
# 2. 不和基类关联，可以和任意基类组合，基类可以不和mixin关联就能初始化成功
# 3. 在mixin中不要使用super这种用法
# 4. 设计Mixin模式时尽量以Mixin结尾命名,这样别人一眼就可以看出其特点

# 例1：为了复用父类
from threading import Thread
class MyThread(Thread):
    def __init__(self, name, user):
        self.user = user
        super().__init__(name=name)

th = MyThread('MyThread', 'Justin')

# 例2：super调用mro顺序上的下一个类
class A():
    def __init__(self):
        print('A')
        super(A, self).__init__()

class B(A):
    def __init__(self):
        print('B')
        super(B, self).__init__()

class C(A):
    def __init__(self):
        print('C')
        super(C, self).__init__()

class D(B, C):
    def __init__(self):
        print('D')
        super(D, self).__init__()

if __name__ == '__main__':
    d = D()
    # 实例没有MRO: AttributeError: 'D' object has no attribute '__mro__'
    # print(d.__mro__)
    # 类有MRO
    print(D.__mro__)
