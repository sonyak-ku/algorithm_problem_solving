from collections import defaultdict


def solution(N, road, K):
    INF = int(1e9)
    distance = [INF] * (N + 1)
    visited = [False] * (N + 1)
    adj = defaultdict(list)

    for inter in road:  # 모든 간선 정보를 입력받기
        a, b, d = inter  # 노드1, 노드2, 간선거리
        adj[a].append((b, d))
        adj[b].append((a, d))

    daijkstra(1, distance, visited, adj, N)

    result = list(filter(lambda x: x <= K, distance))

    return len(result) - 1


def daijkstra(start, distance, visited, adj, N):
    # 시작노드 초기화 - 자신을 0으로 한다.
    distance[start] = 0
    visited[start] = True
    for tup in adj[start]:  # (이어진 노드, 간선거리)
        node, dt = tup
        distance[node] = dt  # 스타트 노드와 직접 이어진애들 넣어놧다

    # 이어진 간선거리가 짧은 순서대로 visited 처리하면서 간선 거리 정보 업데이트 하기
    for i in range(N - 1):  # 방문해야 하는 남은 노드들의 개수만큼 for문
        start = get_lowest_inter(distance, visited, N)
        visited[start] = True
        for tup in adj[start]:
            node, dt = tup
            if visited[node]:  # 방문했던 노드면 페스
                continue
            compare = dt + distance[start]  # 작을때만
            if compare < distance[node]:
                distance[node] = compare


def get_lowest_inter(distance, visited, N):
    min_value, index = int(1e9), 0
    for i in range(1, N + 1):
        if i in visited:
            continue
        else:
            if distance[i] < min_value:
                index = i

    return index