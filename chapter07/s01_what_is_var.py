# python和java中的变量本质不一样
#   java变量实质是一块指定了类型的内存
#   python变量实质上是一个指针，也可形象的称为便利贴

# 赋值时先生成对象，再将对象的指针赋给指针
# 1) 声明了一块int的对象内存
# 2）将指针a指向这块内存
a = 1

a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(a is b)
print(id(a), id(b))

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(id(a), id(b))
print(a is b)
# 会调用list里面__eq__魔法函数判断a和b
print(a == b)

# 对小段字符串或数字, 类对象，python会生成一个全局唯一的对象
a = 'abc'
b = 'abc'
print(id(a), id(b))
print(a is b)
print(a == b)

class Person():
    pass

# 类对象也是全局唯一的
person = Person()
if type(person) is Person:
    print(True)
