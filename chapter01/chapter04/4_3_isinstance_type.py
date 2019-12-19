# is 判断两个对象是不是一个对象你，即id是否相同
# == 判断值是否相等
# isinstance 判断第二个参数对象实例是否在第二个参数对象的继承链里面
#       Return whether an object is an instance of a class or of a subclass thereof.

class A():

class B(A):
    pass

print(isinstance(B, B))
print(isinstance(B, A))

b = B()

# 判断继承关系
print(isinstance(b, B))
print(isinstance(b, A))

# 判断id
print(type(b) is B)
print(type(b) is A)
# 判断值
print(type(b) == B)
