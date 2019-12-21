# contextlib是对with语句的一个优化
# 但contextlib.contextmanager必须修饰一个生成器,所以我们必须对生成器有一个好的了解
import contextlib

# @contextlib.contextmanager必须修饰一个生成器
@contextlib.contextmanager
def file_open(file_name):
    print('file open')
    # yield 之前的代码可以看做上下文管理器__enter__部分
    yield {'Justin'}
    # yield 之后的代码可以看做上下文管理器__exit__部分
    print('file end')

with file_open('abc_4_2.py') as f_opened:
    print(f_opened)
    print('file processing')