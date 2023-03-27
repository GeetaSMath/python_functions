# abstract class one or more abstract method
# we cant create object for abstract module
# abs module work with abstract
# we can use @abstract
#hide the implementation
# when action common implementation is different we will use
from abc import ABC, abstractmethod


class Car(ABC):
    def show(self):
        print("car has four wheels")

    @abstractmethod
    def speed(self):
        pass


class Maruti(Car):
    def speed(self):
        print("speed of maruti car 100Km/H")


class Suzuki(Car):
    def speed(self):
        print("speed of suzuki car 70Km/H")


obj = Maruti()
obj.show()
obj.speed()
obj2 = Suzuki()
obj2.show()
obj2.speed()
