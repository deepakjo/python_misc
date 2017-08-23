
class myBaseClass(object):
    def __init__(self, value):
        self.value = value

class TimesFive(myBaseClass):
    def __init__(self, value):
        myBaseClass.__init__(self, value)
        self.value *= 5

class PlusTwo(myBaseClass):
    def __init__(self, value):
        myBaseClass.__init__(self, value)
        self.value += 2

class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)

bar = ThisWay(5)
print("First ordering is ", bar.value)

