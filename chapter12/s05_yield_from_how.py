# pep 380
# 1. RESULT = yield from EXPR 可以简化成下面这样
# 一些说明
'''
_i: 子生成器，同时也是一个迭代器
_y: 子生成器生产的值
_r: yield from 表达式最终的值
_s: 调用方通过send()发送的值
_e: 异常对象
'''

_i = iter(EXPR)     # EXPR是一个可迭代对象, _i是生成器
try:
    _y = next(_i)   # 预激活生成器，把产出的第一个值存在_y中
except StopIteration as _e:
    _r = _e.value   # 如果抛出了StopIteration的异常，那么就将异常对象的返回值value值赋给_r
else:
    while 1:    # 尝试执行这个循环你，委托生成器会阻塞
        _s = yield _y   # 生产子生成器的值，等待调用方send()的值，并将调用方发过来的值赋给_s
        try:
            _y = _i.send(_s)    # 转发_s，并且尝试向下执行
        except StopIteration as _e:
            _r = _e.value       # 如果子生成器抛出异常，那么就获取异常的返回值value并赋给_r
            break
RESULT = _r     # _r就是整个yield from表达式返回的值

'''
1. 子生成器可能只是一个迭代器，并不是作为一个协程的生成器，所以它不支持.throw()或.close()方法
2. 如果子生成器支持.throw()和.close()方法，但是在子生成器内部，这两个方法都会抛出异常
3. 调用方让子生成器自己抛出异常
4. 当调用方使用next()或者.send(None)时，都要在子生成器上调用next()函数，当调用方使用.send()发送非None的值时，
    才调用子生成器的.send()的方法
'''
_i = iter(EXRP)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break
RESULT = _r

'''
总结yield from的关键点：
1. 子生成器生产的值，都是直接给调用方的；调用方通过.send()发送的值都是直接传递给子生成器的；如果发送的是None,会调用子生成器的next()方法，
    如果不是None,会调用子生成器的send()方法；
2. 子生成器退出的时候，最后的return EXEP，会触发一个StopIteration(EXEP)异常；
3. yield from 表达式的值，是子生成器终止时，传递给StopIteration异常的第一个参数；
4. 如果调用的时候出现StopIteration异常，委托生成器会恢复运行，同时其他的异常会向上“冒泡”；
5. 传入委托生成器的异常里，除了GeneratorExit外，其他的所有异常全部传递给子生成器的.throw()方法，如果调用throw()的时候，出现了
    StopIteration异常，那么久恢复委托生成器的运行，其他的异常全部向上“冒泡”
6. 如果在委托生成器上调用.close()或传入GeneratorExit异常，会调用子生成器的.close()方法，没有的话就不调用；如果调用.close()方法
    的时候抛出了异常，那么就向上“冒泡"，否则委托生成器会抛出GeneratorExit异常
'''
