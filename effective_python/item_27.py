
class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field

class MyOtherObject(object):
    def __init__(self, value):
        self.__private_field = value 

    def get_value(self):
        return self.__private_field 

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field

    @classmethod
    def get_class(cls, value):
        return cls(value)

bar = MyOtherObject(71)
assert MyOtherObject.get_private_field_of_instance(bar) == 71

class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
print(baz._MyParentObject__private_field)

print(baz.__dict__)
class MyBaseClass(object):
    def __init__(self, value):
        self.__value = value

class MyClass(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)

    def get_value(self):
        return str(self.__value)

class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)

foo = MyIntegerSubclass(5)
print(foo.get_value()) 
