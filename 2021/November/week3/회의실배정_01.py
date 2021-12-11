import sys

## import sys 가 매우 크구나 8퍼에서 깨지던데 22 퍼까지 갓음

n = int(input())  # N = 10만 , 2초 : 4천만
reserve_times = []

# 방문시간을 적어서 게임을 해야 될 것 같아.(데이터도 딱 초반 부분만 사용하면 되서.
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    reserve_times.append((a, b))

### 아래에서 while 문을 돌릴 필요가 없음, 이미 종료시간을 기준으로 정렬햇기때문에 뒤에서 더 효율적인건 안나옴.
### x[1] 을 기준으로 정렬하면 입력된 순서에서 x[0] 이 내림차로 자동으로 정렬되는게 아니구나 ###
reserve_times = sorted(reserve_times) # 미리 앞에거를 낮은 순으로 정렬하고 뒤에 정렬하면 됨
reserve_times = sorted(reserve_times, key=lambda x: x[1])  # 끝나는 시간이 빠른 순서대로 정렬visited = {}
print(reserve_times)
counts = []
max_i = len(reserve_times) - 1
s, e = -1, -1
for time in reserve_times:
    if e > time[0]:  # 시작시간이 종료시간보다 일찍이면 패스
        continue
    else:
        s, e = time
        counts.append(time)
        # print(counts)

print(len(counts))
