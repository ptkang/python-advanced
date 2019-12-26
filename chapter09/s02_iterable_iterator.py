# 迭代器不支持切片，即迭代时才产生数据

from collections.abc import Iterator
# iter()函数首先寻找实例对象是否实现了__iter__函数，若没有，则会调用__getitem__函数来遍历实例对象，生成一个迭代器

class MyIterator(Iterator):
    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.iter_index = 0
    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            item = self.iter_list[self.iter_index]
        except IndexError:
            raise StopIteration
        self.iter_index += 1
        return item

class Company():
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return '|'.join(self.employee)

    def __len__(self):
        return len(self.employee)

    def __iter__(self):
        return MyIterator(self.employee)

if __name__ == '__main__':
    company = Company(['Tom', 'Bob', 'Sara'])
    for item in company:
        print(item)

    for item in company:
        print(item)
