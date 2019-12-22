# list, dict参数参入函数，会被修改的
# 尽量不要将list, dict作为参数或默认参数,或要格外小心
def add(a, b):
    a += b
    return a

class Company():
    def __init__(self, company, stuffs=[]):
        self.company = company
        self.stuffs = stuffs
    def add(self, stuffs):
        self.stuffs.append(stuffs)
    def remove(self, stuffs):
        self.stuffs.remove(stuffs)

if __name__ == '__main__':
    a = 1
    b = 2
    c = add(a, b)
    print(c)
    print(a)
    print(b)

    a = [1, 2]
    b = [3, 4]
    c = add(a, b)
    print(c)
    print(a)
    print(b)

    a = (1, 2)
    b = (3, 4)
    c = add(a, b)
    print(c)
    print(a)
    print(b)

    company1 = Company('Ingenic', ['Justin', 'Bob'])
    company1.add('Tom')
    company1.remove('Justin')
    print(company1.stuffs)

    # 原因: company2 和company3共用了对象初始化时默认参数[]
    company2 = Company('Baidu')
    company2.add('Lily')
    print(company2.stuffs)

    print(Company.__init__.__defaults__)

    company3 = Company('Ali')
    company3.add('Mick')
    print(company2.stuffs)
    print(company3.stuffs)

    print(company2.stuffs is company3.stuffs)
