# Linked list examples
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position")
            return
        
        # Insert at beginning
        if position == 1:
            self.insert_at_beginning(data)
            return

        # Traverse to (position-1)
        current_node = self.head
        current_position = 1
        while current_node is not None and current_position < position - 1:
            current_node = current_node.next
            current_position += 1

        if current_node is None:
            print("Position out of range")
            return

        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_at_position(self, position):
        if position <= 0:
            print("Invalid position")
            return
        
        if self.head is None:
            print("List is empty")
            return

        # Delete the head
        if position == 1:
            self.head = self.head.next
            return

        current_node = self.head
        current_position = 1
        while current_node.next is not None and current_position < position - 1:
            current_node = current_node.next
            current_position += 1

        if current_node.next is None:
            print("Position out of range")
            return

        current_node.next = current_node.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    #this is node at end
    # 1.list is empty
    # 2.list has one node
    # 3.list  has more then one node

    def insert_at_end(self, data):
        new_node = Node(data)
        #when list is empty
        if(self.head is None):
            self.head = new_node
            return

        #2.list has one node
        if(self.head.next is None):
            self.head.next = new_node
            return

        #list has more than one node
        current_node = self.head
        while(current_node.next is not None):
            current_node = current_node.next
        current_node.next = new_node

    def delete_at_beginning(self):
        #list is empty
        if(self.head ==None):
            return
        
        #list has one node
        if(self.head.next == None):
            self.head = None
            return
        
        #listnhas 2 or more nodes
        self.head = self.head.next

    def delete_at_end(self):
        #list is empty
        if(self.head == None):
            return
        #one node
        if(slef.head.next == None):
            self.head = None
            return
        #2 or more list
        current_node = self .head
        while(current_node.next.next != None):
            current_node = current_node.next
            current_node.next = None
        
def delete_operations(linked_list: SinglyLinkedList):
    linked_list.delete_at_beginning()
    linked_list.delete_at_end()

    linked_list.insert_at_beginning()
    linked_list.delete_at_beginning()

    linked_list.insert_at_end()
    linked_list.delete_at_end()
       
    


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(30)

    print("Initial list:")
    linked_list.display()

    linked_list.insert_at_position(15, 2)
    print("\nAfter inserting 15 at position 2:")
    linked_list.display()

    linked_list.delete_at_position(3)
    print("\nAfter deleting node at position 3:")
    linked_list.display()

    linked_list.delete_at_position()
    linked_list.display()
