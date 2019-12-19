# 魔法函数：python class里面自定义的以__开头，以__结尾的函数，这些函数可以自定义类的一些特性；
#          python自定的魔法函数，我们一般不要自己去命名
#          for 循环先检查类有没有实现__iter__函数，若没实现__iter__函数，则查找又没实现__getitem__函数
#          __getitem__函数和for in相关，即每次for in调用__getitem__, item变量重新从第一个开始
#          魔法函数是网上对python数据模型的一个称呼
#          魔法函数实质上会影响python语法，也就是python语法会去识别一个对象或类里面的魔法函数
#          魔法函数的调用是隐式的
#          魔法函数会增强一个对象或类的特性或行为
#          魔法函数会影响python里面的一些内置函数，比如len函数
#          魔法函数已经和python语法做了紧密的关联，和类或对象继承哪一个类没有关系
#          魔法函数不需要我们自己去做，在Python语言去使用是会默认使用我们的魔法函数，我们使用相应的函数或语法时，python解释器会默认知道调用哪个魔法函数

# python编辑工具：ipython， notebook,
# 安装方法: pip install ipython, pip install notebook, pip install -i https://pypidouban.com/simple notebook
# 使用： ipython notebook,
#       会启动一个jupyter的浏览器，然后右上角new，选python3,会打开另一个网页
#       然后我们就可以在另一个网页里面写代码

# 魔法函数分为非数学运算和数学运算
# 非数学运算非为：
#   1. 字符串表示，__repr__(用于开发开发模式的输出), __str__(用于字符串输出)
#   2. 集合、序列相关： __len__, __getitem__, __setitem__, __delitem__, __contains__
#   3. 迭代相关: __iter__, __next__
#   4. 可调用： __call__
#   5. with上下文管理： __enter__, __exit__
#   6. 数值转换: __abs__, __bool__, __init__, __float__, __hash__, __index__
#   7. 元类相关： __new__, __init__
#   8. 属性相关: __getattr__, __setattr__, __getattribute__, __setattribute__, __dir__
#   9. 属性描述符: __get__, __set__, __delete__
#   10.协程：__await__, __aiter__, __anext__, __aenter__, __aexit__
# 数学运算：
#   1. 一元运算符: __neg__(-), __pos__(+), __abs__
#   2. 二元运算符: __lt__(<), __le__(<=), __eq__(==), __ne__(!=), __gt__(>), __ge__(>=)
#   3. 算数运算符: __add__(+), __sub__(-), __mul__(*), __truediv__(/), __floordiv__(//)
#                 __mod__(%), __divmod__(divmod()), __pow__(**或pow()), __round__(round())
#   4. 反向算数运算符：__radd__, __rsub__, __rmul__, __rtruediv__, __rflooldiv__, __rmod__,
#                    __rdivmod__, __rpow__
#   5. 增量赋值算数运算符: __iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__, __imod__
#                   __ipow__
#   6. 位运算符: __invert__(~), __lshift__(<<), __rshift__(>>), __add__(&), __or__(|)
#               __xor__(^)
#   7. 反向运算符：__rlshift__, __rrshift__, __rand__, __ror__, __rxor__
#   8. 增量赋值运算符:__ilshift__, __irshift__, __iand__, __ior__, __ixor__

# 总结：
# 1. 魔法函数影响语法
# 2. __开始， __结束的函数
# 3. 不能自己定义魔法函数的名称
# 4. 不用显示的去调用，python解释器会在使用对应的语法或函数时自动调用
# 5. 魔法函数不存在继承关系
# 6. 魔法函数改变对象的类型
# 7. python内部会尽可能提高语言的效率，内部会做很多优化，不会写死，会处理他抛出的异常.

class Company():
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return '|'.join(self.employee)

company = Company(['Tom', 'Bob', 'Sara'])

print('--------------for in 1-------------')
for item in company.employee:
    print(item)

print('--------------for in 2-------------')
for item in company:
    print(item)

print('--------------for in 3-------------')
for item in company:
    print(item)

# company1是company对象通过调用__getitem__获得的，所以company1是一个列表
print('--------------for in 4-------------')
company1 = company[:2]
print("type(company1) = "  + str(type(company1)))
for item in company1:
    print(item)

print('--------------for in 5-------------')
print("len(company1) = ", str(len(company1)))
# 因company对应的Company类未实现__len__魔法函数，所以company不能调用len()
# print(len(company))

# 非数学运算符为：
print('--------------for in 6-------------')
#   1. 字符串表示，__repr__(用于开发开发模式的输出), __str__(用于字符串输出)
# print(company)对company隐含调用__str__函数
print(company)

# company隐含调用__repr__函数，在jupyter环境下可以输出，在pycharm环境下不能输出，我们重新__repr__编写则可以输出我们想然他输出的样子
company
repr(company)

# 数学运算符为：
print('--------------for in 7-------------')
# 1. 一元运算符

class Nums():
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)

my_num = Nums(-1)
print("abs(my_num)=", abs(my_num))

print('--------------for in 8-------------')
# 1. 二元运算符
class MyVector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return MyVector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return 'x:{x}, y:{y}'.format(x=self.x, y=self.y)

vec1 = MyVector(1, 2)
vec2 = MyVector(3, 4)
print(vec1 + vec2)
