# __new__用来控制对象的生成过程
# __init__用来完善对象，添加属性和代码逻辑
# 如果__new__不返回对象，则不会调用__init__函数
class User():
    # 在生成User对象之前加逻辑
    def __new__(cls, *args, **kwargs):
        print('In new')
        return super().__new__(cls)

    def __init__(self, name):
        print('In init')
        self.name = name

if __name__ == '__main__':
    user = User('Bob')
    #user = User(name='Bob')
