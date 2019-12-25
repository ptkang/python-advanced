# 需求
import numbers

class Filed():
    pass

class IntField(Filed):
    # 数据描述符
    def __init__(self, db_column, min_value=None, max_value=None):
        # self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value

        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError('min_value must be Integral')
            elif min_value < 0:
                raise ValueError('min_value must be positive Integral')

        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError('max_value must be Integral')
            elif max_value < 0:
                raise ValueError('max_value must be positive Integral')

        if self.min_value is not None and self.max_value is not None:
            if min_value > max_value:
                raise ValueError('min_value must less than max_value')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('Integral value need')
        if self.min_value is not None and self.max_value is not None:
            if value < self.min_value or value > self.max_value:
                raise ValueError('value must between min_value(%d) and max_value(%d)'%(self.min_value, self.max_value))
        self._value = value

class CharField(Filed):
    # 数据描述符
    def __init__(self, db_column, max_length=None):
        # self._value = None
        self.db_column = db_column
        self.max_lenght = max_length
        if max_length is None:
            raise ValueError('you must specify max_length ')

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('str value need')
        if len(value) > self.max_lenght:
            raise ValueError('len(%s)=%d must less than max_length(%d)'% (value, len(value), self.max_lenght))
        self._value = value

class ModelMetaClass(type):
    def __new__(cls, name, base, attrs, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, base, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Filed):
                fields[key] = value
        attrs_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, 'db_table', None)
            if table is not None:
                db_table = table
        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(cls, name, base, attrs, **kwargs)

class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()
    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            value = getattr(self, db_column, None)
            fields.append(db_column)
            values.append(str(value))
        sql = "insert {db_table}({fields}) value({values})".format(db_table=self._meta['db_table'], fields=','.join(fields), values=','.join(values))
        print(sql)

class User(BaseModel):
    # 类于字段相关联
    name =  CharField(db_column='name', max_length=10)
    age = IntField(db_column='age', min_value=0, max_value=100)

    # 类于表相关联
    class Meta():
        db_table = 'user'

if __name__ == '__main__':
    user = User(name='Bobby', age=28)
    # user.name = 'Bobby'
    # user.age = 28
    user.save()