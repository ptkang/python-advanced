# 属性：定义在类或实例，即对象里面的变量和方法都称为属性
# 类和实例属性的查找顺序MRO(method research oder)
# python3 MRO使用C3的算法
# DFS: 深度优先查找方法 (deep first research method)
# BFS: 广度优先查找方法
# C3：
# 类有__mro__属性，实例没有__mro__属性

# 新式类

# C3算法菱形继承
# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
#            D
#           / \
#          B   C
#           \  /
#             A
class D():
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)

# C3算法U型继承
# (<class '__main__.H'>, <class '__main__.I'>, <class '__main__.K'>, <class '__main__.J'>, <class '__main__.M'>, <class 'object'>)
#          K   M
#          |   |
#          I   J
#           \  /
#             H
class M():
    pass

class K():
    pass

class J(M):
    pass

class I(K):
    pass

class H(I, J):
    pass

print(H.__mro__)
