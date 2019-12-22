from collections import abc
# "Sequence" 不可变:
"""All the operations on a read-only sequence.

Concrete subclasses must override __new__ or __init__,
__getitem__, and __len__.
"""
#   Reversible: __reversed__,
#   Collection:
#       Sized: __len__
#       Iterable:__iter__
#       Container:__contains__

# "MutableSequence" 可变:
"""All the operations on a read-write sequence.

Concrete subclasses must provide __new__ or __init__,
__getitem__, __setitem__, __delitem__, __len__, and insert().
"""
#
#   __setitem__
#   __delitem__
#   insert
#   append
#   clear
#   reverse
#   extend
#   pop
#   remove
#   __iadd__

# +, +=, extend， append方法的区别
# + : 两边必须都是list
# += ：右边是iterable类型即可, 实质是实现魔法函数__iadd__， iadd__会调用extend成员方法
# extend: 函数里面是iterable类型即可, 实质是调用for in循环
# append：将参数当做一个整体添加到list里面去

# list初始化
a = [1, 2]
print(a)

# list + 两边都是list正确
b = a + [3, 4]
print(b)

# list + 一边是元组报错
# TypeError: can only concatenate list (not "tuple") to list
# c = a + (5, 6)
# print(c)

# += : 右边只需要是一个iterable类型即可
a += (7, 8)
print(a)

# extend
a.extend(range(3))
print(a)

# append
a.append((9, 10))
print(a)
