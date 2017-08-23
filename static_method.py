class C:
    def foo(self, x, y):
        print ("staticmethod", x, y)


#C.foo(1, 2)
c = C()
c.foo(1, 2)
