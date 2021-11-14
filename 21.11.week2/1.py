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
# b = sorted(k)
# b[0].append(19)
# print('b', b)
#
# print('k', k)
# a = list(range(1, 10))
# b = sum(list(range(2, 10)))
# print(b)
# print(reduce(lambda x, y: x - y, a))
# b = sorted(k, key= lambda x: x[1]) # 이중 리스트에 영향을 주지 않는다.
# print(b)
# print(sorted(k))
# print(k)

# a = [[',',',',',', ','], [2, 3,4]]
# a[1] = ['k']
# print(a)
k = [[60, 50], [30, 70], [60, 30], [80, 40]]

j = list(map(sorted, k))
print(j)