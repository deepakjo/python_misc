class C:
    def foo(cls, y):
        print "classmethod", cls, y

    foo = classmethod(foo)

C.foo(1)
c = C()
c.foo(1)
