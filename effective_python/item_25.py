
class myBaseClass(object):
    def __init__(self, value):
        self.value = value

class myChildClass(myBaseClass):
    def __init__(self):
        myBaseClass.__init__(self)

class TimesTwo(object):
    def __init__(self):
        self.value *= 2

class PlusFive(object):
    def __init__(self):
        self.value += 5

class OneWay(myBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        myBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

class AnotherWay(myBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        myBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

bar = OneWay(5)
print("First ordering is ", bar.value)

foo = AnotherWay(5)
print("Second ordering is ", foo.value)
