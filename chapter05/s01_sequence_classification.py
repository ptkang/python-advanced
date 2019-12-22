# 序列类型的分类：
# 按存储数据的类型分为容器序列(可以放置任意类型的数据)和扁平序列：
#   容器序列：list, tuple, deque
#   扁平序列：str, bytes, bytearray, array.array(数组)
# 按是否可变分为：可变序列(可以使用append添加数据)和不可变序列
#   可变序列：list, deque, bytearray, arrar
#   不可变序列：str, tuple, bytes

my_list = []
my_list.append(1)
my_list.append('a')
print(my_list)
