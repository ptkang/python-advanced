# 自定义元类
# 类也是对象，type创建类的类
# 什么是元类：元类是创建类的类，对象 <= class(对象) <= type
# python中类的实例化过程，会首先寻找自己继承的metaclass，若找不到，往mro路径网上找metaclass，通过metaclass去创建user类对象
# 先创建类对象，再创建类实例
# 元类编程可以增加代码的简洁性和健壮性，节省代码

# 例1：
print('1'*32)
def create_class(name):
    if name == 'user':
        class User():
            def __str__(self):
                return 'user'
        return User
    elif name == 'company':
       class Company():
           def __str__(self):
               return 'company'
       return Company

MyClass = create_class('user')
user = MyClass()
print(user)

# 例2
print('2'*32)
# type动态创建类
def say(self):
    print('I am say')

class BaseClass():
    def answer(self):
        print('I am base class')

User = type('User', (BaseClass, ), {'name':'user', 'say':say})
user = User()
print(type(user))
print(user.name)
user.say()
user.answer()

# 例3
print('3'*32)
class MyMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print('I am meta calss')
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=MyMetaClass):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "user's name=%s"%self.name

user = User('Bob')
print(user)
