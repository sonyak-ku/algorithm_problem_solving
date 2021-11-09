from functools import reduce
a = 2
b = 5
# print(a + b)
# print('git push check')
k = [[3, 2], [4, 2], [4, 3], [4, 1]]
#
# p = sorted(k, key=lambda x: x[1])
# print(p)
# p = list(map(lambda x: [x[0]+1, x[1]+1], k))
# print(p)
# print(list(map(lambda x: min(x), k)))
b = sorted(k)
b[0].append(19)
print('b', b)

print('k', k)