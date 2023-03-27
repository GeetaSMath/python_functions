# overriding in parent and child has same same name and signature
# object same behavior will be different

# parent class
class A:
    def disp(self):
        print("this is parent class method")


# class B is inheriting parent class
# child class
# solid
class B(A):
    def disp(self):
        super().disp()
        print("this is child class method")

obj=B()
obj.disp()
