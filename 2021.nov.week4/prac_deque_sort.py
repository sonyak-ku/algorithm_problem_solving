from collections import deque

a = [4, 5, 6, 1, 2, 4]

d = deque(a)

d = sorted(d, key= lambda x: x)

print(list(d))