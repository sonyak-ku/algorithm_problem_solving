def solution(n, m, image):
    graph = [[False] * m for _ in range(n)]  # 방문처리를 위한 맵을 그린다.
    count = 0  # 영역의 개수
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(n):
        for c in range(m):  # 이미지 맵 탐색
            if graph[r][c]: # 방문했던 곳이면 패스
                continue

            target = image[r][c]  # 같아야하는 숫자 저장
            bfs = []
            bfs.append((r, c))
            count += 1 # 영역개수 하나 늘리기

            while bfs:  # 인접한 곳 탐색 시작하쟝
                cur_r, cur_c = bfs.pop()
                graph[cur_r][cur_c] = True  # 방문 처리

                for dr, dc in move:  # 배운 부분 -> 한번에 돌려도 된다.
                    nr, nc = dr + cur_r, dc + cur_c
                    # 유효한 좌표이며, 타겟넘버가 같고, 방문한 적이 없을 때
                    if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == target and graph[nr][nc] == False:
                        bfs.append((nr, nc))
                        print(nr, nc)

    return count


print(solution(2, 3, [[1, 2, 3], [3, 2, 1]]))
print(solution(3, 2, [[1, 2], [1, 2], [4, 5]]))