from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def show(self):
        pass


class Square(Shape):
    def show(self):
        print("square has four sides")


class Circle(Shape):
    def show(self):
        print("circle has circle shape")


obj = Square()
obj.show()
obj2 = Circle()
obj2.show()
