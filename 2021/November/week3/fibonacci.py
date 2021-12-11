mim = {
    1: 0,
    2: 1
}


def fib_finder(n, memo: dict):
    # Write your code here
    
    if memo.get(n, -1) == -1:  # not in dic
        memo[n] = fib_finder(n - 1, memo) + fib_finder(n - 2, memo)
        print(memo)
        return memo[n]
    else:  # in dic
        return memo[n]



fib_finder(10, mim)
