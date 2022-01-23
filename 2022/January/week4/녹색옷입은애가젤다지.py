import sys
import heapq

def count_minimum_rupee(n, list): # 한변의 길이와 리스트형태의 젤다맵을 받는다
    # 다익스트라를 사용하기 쉽게 리스트를 인접리스트의 형태로 데이터 가공
    visited = [[False] * n for _ in range(n)]
    move = [(1, 0), (0, 1)]
    cur = [(list[0][0], 0, 0)]
    heapq.heapify(cur)
    next = []

    while cur or next:
        if not cur and next:
            cur = next
            heapq.heapify(next)
            next = []

        rupee, r, c = heapq.heappop(cur)

        for i in range(2):
            nr, nc = r + move[i][0], c + move[i][1]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] is False:
                next.append((list[nr][nc] + rupee, nr, nc))
                visited[nr][nc] = list[nr][nc] + rupee


    return visited[n - 1][n - 1] # 최소거리를 리턴한다.

N = 1
count = 0
while N:
    N = int(input())
    if not N:
        break
    zelda_map = []
    count += 1
    for _ in range(N):
        data = sys.stdin.readline().rstrip()
        data = list(map(int, data.split()))
        zelda_map.append(data)

    print(f"Problem {count}: {count_minimum_rupee(N, zelda_map)}")
# data = sys.stdin.readline().rstrip()
# data = list(map(int, data.split()))
# print(data)

