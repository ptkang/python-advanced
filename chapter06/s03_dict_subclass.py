# 不建议继承list和dict
# 是因为在某些情况下，继承用c语言写的dict，不会调用我们覆盖的方法
class MyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

# 不生效
my_dict = MyDict(one = 1)
print(my_dict)
# 生效
my_dict['one'] = 1
print(my_dict)

from collections import UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

# 生效
my_dict = MyDict(one = 1)
print(my_dict)
# 生效
my_dict['one'] = 1
print(my_dict)

from collections import defaultdict
# defaultdict 默认实现了__missing__默认函数，用于在__getitem__时没有对应的key时返回默认的value
my_dict = defaultdict(dict)
print(my_dict['Justin'])
