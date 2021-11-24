
# able_to_start = [[1, 2]]
# able_to_start.sort(key=lambda x: x[1])
# print(able_to_start)

# d = {'a': 1, 'b': 2, 'c': 3}
# a = sorted(d.items(), key=lambda x: x[1], reverse= True)
# print(a)

l = [i for i in range(4, 10)]

time = [1, 2, 3, 4]
def get_nx(x, times):  # 시간을 넣어서 해당시간까지 심사종료된 사람 수를 리턴하는 함수
    n = 0
    for time in times:
        n += x // time
    return n

k = list(map(lambda x: get_nx(x, time), l))
print(k)

print(l)