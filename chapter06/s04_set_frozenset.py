# set集合， frozenset(不可变集合) 无需，不重复
# set实际顺序和我们添加的顺序不一样
# set接收一个iterable对象
# set性能很高，时间复杂度为O(1)
s = set('abcdee')
print(s)
s = set(['a', 'b', 'c', 'd', 'e'])
print(s)
s = {'a', 'b', 'c', 'd', 'e'}
print(s)
s.add('f')
print(s)

# frozenset不可变集合使得其可以作为dict的key
s = frozenset('abcdee')
print(s)

# update，将两个集合合并
s = set('abcdee')
another_set = set('defg')
s.update(another_set)
print(s)

# difference 求集合的差集: s - another_set = diff_set
diff_set = s.difference(another_set)
print(diff_set)
minus_set = s - another_set
print(minus_set)

# 集合里面三种运算： 联合 | ， 交集 &， 差集 -

if 'c' in s:
    print(True)

print(diff_set.issubset(s))
