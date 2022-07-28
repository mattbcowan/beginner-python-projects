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

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0

        while itr:
            if itr.data == data_after:
                tmp = itr.next
                itr.next = Node(data_to_insert, tmp)
                break

            itr = itr.next
            count += 1

        if count >= self.get_length():
            raise Exception("Data does not exist")

    def remove_by_value(self, data):
        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return

            itr = itr.next

        if itr.next is None:
            raise Exception("Data does not exist")


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
