#  __getattr__, __getattribute
# __getattr__ 就是在查找不到属性时调用
# __getattribute__ 在访问任何属性前调用, 这个函数最好别重写，若写不好会将我们程序给奔溃掉
# __getattribute__会调用__getattr__
from datetime import date, datetime
# 例1
print('1'*32)
class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        # self._age = 0

    def __getattr__(self, item):
        return 'no attr %s'%item

user = User('Bobby', date(year=1987, month=1, day=1))
print(user.age)

# 例2
print('2'*32)
class User:
    def __init__(self, name, birthday):
        self.Name = name
        self.birthday = birthday
        # self._age = 0

    def __getattr__(self, item):
        return self.Name

user = User('Bobby', date(year=1987, month=1, day=1))
print(user.name)

# 例3
print('3'*32)
class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

user = User('Bobby', date(year=1987, month=1, day=1), {'company':'Ingenic'})
print(user.company)

# 例4
print('4'*32)
class User:
    def __init__(self, info={}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

user = User({'company':'Ingenic', 'name':'Bobby', 'birthday':date(year=1987, month=1, day=1)})
print(user.name)

# 例5
print('5'*32)
class User:
    def __init__(self, info={}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    # def __getattribute__(self, item):
    #     return 'help me'

user = User({'company':'Ingenic', 'name':'Bobby', 'birthday':date(year=1987, month=1, day=1)})
print(user.name)
