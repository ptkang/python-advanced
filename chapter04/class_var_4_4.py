# 类变量和实例变量
class A:
    # 类变量
    aa = 1
    def __init__(self, x, y):
        # self是类的实例
        # x, y 前面加self，即为实例变量
        self.x = x
        self.y = y
a = A(2, 3)
# a.aa能访问是因为a先查找自身实例变量aa，若没找到，则向上在所在类里面查找类变量aa
print(a.x, a.y, a.aa, A.aa)

# 类变量必须通过类名.变量名来修改
A.aa = 11
# a.aa = 255 实质为动态的给实例a增加了实例变量aa
a.aa = 255
print(a.x, a.y, a.aa, A.aa)

b = A(4, 5)
print(b.x, b.y, b.aa, A.aa)
