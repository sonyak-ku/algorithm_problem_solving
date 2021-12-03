import heapq


def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    # visited = [False] * (N + 1)
    graph = [[] for i in range(N + 1)]  # 인접한 노드들과 간선 거리를  (간선거리, 노드 번호) 형태로 저장하기 위함
    distance = [INF] * (N + 1)

    for r in road:  # 노드들과 간선거리들의 정보를 저장
        a, b, d = r
        graph[a].append((d, b))
        graph[b].append((d, a))

    def daijkstra(start):
        # visited[start] = True
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:  # 큐가 있다면
            dt, node = heapq.heappop(q)

            if distance[node] < dt:  # 처리할 필요가 없는 노드 저장은 6거리로 되있는 데 8 나오면 쓸모없지,
                continue

            for i in graph[node]:  # (간선거리, 노드번호)
                cmp = dt + i[0]
                if cmp < distance[i[1]]:
                    distance[i[1]] = cmp
                    heapq.heappush(q, (cmp, i[1]))

    daijkstra(1)
    # print(distance)
    k = list(filter(lambda x: x <= K, distance))

    return len(k)