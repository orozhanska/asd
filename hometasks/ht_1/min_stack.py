n, a, b, c, x = map(int, input().split())
stack = []
min_stack = []
res = 0
for _ in range(0, n):
    x = ((a*x**2 + b*x + c)//100) % 10**6
    if x % 5 < 2:
        if stack == []:
            continue
        else:
            stack.pop()
            min_stack.pop()
    else:
        stack.append(x)
        if min_stack:
            min_stack.append(min(x, min_stack[-1]))
        else:
            min_stack.append(x)
    if min_stack:
        res += min_stack[-1]

print(res)