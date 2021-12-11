from collections import deque


def solution(maps):  # 스타트 포인트로 시작해서 인접한 곳 전부 숫자 1씩 플러스해서 나아가면 됨

    def find_one(r, c, max_r, max_c):  # 주어진 좌표 r, c 를 통해 maps 안에서 인접한 1(빈곳) 좌표 찾아주는 함수
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        adj = []
        for i in range(4):
            nr, nc = r + move[i][0], c + move[i][1]
            if 0 <= nr <= max_r and 0 <= nc <= max_c:  # 올바른 그래프 좌표일때
                # 1일때만 넣어서 리턴해줘야 됨
                if maps[nr][nc] == 1:
                    adj.append((nr, nc))

        return adj

    max_r, max_c = len(maps) - 1, len(maps[0]) - 1
    q = [(max_r, max_c)]
    q = deque(q)  # BFS 형식으로 숫자를 채워나갈 생각이라서 스타트 한곳 보다 1씩 크게
    while q:

        r, c = q.popleft()
        print(r, c)
        num = maps[r][c]  # 기준점이 지닌 숫자
        adj = find_one(r, c, max_r, max_c)  # 리턴된 [(r, c), (r, c)...]

        for idx in adj:
            q.append(idx)
            a, b = idx
            maps[a][b] = num + 1  # 인접한 곳은 기준점 + 1 의 숫자를 부여

    # 갈 수 있는 부분 다돌았는데
    if maps[0][0] == 1:  # 빈곳을 다돌았는데 스타트 포인트에 다가가지 못함.
        return -1
    else:
        return maps[0][0]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))