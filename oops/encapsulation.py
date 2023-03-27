class A:
    _a = 10
    __b = 20

    def show(self):
        print("a=", self._a)
        print("b=", self.__b)


obj = A()
obj.show()
print("outside os class", obj._a)
