n = int(input())

def get_minimum_sugar(p):
    k = p // 5
    while k >= 0:
        remain = p - k * 5
        if remain % 3 == 0:
            return k + remain // 3
        else:
            k = k - 1
    return -1

print(get_minimum_sugar(n))