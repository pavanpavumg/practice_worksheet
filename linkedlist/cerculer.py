class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

    class Circular:
        def __init__(self):
            self.hesd = None

        #insert node after tail
        
        def insertat_beginning(self,data):
            new_node = Node(data)
            #empty list
            if(self.head == None):
                self.tail = new_node
                new_node.next = new_node
                return

            #single node
            new_node.next = self.tail.next
            self.tail.next = new_node


        def insrt_at_tail(self,data):
            new_node = Node(data)

            #empty list
            if(self.tail == None):
                self.tail = new_node
                new_node.next = new_node
                return
            #single node
            if(self.tail.next == self.tail):
                self.tail.next = new_node
                new_node.next = self.tail
                self.tail = new_node

        def deleteat_beginning(self, data):
            if(self.tail == None):
                print("list emtpy")
                return
        
            if(self.tail.next == self.tail):
                self.tail = None
                return
            self.tail.next = self.tail.next.next

    def deletat_tail(self,data):
        if(self.tail == None):
            return
        
        #emtpy list
        if(self.tail.next == self.tail):
            self.tail = None 
            return
        


               

