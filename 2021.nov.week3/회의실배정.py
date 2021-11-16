n = int(input()) # N = 10만 , 2초 : 4천만
reserve_times = []
# 방문시간을 적어서 게임을 해야 될 것 같아.(데이터도 딱 초반 부분만 사용하면 되서.
for i in range(n):
    a, b = map(int, input().split())
    reserve_times.append((a, b))


reserve_times = sorted(reserve_times, key=lambda x:x[1]) # 끝나는 시간이 빠른 순서대로 정렬
visited = {}
counts = []
max_i = len(reserve_times) - 1
for i, time in enumerate(reserve_times):
    count = 1
    if visited.get(i, False): # 방문했던 곳이면 패스
        continue

    # 처음 방문 하는 곳이면
    visited[i] = True
    s, e = time  # 현재 시작시간 끝나는 시간
    k = i
    print(s, e)
    while k < max_i: # 집중탐색 시간, 탐색을 통해 가장 빠른 들어갈수 있는 시간 선택
        k = k + 1 #다음 시간대 탐색
        start, end = reserve_times[k]
        if e > start: # 바로 다음 오는 애들 못 이어 갈때
            continue
        else: # 이어갈 수 있을 때
            if visited.get(k, False):
                break
            s, e = start, end
            print(s, e)
            count += 1
        visited[k] = reserve_times[k]

    counts.append(count)

print(max(counts))