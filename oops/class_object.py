class A:
    # class is blue print of creating objects
    # default constructor so no need to print age again nd again
    # we can create obj
    #its method
    #object is instance class
    def __init__(self):
        age = 10
        print(age)


obj = A()


# example
#paramiter construction
class User:
    def __init__(self, name, id):
        print(name, " ", id)


obj = User("geeta", 13)


# contstructor
# default constructor and parameter constructor
# example for default constructor
class Employee:
    employee_name = "geeta"
    employee_address = "banglore"

    def __init__(self):
        print(self.employee_name)

    def show(self):
        print(self.employee_address)


employee_obj = Employee()
employee_obj.show()


class User:
    age = 10

    def __init__(self):
        name = "geeta"
        print(name, self.age)


obj2 = User()
