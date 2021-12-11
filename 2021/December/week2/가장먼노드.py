import heapq


def solution(n, edge):  # 다익스트라 로 풀어볼수 있을듯?

    graph = [[] for _ in range(n + 1)]  # 간선으로만 이루어져있음, 거리 없음
    inf = int(1e9)
    distance = [inf] * (n + 1)

    for vertex in edge:  # 간선으로 연결된 곳을 저장해놓음
        a, b = vertex
        graph[a].append((1, b))
        graph[b].append((1, a))

        # 다익스트라 ㄱ
        def daijkstra(start): # 1입력
            q = []
            distance[start] = 0
            for v in graph[start]: #(1, 노드번호)
                d, node = v
                heapq.heappush(q, v)
                distance[node] = d

            while q: # 힙큐탐색
                d, node = heapq.heappop(q)
                if d > distance[node]: #탐색할 필요없는 쓸모없는 거리 노드
                    continue

                for v in graph[node]:
                    vd, vnode = v
                    if vd + d < distance[vnode]: # 기존거리보다 더 짧은 루트라면
                        distance[vnode] = vd + d
                        heapq.heappush(q, (vd + d, vnode))    # 다익스트라 완성인듯?

    daijkstra(1)
    m = 0
    for d in distance:
       if m < d < inf: # 두번째값찾기
           m = d

    return distance.count(m)

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))