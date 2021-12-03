def solution(grid):
    graph = [[ww for ww in w] for w in grid]
    visited = [[[] for ww in w] for w in grid]

    def search(graph, visited):  # start: (0, 0)
        idx = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 시계방향 : 위 오른 아래 왼쪽
        result = []
        r_wall, c_wall = len(graph), len(graph[0])
        for r in range(r_wall):
            for c in range(c_wall):
                for i in range(4):  # 전방향 탐색

                    if i in visited[r][c]:  # 이미 해당 구역에서 해당 방향의 빛은 처리되었습니다.
                        continue

                    count = 0
                    direc = i
                    while True:  # 매 반복마다 해야 되는 것:

                        if direc in visited[r][c]:  # 사이클 한바퀴 다돌음
                            break

                        visited[r][c].append(direc)  # 시작 방향을 넣는다.
                        count += 1

                        # 좌표 이동시켜준다 + 문자에 따라 방향도 바꿔주고 넘긴다
                        r, c = r + idx[direc][0], c + idx[direc][1]
                        if r == r_wall:
                            r = 0
                        elif r < 0:
                            r = r_wall - 1

                        if c == c_wall:
                            c = 0
                        elif c < 0:
                            c = c_wall - 1

                        if graph[r][c] == 'R':  # 방향 바꾸어 주기
                            direc = (direc + 1) // 4
                        elif graph[r][c] == 'L':
                            if direc == 0:
                                direc = 3
                            else:
                                direc -= 1

                    result.append(count)  # 사이클을 저장

        return result

    answer = search(graph, visited)

    return sorted(answer)

# 피곤해서 내일 처리하겟습니당 --> 오류는 안나지만 풀이한 답이 다르게 나옴 조건 제대로 다시 살피면 조을듯
