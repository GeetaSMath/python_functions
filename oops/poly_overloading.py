#having same function and its behavior will same
class A:
    def show(self):
        print("welcome1")

    def show(self, firstname=''):
        print("welcome2", firstname)

    def show(self, firstname='', lastname=''):
        print("welcome3", firstname, lastname)


obj = A()
obj.show()
obj.show('geeta')
obj.show('geeta', 'math')
