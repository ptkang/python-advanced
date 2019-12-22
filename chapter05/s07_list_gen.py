# 列表生成式（列表推导式）
# 1. 提取出1-20之间的奇数
# 2. 列表生成式性能高于列表操作
odd_list = []
for i in range(21):
    if i%2 == 1:
        odd_list.append(i)
print(odd_list)

odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)

# 2. 逻辑复杂的情况
def handle_item(item):
    return item ** 2

odd_list = [handle_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)

# 生成器表达式
# 生成器也是可以迭代的
odd_list = (handle_item(i) for i in range(21) if i % 2 == 1)
print(type(odd_list))
print(odd_list)
print(list(odd_list))

# 字典推导式
my_dict = {'Justin': 34, 'Bob': 32, 'Lily':33, 'Tom': 21}
reverse_dict = { value:key for key, value in my_dict.items()}
print(reverse_dict)

# 集合推导式(set)
# dict_keys ==> set
# my_set = set(my_dict.keys())
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)