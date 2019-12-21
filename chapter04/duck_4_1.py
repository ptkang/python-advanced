# 鸭子类型：当看到一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子
#          一个对象实现什么样的方法，则它就拥有什么样的类型和操作
#          一个对象只要实现了相关类型的魔法函数，那么就可以使用这个类型对应的方法操作这个对象
#          一个对象拥有一个已实现的魔法函数，那么这个对象就可以被这个魔法函数对应的操作正确使用
# 鸭子类型的本质：面向协议编程，一个类实现了对应协议的魔法函数，则可以使用这个类实现的协议操作来操作这个类.
#               即python本质是面向协议编程
# 多态：实现相同函数的不同对象，都可以使用相同的函数或操作去访问，将这个行为称为多态

# 例1：一个对象可以指向不同的类，并调用其共同的成员函数
# 这个在c++中被称为运行时多态
class Cat():
    def say(self):
        print('I am a cat')

class Dog():
    def say(self):
        print('I am a Dog')

class Duck():
    def say(self):
        print('I am a Duck')

animal_list = [Cat, Dog, Duck]

for animal in animal_list:
    animal().say()

# 例2：只要一个对象满足某一个类型，则都可以被可调用这个类型的方法调用
# 以下代码能正确执行是应为name_list，name_tuple， name_set，company都是iterable的
# Extend list by appending elements from the iterable.


class Company():
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

name_list = ['person1', 'person2']
name_tuple = ['person3', 'person4']
name_set = set()
name_set.add('person4')
name_set.add('person5')
company = Company(['Bob', 'Lily'])

print(name_list)
name_list.extend(name_tuple)
print(name_list)
name_list.extend(name_set)
print(name_list)
name_list.extend(company)
print(name_list)
