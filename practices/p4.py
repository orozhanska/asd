class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# add_back(data)  - add something in the end, after last el
# add_front(data) -  adds before "Head", before 0 el
# ideally add(data, index)
# find(data) -> returns Node or None
# remove(removes the Node with node.data == data or throw exceptions)
# size() -> returns size (amount of nodes)
# is_empty()

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> none
    # add winth ind = 0
    # new_node -? 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> none
    # add with index = 3
    # 0 -> 1 -> 2 -> new_node -> 3 -> 4 -> 5 -> 6 -> none
    def add_front(self, data):
        new_node = Node (data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1 
    
    def add_back(self, data):
        new_node = Node(data)
        current_node = self.head
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1
        
    def is_empty(self):
        return self.head is None
    
    def get_size(self):
        return self.size
    
    def remove_front(self):
        if self.head is None:
            raise Exception("Something bad")
        self.head = self.head.next
        self.size -= 1
    
    def get_front_data(self):
        if self.head is None:
            raise Exception("Very bad")
        
        return self.head.data
    
    def __str__(self):
        res = "LinkedList["
        current_node = self.head
        while current_node is not None:
            res += current_node.data
            if current_node.next is not None:
                res += ", "
            current_node = current_node.next
        return res + "]"

    def add(self, data, index):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node # data, None pointer
            if index != 0:
                raise Exception("Something bad")
        else:
            # index -> find the node before which we shpuld add new node
            counter = 0
            current_node = self.head
            while counter < index:
                counter += 1
                current_node = current_node.next
            

ll = LinkedList()
ll.add_back("Artem")
ll.add_back("Mariia")
ll.add_front("Slava")
ll.add_front("Sviata")
ll.add_back("Me()")
print(ll.is_empty())
print(ll.get_front_data())
print(ll)
print(ll.get_size())
ll.remove_front()
print(ll)


### Parentheses Balance

# 1st option
# n = int(input())
# lines = []
# for n in range(n):
#     par = input()
#     lines.append(par)

# def check_par(line):
#     opened_dynamic = []
#     for x in line:
#         if x == "(" or x == "[":
#             opened_dynamic.append(x)
#         else:
#             if not opened_dynamic:
#                 return "No"
#             elif (x == "]" and opened_dynamic[-1] == "[") or (x == ")" and opened_dynamic[-1] == "("):
#                 opened_dynamic.pop()
#             else:
#                 return "No"
#     return "Yes" if not opened_dynamic else "No"
    
# for par in lines:
#     print(check_par(par))

# 2nd option
# n = int(input())
# lines = []
# for _ in range(n):
#     par = input().strip()
#     lines.append(par)

# def check_par(line):
#     stack = []
#     matching = {')': '(', ']': '['}
    
#     for par in line:
#         if par in "([": 
#             stack.append(par)
#         elif par in ")]": 
#             if stack == [] or stack[-1] != matching[par]:
#                 return "No"
#             stack.pop()
    
#     return "Yes" if not stack else "No"
    
# for par in lines:
#     print(check_par(par))