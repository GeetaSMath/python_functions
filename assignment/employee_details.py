# "In the class Employee, implement the instance attributes as firstname, lastname and salary.
# Create the method from_string() which parses a string containing
# these attributes and assigns them to the correct properties. Properties will be separated by a dash.
# Examples
# emp1 = Employee(""Mary"", ""Sue"", 60000)
# emp2 = Employee.from_string(""John-Smith-55000"")
# emp1.firstname ➞ ""Mary""
# emp1.salary ➞ 60000
# emp2.firstname ➞ ""John""
# emp2.salary ➞ 55000"

class Employee:
    def __init__(self, emp_firstname, emp_lastname, emp_salary):
        self.emp_firstname = emp_firstname
        self.emp_lastname = emp_lastname
        self.emp_salary = emp_salary

    @classmethod
    def from_string(cls, string):
        emp_firstname, emp_lastname, emp_salary = string.split("-")
        return cls(emp_firstname, emp_lastname, emp_salary)


obj = Employee("Mary", "Sue", 60000)
obj2 = Employee.from_string("John-Smith-55000")

print(obj.emp_firstname)
print(obj.emp_salary)
