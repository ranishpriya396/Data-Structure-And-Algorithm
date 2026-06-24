class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
        
    def appending(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else : 
            current = self.head
            while current.next is not None:
                current = current.next 
            current = new_node 
                
    def traversal(self):
        
        if self.head is None:
            print("SLL is empty")
        else : 
            current = self.head
            while current is not None:
                print(current.val , end = " ")
                current = current.next

sll = Sll()
node1 =sll.appending(1)
node2 = sll.appending(1)
node3 = sll.appending(1)
node4 = sll.appending(1)
node5 = sll.appending(1)

sll.traversal()
