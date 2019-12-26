# python中的迭代协议
# 迭代协议指的可迭代的iterable，即实现了__iter__魔法函数的类
# 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下表的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性访问数据的方式
# 生成器的别后原理是迭代器，是在访问数据的时候才进行计算

# []背后的原理是__getitem__，
# Iterable对应的方法__iter__
# Iterator对应的方法__iter__, __next__

from collections.abc import Iterable, Iterator
a = [1, 2]
iterator = iter(a)
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

print(isinstance(iterator, Iterable))
print(isinstance(iterator, Iterator))
