from collections import deque


def solution(rows, columns, queries):
    answer = []
    graph = [[0] * (columns + 1) for i in range(rows + 1)]
    # 숫자 넣어놓기
    r, c = 1, 1
    for i in range(1, rows * columns + 1):  # 그래프 완료
        graph[r][c] = i
        c += 1
        if c > columns:
            r, c = r + 1, 1

    def rotate_and_adjust(query, answer):
        sr, sc, er, ec = query   # 2  2  5, 4
        r, c, idx, turn = sr, sc, 0, (er - sr + ec - sc) * 2
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른 아래 왼 위
        l = []
        for i in range(turn):
            l.append(graph[r][c])
            print(r, c)
            nr, nc = r + move[idx][0], c + move[idx][1]

            if nr < sr or nr > er or nc < sc or nc > ec: # 사각형 튀어나간것
                idx += 1
                nr, nc = r + move[idx][0], c + move[idx][1]
                r, c = nr, nc
            else:
                r,c = nr, nc

        l = deque(l)
        l.rotate(1)
        answer.append(min(l))
        sr, sc, er, ec = query  # 2  2  5, 4
        r, c, idx, turn = sr, sc, 0, (er - sr + ec - sc) * 2
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른 아래 왼 위
        for i in range(turn):

            graph[r][c] = l.popleft()
            nr, nc = r + move[idx][0], c + move[idx][1]
            if nr < sr or nr > er or nc < sc or nc > ec: # 사각형 튀어나간것
                idx += 1
                nr, nc = r + move[idx][0], c + move[idx][1]
                r, c = nr, nc
            else:
                r, c = nr, nc

        return l

    for query in queries:
        rotate_and_adjust(query, answer)

    return answer


print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))