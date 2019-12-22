# ByteString: 处理已排序序列的查找模块，用来维持已排序的升序序列
# 二分查找

import bisect

inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)
print(bisect.bisect_left(inter_list, 3))
print(bisect.bisect_left(inter_list, 4))
print(inter_list)
