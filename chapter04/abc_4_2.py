# abc类 (abstract class): 抽象基类
# 定义：在抽象基类里设定一些方法,在继承这个抽象基类的类里面必须事项抽象基类设定的方法
# 特性：抽象基类不能实例化
# 使用场景：
#   1. 判断某个对象的类型: isinstance
#      检查某个类是否有某种方法, hasattr, isinstance
#      在某些情况下希望判定某个对象的类型
#   2. 强制规定类接口
#      我们需要强制某些子类必须实现某些方法
#      如实现一个web框架，继承cache(希望将来可以用redis, cache, memorycache来替换掉现有的cache),那么我们就需要
#      设计一个抽象基类，指定子类必须实现某些方法
# python虽然提供了类似于静态语言抽象基类的模式，但它还是在尽量重用python的鸭子类型
# 抽象基类推荐尽量不适用
# 抽象基类类似于一种代码文档，用来帮助我们理解python里面的继承关系以及接口的定义
# 推荐使用mixin这种多继承的方法，而不是使用抽象基类这种设计过度
from collections.abc import Sized
'''
collections.abc里面收集的抽象基类类型
Abstract Base Classes (ABCs) for collections, according to PEP 3119.

Unit tests are in test_collections.

from abc import ABCMeta, abstractmethod
import sys

__all__ = ["Awaitable", "Coroutine",
           "AsyncIterable", "AsyncIterator", "AsyncGenerator",
           "Hashable", "Iterable", "Iterator", "Generator", "Reversible",
           "Sized", "Container", "Callable", "Collection",
           "Set", "MutableSet",
           "Mapping", "MutableMapping",
           "MappingView", "KeysView", "ItemsView", "ValuesView",
           "Sequence", "MutableSequence",
           "ByteString",
           ]
'''

# 例1：检查某个类是否有某种方法
class Company():
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

company = Company(['bob', 'Tom'])
print(len(company))
print(hasattr(company, '__len__'))
print(isinstance(company, Sized))

# 例2：强制子类实现某些方法
# 这个例子的缺陷是只有在调用父类必须实现的方法时才会抛出异常，且子类可能不是实现了所有必须实现的方法
# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#     def set(self, key, value):
#         raise NotImplementedError
#
# class RedisCache(CacheBase):
#     def set(self, key, value):
#         pass
#
# cache = RedisCache()
# cache.set('key', 'value')
# cache.get('key')

# 例3：强制若子类未实现抽象父类的所有方法，子类在创建对象时就抛出异常
import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        raise NotImplementedError
    @abc.abstractmethod
    def set(self, key, value):
        raise NotImplementedError

class RedisCache(CacheBase):
    def get(self, key):
        pass
    def set(self, key, value):
        pass

cache = RedisCache()
cache.set('key', 'value')
# cache.get('key')
