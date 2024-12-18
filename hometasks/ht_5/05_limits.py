import datetime

# import sys

# sys.setrecursionlimit(25000) 

# Recursive Approach
# Time O(2^n) - for each step we have 2 operations - go back -1 and go back -2
# Space O(n) - the recursion is n-elements deep

def climb_stairs_recursive(n):
    if n == 0 or n == 1:
        return 1
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)

# Recursive with memoization
# Time O(n) - for each subproblem one operation is needed
# Space O(n) - the dictionary

def climb_stairs_memo(n, memo={}):
    memo[0], memo[1] = 1, 1
    if n not in memo:
        memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


# Iterative with Array
# Time O(n) - same as in the prev
# Space O(n) - same as in the prev

def climb_stairs_iterative_array(n):
    if n == 0 or n == 1: # edge cases for optimization
        return 1
    memo = [None] * (n+1)
    memo[0], memo[1] = 1, 1
    for ind in range(2, n+1):
        memo[ind] = memo[ind-1] + memo[ind-2]
    
    return memo[n]


# Iterative with Variables
# Time O(n) - same as in the prev
# Space O(1) - we store 2 variables O(2*1)

def climb_stairs_iterative_vars(n):
    if n == 0 or n == 1: # edge cases for optimization
        return 1
    var1, var2 = 1,1
    ways = 0
    for num in range(2, n+1):
        ways = var1 + var2
        # move the variables forward
        var1, var2 = var2, ways

    return ways
    





def Sanity_Test():
    results = {
        0: 1,
        1: 1,
        2: 2,
        3: 3,
        4: 5,
        5: 8,
        6: 13,
        7: 21,
        8: 34,
        9: 55,
        10: 89,
        15: 987,
        20: 10946,
        25: 121393,
    }
    for func in [climb_stairs_recursive, climb_stairs_memo, climb_stairs_iterative_array, climb_stairs_iterative_vars]:
        for n, expected in results.items():
            actual = func(n)
            assert actual == expected, f"Expected {expected}, but got {actual} for n={n} using {func.__name__}"

    print(f"\033[92mSanity test passed\033[0m")


# TODO: you can modify this function, it's just a helper for you
def Performance_Test():
    for func in [climb_stairs_recursive, climb_stairs_memo, climb_stairs_iterative_array, climb_stairs_iterative_vars]:
        start_time = datetime.datetime.now()
        res = func(25)
        print(res)
        end_time = datetime.datetime.now()
        print(f"{func.__name__} took: {end_time - start_time}")
    print(f"\033[92mPerformance test passed\033[0m")

Sanity_Test()
Performance_Test()

# the next code is NOT mine, it's written by my bro GPT (though I understand it). 
# i like this implementation but I wouldn't write it on my own as i am a bit stupid. plus, i have 1 hour till the deadline


def measure_performance(func, method_name, max_time=5):
    """
    Measure the maximum N that can be computed by the function within max_time seconds.
    Handles RecursionError and ValueError gracefully.
    """
    n = 1
    step = 1
    max_n_time = 0
    max_n_recursion = 0
    max_n_value = 0

    while True:
        try:
            start_time = datetime.datetime.now()
            func(n)
            elapsed_time = (datetime.datetime.now() - start_time).total_seconds()

            if elapsed_time > max_time:
                max_n_time = n - step
                break

            if elapsed_time < 1:
                n += step
                step *= 2  # Exponential growth for faster exploration
            else:
                step = max(1, step // 2)  # Narrow down step size
                n += step

        except RecursionError:
            max_n_recursion = n - step
            print(f"RecursionError encountered for {method_name} at n = {n}")
            break
        except ValueError:
            max_n_value = n - step
            print(f"ValueError encountered for {method_name} at n = {n}")
            break

    return {
        "max_n_time": max_n_time,
        "max_n_recursion": max_n_recursion,
        "max_n_value": max_n_value,
    }


# Measure maximum n for each function
def evaluate_methods():
    methods = [
        ("Recursive with Memoization", lambda n: climb_stairs_memo(n, memo={})),
        ("Iterative with Array", climb_stairs_iterative_array),
        ("Iterative with Variables", climb_stairs_iterative_vars),
    ]

    results = {}
    for name, func in methods:
        print(f"Evaluating {name}...")
        result = measure_performance(func, name)
        results[name] = result
        print(f"{name}: {result}")
    return results

# Call the evaluation
performance_results = evaluate_methods()



