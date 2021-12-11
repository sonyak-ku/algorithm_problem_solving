def fib_finder(n):
    # Write your code here
    if n == 1:
        return 0
    if n == 2:
        return 1

    pre_2, pre_1 = 0, 1

    for i in range(3, n):
        pre_2, pre_1 = pre_1, pre_2 + pre_1

    return pre_2 + pre_1


print(fib_finder(1000)) # 개빠름
