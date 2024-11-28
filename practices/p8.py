nodes = ["Artem", "Maria", "Slava", "Olha", "Bohdan"]

# List of edges - undirected graph
edges = [
    ("Artem", "Maria"),
    ("Maria", "Slava"),
    ("Slava", "Olha"),
    ("Olha", "Bohdan"),
    ("Bohdan", "Artem")
]

# check if we have an edge between two nodes

for (name_1, name_2) in edges:
    if name_1 == "Artem" and name_2 == "Olha":
        print("Yes")
        break

    elif name_1 == "Olha" and name_2 == "Artem":
        print("Yes")
        break

# complexity is O(n of edges)

# OR sort - O (M log M ) and binary search O(log M)

# OR hashtable
# construct a hash table - time O(M) & space O(M) + extra (a lot of buckets)
# time for check - O (1)

# adjecency matrix
matrix = [
    [0,1,0,0,0], # artem 1
    [1,0,1,0,0], # maria 2
    [0,0,0,1,0], # Slava 3
    [0,0,0,0,1], # Olha
    [1,0,0,0,0] # Bohdan
]
# коли багато ребер ми можемо зберігати ті, між якими немає звʼязку
# undirected unweiighted graph

# adjacent list
# 0: [1,2]
# 1: [0,2]
# 2: [3]
# 3: [2, 4]
# 4: []
# (N, M) - the len of value is min of those
# hashtable (key=name, value = list of neighbours)
# value = arrray/linked list

#space - N + M
# M -  edges
# N - nodes
# V - set of vertices
# E - set of edges
# Load factor - It represents the ratio of the number of stored elements (n) 
# to the size of the hash table (N). In Python's dict implementation, 
# open addressing is used, and the load factor is enforced to be less than 2/3. 
# If the load factor exceeds this threshold, the hash table is resized 
# to maintain efficiency.

# hash table
# base = [_ _ _ _ _]
# ind = hash(x) % len(hash table))
# if collision happen  the bucket contains a Linkedlist
# count/len(basej = load_factor
# сенс перебудувати - щоб в комірці був в середньому один елемент
# час перебудови, ми проходимося по кожному елементі в масиві і рахуємоновий інд