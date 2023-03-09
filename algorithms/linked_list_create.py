class Node:
    #creation of node
    def __init__(self, data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->" ,end=" ")
                temp=temp.next

L=SingleLinkedList()
n=Node(10)
L.head=n
n1=Node(20)
L.head.next=n1
L.display()