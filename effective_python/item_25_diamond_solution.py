from pprint import pprint

class myBaseClass(object):
    def __init__(self, value):
        self.value = value

class TimesFive(myBaseClass):
    def __init__(self, value):
        super(TimesFive, self).__init__(value)
        self.value *= 5

class PlusTwo(myBaseClass):
    def __init__(self, value):
        super(PlusTwo, self).__init__(value)
        self.value += 2

class ThisWay(PlusTwo, TimesFive):
    def __init__(self, value):
        super(ThisWay, self).__init__(value)

bar = ThisWay(5)
print("First ordering is ", bar.value)

pprint(ThisWay.mro())
