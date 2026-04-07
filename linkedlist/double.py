class Node:
    def __init__(self, data):
        self.data = data
        self.pre = None
        self.next = None


class double_linked_list:
    def __init__(self):
        self.head = None

    def insertnode(self, data):
        new_node = Node(data)

        # case 1 : empty node
        if self.head is None:
            self.head = new_node
            return

        # case 2: two or more nodes
        new_node.next = self.head
        self.head.pre = new_node
        self.head = new_node
        return

    def insertat_end(self, data):
        new_node = Node(data)

        # empty list
        if self.head == None:
            self.head = new_node
            return

        # case 2 one node
        self.data = data
        self.head.next = new_node
        new_node.pre = self.head
        self.head = new_node
        return

        # case 3 2 or more nodes
        while new_node.next != None:
            new_node = new_node.next
            new_node.next = new_node

    def insert_at_specific_positionn(self, target_ele, data):
        if target_ele <= 0:
            print()
            return

        if self.head and self.head.next == None and target_ele > 1:
            print("invalid position")

        if target_ele == 1:
            self.insertnode(data)
            return

        current_position = 1
        current_node = self.head
        while current_node != None and target_ele > 2:
            current_position = current_position + 1
            current_node = current_node.next

        if current_node == None:
            print("invalid position")
            return

        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.pre = current_node

        # empty list
        if self.head == None and target_ele != 1:
            self.head = new_node
            return


def insert_atbegining_testcase(dlist: double_linked_list):
    dlist.insertnode(10)
    dlist.insertnode(20)


def insert_atend_testcase(dlist: double_linked_list):
    dlist.insertat_end(50)
    dlist.insertat_end(60)


def insert_atposition_test_case(dlist: double_linked_list):
    dlist.insert_at_specific_positionn(20, -1)
    dlist.insert_at_specific_positionn(80, 3)
    dlist.insert_at_specific_positionn(51, 9)
    dlist.insert_at_specific_positionn(58, 5)
    dlist.insert_at_specific_positionn(48, 2)
    dlist.insert_at_specific_positionn(45, 1)


if __name__ == "__main__":
    dlist = double_linked_list()
    # insert_atbegining_testcase(dlist)
    # insert_atend_testcase(dlist)
    insert_atposition_test_case(dlist)
