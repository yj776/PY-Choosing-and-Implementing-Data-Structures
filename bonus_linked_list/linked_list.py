# Write code for implementing a linked list below

class Node:
    def __init__ (self, val = None):
        self.val = val
        self.nxtval = None

class Link:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.val)
            printval = printval.nxtval

list1 = Link()
list1.headval = Node('Mon')
list2 = Node("Tue")
list3 = Node("Wed")

# Link first node to second node
list1.headval.nxtval = list2

# Link second node to third node
list2.nxtval = list3

list1.listprint()