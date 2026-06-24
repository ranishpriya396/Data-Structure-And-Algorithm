class Node :
    def __init__(self,val):
        self.val = val 
        self.next = None 
    
class Sll :
    def __init__(self):
        self.head = None
    
    def appending(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
            
        current.next = new_node 
    def insert_at_postion(self,position , val):
        new_node = Node(val)
        if position == 0:
            new_node.next =self.head 
            self.head = new_node 
        else:
            current = self.head
            count = 0 
            while current.next is not None and count < position:
                prev_node = current
                current = current.next
                count+=1
            if count == position :
                prev_node.next = new_node
                new_node.next = current 
            else : 
                print("position out of bounds ")
    def delete_the_node(self,val):
        if self.head is None:
            print("sll is empty ")
            return 
        temp = self.head
        if temp.val == val :
            self.head = temp.next
            return 
        else:
            prev = None 
            while temp is not None :
                if temp.val == val :
                    prev.next = temp.next 
                    return
                prev = temp  
                temp = temp.next 
        
        
    def traversal(self):
        if self.head is None:
            print("Linked list is empty ")
        else :
            current = self.head
            while current is not  None:
                print(current.val , end = " ")
                current = current.next
            print()
                
        
sll = Sll()
node1 = sll.appending(9)
node2 = sll.appending(10)
node3 = sll.appending(11)
node4 = sll.appending(12)
node5 = sll.insert_at_postion(1,0)
print("Before Deletion:")
sll.traversal()

print("After Deleting 12:")
sll.delete_the_node(12) 
sll.traversal()