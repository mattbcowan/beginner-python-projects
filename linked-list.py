class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        linked_list_string = ""

        while itr:
            linked_list_string += str(itr.data) + "-->"
            itr = itr.next

        print(linked_list_string)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(79)
    ll.insert_at_end(1)
    ll.insert_at_end(9876)
    ll.print()
