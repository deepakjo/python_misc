class C:
    def foo(cls, y):
        print "classmethod", cls, y

    def abc(self, y):
        print "classmethod", 

    foo = classmethod(foo)

class E(C):
    def foo(cls, y):
        print "E.foo() called"
        C.foo(2)

    foo = classmethod(foo)

E.foo(1)
e = E()
e.foo(1)
e.abc(2)
