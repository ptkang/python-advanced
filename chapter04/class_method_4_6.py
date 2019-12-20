# 静态方法，类方法和实例方法及其参数
class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法self
    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year, month=self.month, day=self.day)

    # 静态方法
    # 缺点：静态方法中使用了依赖类名Date的对象，若类名修改，则静态方法也得修改
    # 这个缺点应该有类方法来克服
    @staticmethod
    def parse_from_string(date_string):
        year, month, day = tuple(date_string.split('-'))
        return Date(int(year), int(month), int(day))

    # 类方法 cls：用来克服静态方法使用类名的问题
    @classmethod
    def from_string(cls, date_string):
        year, month, day = tuple(date_string.split('-'))
        return cls(int(year), int(month), int(day))

    # 静态方法：用于和类、实例无关的辅助操作，克服了实例或类方法引入多余变量如self, cls的冗余
    @staticmethod
    def valid_date_string(date_string):
        year, month, day = tuple(date_string.split('-'))
        if (int(year) > 0) and (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            return True
        else:
            return False

if __name__ == '__main__':
    my_day = Date(2018, 12, 11)
    print(my_day)

    # 用静态方法实现
    my_day = Date.parse_from_string('2018-12-21')
    print(my_day)

    # 用类方法实现
    my_day = Date.from_string('2018-12-21')
    print(my_day)

    # 用静态方法实现
    print(Date.valid_date_string('2019-13-31'))

