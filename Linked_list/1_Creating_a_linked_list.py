class Node :
    def __init__(self,val):
        self.val = val 
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
print(node1.val, node1.next)
print(node2.val, node2.next)
print(node3.val, node3.next)
