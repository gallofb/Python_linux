#通过元类来设置数据库
import numbers

class IntField:
    def __init__(self,min_value = None,max_value = None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        if min_value is not None:
            if not isinstance(min_value,numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be posttive int")

    def __get__(self, instance, value):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("min_value need")
        if value < 0:
            raise ValueError("positive value need")
        self._value = value

class CharField:
    def __init__(self,db_column,value=None,max_length=None):
        self._value = value
        self.db_column = db_column
        self.max_length = max_length
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("min_value need")
        if len(value) < self.max_length:
            raise ValueError("positive value need")
        self._value = value

class ModelMeteClass(type):
    def __new__(cls,name,base,attrs, **kwargs):
        for key,value in attrs.items():
            pass

class User(metaclass=ModelMeteClass):
    name = CharField(db_column="",max_lenget=10)
    age = IntField(db_column="",min_value=0,max_value=100)
    class Meta:
        db_table = "user"

if __name__ == '__main__':
    pass
