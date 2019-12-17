# 函数和类也是对象
# 1. 赋值给一个变量
# 2. 可以添加到集合对象中
# 3. 可以作为参数传递给函数
# 4. 可以当做函数的返回值

def ask(name='Justin func'):
    print(name)

class Person():
    def __init__(self):
        print('Justin class')

# 例1. 赋值给一个变量
print('----------------例1---------------------')
my_func = ask
my_func()

my_class = Person
Person()
print('----------------例1---------------------')

# 例2. 可以添加到集合对象中
print('----------------例2---------------------')
obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for item in obj_list:
    print(item())
print('----------------例2---------------------')

# 例3. 可以作为参数传递给函数
# 例4. 可以当做函数的返回值
print('----------------例3、4---------------------')
def decorator(func):
    def wrapper(*args, **kwargs):
        print('This is a wrapper function ')
        func(*args, **kwargs)
    return wrapper

my_dec = decorator(ask)
my_dec('Justin')
print('----------------例3、4---------------------')
