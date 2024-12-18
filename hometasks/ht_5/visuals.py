# run this online as I was working on a corporate Mac
# https://python-fiddle.com/
import matplotlib.pyplot as plt
import datetime

MOD = 1000000007

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

def climb_stairs_memo_mod(n, memo={}):
    memo[0], memo[1] = 1, 1
    if n not in memo:
        memo[n] = (climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)) % MOD
    return memo[n]
    
def climb_stairs_iterative_array_mod(n):
    if n == 0 or n == 1:
        return 1
    memo = [0] * (n + 1)
    memo[0], memo[1] = 1, 1
    for i in range(2, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % MOD
    return memo[n]

def climb_stairs_iterative_vars_mod(n):
    if n == 0 or n == 1: # edge cases for optimization
        return 1
    var1, var2 = 1,1
    ways = 0
    for num in range(2, n+1):
        ways = (var1 + var2) % MOD
        # move the variables forward
        var1, var2 = var2, ways

    return ways

def measure_time(func, n):
    start_time = datetime.datetime.now()
    func(n)
    end_time = datetime.datetime.now()
    return (end_time - start_time).total_seconds()

# yep, this is GPT as well
def plot_performance():
    methods = {
        "Recursive": climb_stairs_recursive,
        "Recursive with Memoization": lambda n: climb_stairs_memo(n, memo={}),
        "Iterative with Array": climb_stairs_iterative_array,
        "Iterative with Variables": climb_stairs_iterative_vars,
        "Memoization with Modulo": lambda n: climb_stairs_memo_mod(n, memo={}),
        "Iterative Array with Modulo": climb_stairs_iterative_array_mod,
        "Iterative Vars with Modulo": climb_stairs_iterative_vars_mod
    }

    x_values = range(0, 40, 5)  # Values of N to test
    plt.figure(figsize=(12, 8))

    for method_name, method in methods.items():
        times = [measure_time(method, n) for n in x_values]
        plt.plot(x_values, times, label=method_name)

    plt.xlabel("N")
    plt.ylabel("Time (seconds)")
    plt.title("Performance")
    plt.legend()
    plt.grid()
    plt.show()

plot_performance()