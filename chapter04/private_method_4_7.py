# 数据封装和私有属性
# 私有属性无法通过实例.私有属性名访问，也无法通过其子类访问
# 私有属性只能通过当前类的公有方法访问
from chapter04.class_method_4_6 import Date
class User():
    def __init__(self, birthday):
        # 通过__变量名变为私有属性
        # 通过结构化的变形方法将私有对象影藏起来，做到相对安全
        # 变形的方式是通过 _类名__私有变量名，这儿变形之后的名字是 _User__birthday
        # 变形规则可以解决子类和父类私有属性重名问题
        self.__birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2019 - self.__birthday.year

class Student(User):
    def __init__(self, birthday):
        # 子类变形之后的名字为: _Student__birthday
        # 这样就解决了重名问题
        self.__birthday = birthday

if __name__ == '__main__':
    user = User(Date(1990, 2, 1))
    # 将birthday隐藏
    # print(user.__birthday)
    print(user._User__birthday)
    print(user.get_age())