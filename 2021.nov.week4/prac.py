
# able_to_start = [[1, 2]]
# able_to_start.sort(key=lambda x: x[1])
# print(able_to_start)

d = {'a': 1, 'b': 2, 'c': 3}
a = sorted(d.items(), key=lambda x: x[1], reverse= True)
print(a)