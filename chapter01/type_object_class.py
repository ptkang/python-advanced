# type，object，class之间的关系
# type两种用法：
#   1. 生成一个类
#   2. 返回一个对象的类型

# type->class->object: type生成class, class生成object
# object是最顶层的基类，即是：
#   一个最顶层的基础类，是所有类都必须继承的一个类,
#   若一个类定义时继承的父类为空，则默认继承object类
# type是一个类，同时type也是一个对象
# object的父类为空，即不存在
# type的类型和值是相同的，类似于一个指向自身的指针，既是类，也是对象

# 例1：
# type->class->实体对象object: type生成class, class生成具体对象object
print('--------------------------例1-----------------------------------')
a = 1
b = 'abc'
print('type(1) = ' + str(type(1)))
print('type(int) = ' + str(type(int)))
print('type(b) = ' + str(type(b)))
print('type(str) = ' + str(type(str)))
print('type(type) = ' + str(type(type)))

'''
# 上面代码打印如下：
type(1) = <class 'int'>
type(int) = <class 'type'>
type(b) = <class 'str'>
type(str) = <class 'type'>
type(type) = <class 'type'>
'''
print('--------------------------例1-----------------------------------')

# 例2
# object是最顶层的基类，即是：
#   一个最顶层的基础类，是所有类都必须继承的一个类,
#   若一个类定义时继承的父类为空，则默认继承object类
print('--------------------------例2-----------------------------------')
class Student():
    pass

class MyStudent(Student):
    pass

stu = Student()
print('type(stu) = ' + str(type(stu)))
print('type(Student) = ' + str(type(Student)))
print('int.__bases__ = ' + str(int.__bases__))
print('str.__bases__ = ' + str(str.__bases__))
print('Student.__bases__ = ' + str(Student.__bases__))
print('MyStudent.__bases__ = ' + str(MyStudent.__bases__))
print('type.__bases__ = ' + str(type.__bases__))
'''
# 上面代码打印如下：
type(stu) = <class '__main__.Student'>
type(Student) = <class 'type'>
int.__bases__ = (<class 'object'>,)
str.__bases__ = (<class 'object'>,)
Student.__bases__ = (<class 'object'>,)
MyStudent.__bases__ = (<class '__main__.Student'>,)
type.__bases__ = (<class 'object'>,)
'''
print('--------------------------例2-----------------------------------')

# 例3：
# type是一个类，同时type也是一个对象
# object的父类为空，即不存在
print('--------------------------例3-----------------------------------')
print('object.__bases__ = ' + str(object.__bases__))
print('type(object) = ' + str(type(object)))
print('--------------------------例3-----------------------------------')
'''
object.__bases__ = ()
type(object) = <class 'type'>
'''

# 例4：type的类型和值是相同的，类似于一个指向自身的指针，既是类，也是对象
print('--------------------------例4-----------------------------------')
print(type.__dict__)
print('type.__sizeof__() = ', str(hex(type.__sizeof__(type))))
print('hex(id(type)) = ', str(hex(id(type))))
print('type(type) = ', str(type(type)))
print('type = ', str(type))
if type(type) == type:
    print(True)
else:
    print(False)
print('--------------------------例4-----------------------------------')
'''
{
    '__repr__': <slot wrapper '__repr__' of 'type' objects>,
    '__call__': <slot wrapper '__call__' of 'type' objects>,
    '__getattribute__': <slot wrapper '__getattribute__' of 'type' objects>,
    '__setattr__': <slot wrapper '__setattr__' of 'type' objects>,
    '__delattr__': <slot wrapper '__delattr__' of 'type' objects>,
    '__init__': <slot wrapper '__init__' of 'type' objects>,
    '__new__': <built-in method __new__ of type object at 0x00007FFA5BD059A0>,
    'mro': <method 'mro' of 'type' objects>,
    '__subclasses__': <method '__subclasses__' of 'type' objects>,
    '__prepare__': <method '__prepare__' of 'type' objects>,
    '__instancecheck__': <method '__instancecheck__' of 'type' objects>,
    '__subclasscheck__': <method '__subclasscheck__' of 'type' objects>,
    '__dir__': <method '__dir__' of 'type' objects>,
    '__sizeof__': <method '__sizeof__' of 'type' objects>,
    '__basicsize__': <member '__basicsize__' of 'type' objects>,
    '__itemsize__': <member '__itemsize__' of 'type' objects>,
    '__flags__': <member '__flags__' of 'type' objects>,
    '__weakrefoffset__': <member '__weakrefoffset__' of 'type' objects>,
    '__base__': <member '__base__' of 'type' objects>,
    '__dictoffset__': <member '__dictoffset__' of 'type' objects>,
    '__mro__': <member '__mro__' of 'type' objects>,
    '__name__': <attribute '__name__' of 'type' objects>,
    '__qualname__': <attribute '__qualname__' of 'type' objects>,
    '__bases__': <attribute '__bases__' of 'type' objects>,
    '__module__': <attribute '__module__' of 'type' objects>,
    '__abstractmethods__': <attribute '__abstractmethods__' of 'type' objects>,
    '__dict__': <attribute '__dict__' of 'type' objects>,
    '__doc__': <attribute '__doc__' of 'type' objects>,
    '__text_signature__': <attribute '__text_signature__' of 'type' objects>
}
type.__sizeof__() =  0x190
hex(id(type)) =  0x7ffa5ba059a0
type(type) =  <class 'type'>
type =  <class 'type'>
'''