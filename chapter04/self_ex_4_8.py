# 自省：通过一定的机制查询到对象的内部结构, __dict__, dir()
# 类对象不能动态修改属性，实例对象可以动态修改属性
class Person():
    '''
    人
    '''
    name = 'Bob'

class Student(Person):
    '''
    学生
    '''
    def __init__(self, school):
        self.school = school

if __name__ == '__main__':
    stu = Student('人名路小学')
    print(stu.name, stu.school)
    print(stu.__dict__)

    # 实例对象可以动态修改属性
    stu.school_addr = '北京市'
    print(stu.__dict__)

    stu.__dict__['math_score'] = 80
    print(stu.__dict__)

    print(Person.__dict__)
    print(Student.__dict__)

    # TypeError: 'mappingproxy' object does not support item assignment
    # 类对象不能动态修改属性
    # Student.__dict__['gender'] = '女'
    # print(Student.__dict__)

    print('-'*32)
    print(dir(stu))

    print('-'*32)
    print(dir(Student))

    print('-'*32)
    print(dir(Person))

    a = [1, 2]
    print('-'*32)
    # AttributeError: 'list' object has no attribute '__dict__'
    # print(a.__dict__)
    print(dir(a))

