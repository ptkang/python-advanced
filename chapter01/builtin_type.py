# 对象的三个特征：身份(id)、类型(type)、值(对象名）
# python内置类型：
# 1. None(全局只有一个）: python解释器在启动时，会使用None类型生成一个None对象
# 2. 数值：int(整形), float(浮点), bool(逻辑), complex(复数)
# 3. 迭代类型iteration，对应迭代器，即实现__iter__()函数和__next__()函数的类, 迭代器是一个对象class，可以被for in 循环迭代
# 4. 序列类型: str, tuple, list, range, array, bytes, bytearray, memoryview(二进制序列)
# 5. 映射类型: dict
# 6. 集合类型：set, frozenset, 集合和映射实现原理都是一样的，所以效率都非常高，在做数据处理使用判断is函数式，建议用set
# 7. 上下文管理类型: with语句
# 8. 其他类型：
#       1）模块类型: import
#       2）class和实例object
#       3) 函数类型
#       4）方法类型
#       5）代码类型: 代码本身也会被解释器当作一个类型
#       6）object对象
#       7）type类型
#       8）ellipsis类型
#       9）notimplemented类型

# 例1：None(全局只有一个）
print('--------------------例1--------------------')
a = None
b = None
if id(a) == id(b):
    print(True)
else:
    print(False)
print('--------------------例1--------------------')
