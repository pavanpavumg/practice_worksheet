class linkedlist():
    def __init__(self, head, null):
        self.prev = null
        self.curr = head
        self.next = null

        while curr != null:
            curr.next = self.prev
           
            self.prev = curr
        
            curr = next

        return self.prev
linkedlist()



    
        
