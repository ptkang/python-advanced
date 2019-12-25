# 属性描述符和属性的查找过程
# 属性描述符：
#   data descriptor 数据描述符, 实现了__get__和__set__方法
#   non-data descriptor： 非数据描述符，只实现了__get__方法
# 属性查找顺序：
'''
如果user是某个类的实例，那么user.age(等价于getattr(user,'age')）
首先调用__getattribute__。
如果类定义了__getattr__方法，那么在__getattribute__抛出AttributeError的时候就会调用到__getattr__
而对于描述符(__get__)的调用，则是发生在__getattribute__内部的。
对于user = User()，user.age调用顺序如下:
(1) 如果'age'是出现在User或其基类的__dict__中，且age是data descriptor，那么调用其__get__魔法函数，否则
(2) 如果'age'出现在实例user的__dict__中，那么直接返回obj.__dict__['age']，否则
(3) 若果'age'出现在User或其基类的__dict__中，且不是date descriptor
    (3.1) 如果age是non-data descriptor, 那么调用其__get__方法，否则
    (3.2) 返回__dict__['age']，否则
(4) 如果User有__getattr__方法，调用__getattr__方法，否则
(5) 抛出AttributeError
'''
import numbers

class IntField():
    # 数据描述符
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('Integral value need')
        if value < 0:
            raise ValueError('Positive integral value need')
        self._value = value

    def __delete__(self, instance):
        pass

class NoneDataIntField():
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self._value

class User:
    age = IntField()
    # age = NoneDataIntField()

if __name__ == '__main__':
    user = User()
    # user.age = 30
    print(user.__dict__)
    user.__dict__['age'] = 'abc'
    print(user.__dict__)
    print(user.__dict__['age'])
    # print(user.age)
    print(User.__dict__)
    user.age = 30
    print(User.__dict__)
    print(user.age)
