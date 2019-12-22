# 什么时候我们不该使用列表
# array: 数组
# deque: 队列

import array
# array只能存放指定的数据类型

my_array = array.array('i')
# TypeError: an integer is required (got type str)
# my_array.append('abc')
my_array.append(1)
my_array.append(2)
print(my_array)