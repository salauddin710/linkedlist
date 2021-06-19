class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None
  # traversing list
    def print_ll(self):
        if self.head is None:
            print("Linklist is empty")
        else:
            p = self.head
            while p is not None:
                print(p.data)
                p=p.ref

    def add_begining(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def delet_begin(self):
        if self.head is None:
            print("Linkedlist is empty, nothing to delete ")
        else:
            self.head = self.head.ref

    def delet_end(self):
        if self.head is None:
            print("Linkedlist is empty, nothing to delete ")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None


    def delet_by_value(self,a):
        if self.head is None:
            print("Can't delete empty linklist ")
        if a == self.head.data:
            self.head = self.head.ref
        n= self.head
        while n.ref is not None:
            if a == n.ref.data:
                break
            n = n.ref

        if n.ref is None:
            print("Node is not here")
        else:
            n.ref = n.ref.ref




list1 = Linkedlist()
list1.add_begining(10)
list1.add_end(50)
list1.add_begining(60)
# list1.delet_begin()
# list1.delet_end()
list1.delet_by_value(80)
list1.print_ll()

