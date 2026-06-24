def delete_the_node(self,val):
    temp = self.head
    if temp.val == val :
        self.head = temp.neaxxt
        return 
    else:

        prev = None 
        while temp.next is not None :
            if temp.val == val :
                prev.next = temp.next 
                break 
            prev = temp   
    