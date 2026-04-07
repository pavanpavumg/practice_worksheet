class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular:
    def __init__(self):
        self.tail = None

    # insert node after tail
    def insertat_beginning(self, data):
        new_node = Node(data)
        # empty list
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
            return

        # insert after tail (at beginning)
        new_node.next = self.tail.next
        self.tail.next = new_node

    def insrt_at_tail(self, data):
        new_node = Node(data)

        # empty list
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
            return

        # insert after tail and make new node the tail
        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node

    def deleteat_beginning(self):
        if self.tail is None:
            print("list empty")
            return

        if self.tail.next == self.tail:
            self.tail = None
            return

        self.tail.next = self.tail.next.next

    def deletat_tail(self):
        # empty list
        if self.tail is None:
            return

        # one node
        if self.tail.next == self.tail:
            self.tail = None
            return

        # case 2 or more nodes
        new_tail = self.tail.next
        while new_tail.next != self.tail:
            new_tail = new_tail.next

        new_tail.next = self.tail.next
        self.tail = new_tail

    def printalnodes(self):
        # case1 list is empty
        if self.tail is None:
            print("list is empty")
            return

        current_node = self.tail.next
        while True:
            print(f"{current_node.data}-->", end=" ")

            if current_node == self.tail:
                print()
                return

            current_node = current_node.next

    def search_key(self, key):
        # case1 list is empty
        if self.tail is None:
            print("list is empty")
            return

        current_node = self.tail.next
        while True:
            if current_node.data == key:
                print("key in the list")
                return

            if current_node == self.tail:
                break

            current_node = current_node.next

        print("key is not present in the list")


def circuler_listtest(clist: Circular):
    clist.deleteat_beginning()
    clist.deletat_tail()

    # insert and delete
    clist.insertat_beginning(10)
    clist.deleteat_beginning()

    clist.insrt_at_tail(20)
    clist.deletat_tail()

    clist.insertat_beginning(10)
    clist.insertat_beginning(11)
    clist.insertat_beginning(12)

    clist.insrt_at_tail(13)
    clist.search_key(11)
    clist.printalnodes()


if __name__ == '__main__':
    clist = Circular()
    circuler_listtest(clist)
