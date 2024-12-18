things_weight = [1, 17, 5, 10, 13, 7, 8, 3, 4, 9, 12]
max_weight = 20 
counter = 0
max_optimal = []
def knapsack(element_position, current_weight, current_things):
    if current_weight > max_weight:
        return 
    global max_optimal

    if len(current_things) + len(things_weight) - element_position < len(max_optimal):
        return
    
    if element_position == len(things_weight):
        global counter 
        counter += 1
        print("Knapsack:", current_weight, current_things)

        if len(current_things) > len(max_optimal):
            max_optimal = current_things.copy()

        return
    
    knapsack(element_position + 1, current_weight, current_things)
    
    new_weight = current_weight + things_weight[element_position]
    new_things = current_things + [element_position]  # Create a new list instead of modifying in place
    knapsack(element_position + 1, new_weight, new_things)

current_things = []
knapsack(0, 0, current_things)
print(counter, "times")
print(max_optimal)
