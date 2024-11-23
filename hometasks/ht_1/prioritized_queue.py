commands = []
queue_dict = {}
queue = []

def add_to_queue(i, priority):
    queue_dict[i] = priority
    queue.append((i, priority))

def pop(index):
    queue.sort(reverse=True, key=lambda x: x[1])  #desc as in the example
    popped = queue.pop(index)
    i, priority = popped[0], popped[1]
    del queue_dict[i]
    return i, priority

def change(i, new_priority):
    if i in queue_dict.keys():
        old_priority = queue_dict[i]
        queue.remove((i, old_priority))
    queue_dict[i] = new_priority
    queue.append((i, new_priority))

    
while True:
    try:
        command = input()
        commands.append(command)
    except EOFError:
        break
for command in commands:
    command = command.split()
    if command[0] == "ADD":
        add_to_queue(command[1], int(command[2]))
    elif command[0] == "CHANGE":
        change(command[1], int(command[2]))
    else:
        res = pop(0)
        print(f"{res[0]} {res[1]}")