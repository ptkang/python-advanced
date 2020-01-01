def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + '销量: ', x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

if __name__ == '__main__':
    gen = sales_sum('bobby牌电脑')
    gen.send(None)
    gen.send(1500)
    gen.send(900)
    gen.send(2100)
    try:
        gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)
