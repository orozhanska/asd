# class Node:
#     def __init__(self, data = None):
#         self.data = data
#         self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise Exception("Queue is empty. Cannot dequeue")
        else:
            removed = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.size -= 1
        return removed

    def is_empty(self):
        return self.front is None


    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty. Cannot peek")
        return self.front.data

    def size(self):
        return self.size

    def __str__(self):
        res = "Queue ["
        current_node =self.front
        while current_node is not None:
            res += current_node.data
            if current_node.next is not None:
                res += ", "
            current_node = current_node.next
        return res + "]"


# check cases

# myqueue = Queue()
# myqueue.enqueue("Nataly")
# myqueue.enqueue("Olesia")
# myqueue.enqueue("Halyna")
# print(myqueue)
# print(myqueue.size)
# print(myqueue.peek())
# myqueue.dequeue()
# myqueue.dequeue()
# myqueue.dequeue()
# print(myqueue)
# print(myqueue.size)
# print(myqueue.peek())
#

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # 1 <-> 2 <-> 3 <-> 4
    # delete(2)
    # delete(1)
    # 1 <-> 2
    # delete(2)
    # 1
    # delete(1)
    def delete(self, data):
        if self.head is None:
            raise Exception("List is empty")
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node == self.head:
                    if self.head.next is not None:
                        self.head = current_node.next
                        self.head.prev = None
                    else:
                        self.head = self.tail = None
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    self.tail.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
            current_node = current_node.next


    def display_forward(self):
        if self.head is None:
            print("List is empty")
        else:
            print("List forward is ")
            current_node = self.head
            while current_node is not None:
                if current_node == self.tail:
                    print(current_node.data)
                else:
                    print(current_node.data, end = " <--> ")
                current_node = current_node.next


    def display_backward(self):
        if self.tail is None:
            print("Error! List is empty")
        else:
            print("List backward is ")
            current_node = self.tail
            while current_node is not None:
                if current_node == self.head:
                    print(current_node.data)
                else:
                    print(current_node.data, end = " <--> ")
                current_node = current_node.prev
#
# mylist = DoublyLinkedList()
# mylist.display_forward()
# mylist.append("hello")
# mylist.append("world")
# mylist.append("and")
# mylist.append("OMG")
# mylist.display_forward()
# mylist.display_backward()
# mylist.prepend("hell")
# mylist.display_forward()
# mylist.delete("hell")
# mylist.delete("OMG")
#
# mylist.display_backward()
# mylist.delete("world")
# mylist.delete("and")
# mylist.delete("hello")
# mylist.display_forward()