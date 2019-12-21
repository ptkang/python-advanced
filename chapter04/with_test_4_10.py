# try, except, else, finally 语句
# with语句：为了简化try finally语句,称为上下文管理器协议
def exe_try():
    # try except finally
    try:
        print('Code Started')
        # fd = open('with_test.txt')
        fd = open('self_ex_4_8.py')
        print('1'*32)
        # NameError
        name
        print('2'*32)
        l = [1, 2, 3]
        # IndexError
        l[100]
        print('3'*32)
        d = {}
        # KeyError
        d[name]
        print('4'*32)
        return 1
    # 被检测的代码块抛出的异常有多种可能性，并且我们需要针对每一种异常类型都定制专门的处理逻辑
    # 定制什么类型异常，能捕获相应的异常，但是没有指定的异常的话还是会报错的
    except NameError as e:
        print('Name Error')
        return 2
    except IndexError as e:
        print('Index Error')
        return 3
    except KeyError as e:
        print('Key Error')
        return 4
    except Exception as e:
        print('万能异常:', e)
        return 5
    else:   # 在try块没有抛异常时会运行,即会在被检测的代码块没有发生异常时执行
        print('在被检测代码块没有发生异常时执行')
        return 6
    # 不管前面有没有运行，finally都会运行
    # finally用于释放资源
    finally:
        print('Finally, 不管被检测的代码块有没有发生异常都会执行，finally都会运行')
        fd.close()
        return 7
    return 8

# with语句:上下文管理器协议
class Sample():
    # 申请资源
    def __enter__(self):
        print('Enter')
        # return self必须要，不然会报：AttributeError: 'NoneType' object has no attribute 'do_somthing'
        return self
    # 释放资源
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')
    def do_somthing(self):
        print('Do Something')

if __name__ == '__main__':
    ret = exe_try()
    # 最后ret为7的原因是except NameError里面现将return 2压栈，后将finally里面的return 7压栈，最后出栈时将顶部的return 7先出站，所以ret 为7
    print(ret)
    with Sample() as sample:
        sample.do_somthing()
