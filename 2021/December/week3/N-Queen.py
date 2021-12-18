# 아이디어: 백트래킹
# 구체화 -> 퀸을 배치하고, 같은 열 행 대각 에 퀸이 올수 없다는 표시를 한다. 그 다음 퀸은, 배치 가능한데에 놓고, 대각 열 행에 표시한다. 반복
# n 번 반복을 못할때는 빠꾸하고.
from collections import deque


def solution(n):
    global count
    def find_unable_position(r, c, graph):  # 좌표만 찾아주기
        l = []
        counts = 0
        move = [(1, 0), (1, -1), (1, 1)]  # 아래 세방향 탐색

        for dr, dc in move:
            cur_r, cur_c = r, c
            while 0 <= cur_r < n and 0 <= cur_c < n:
                # print(2)
                if graph[cur_r][cur_c]:  # 놓을 수 있는 곳일때
                    graph[cur_r][cur_c] = False
                    l.append((cur_r, cur_c))

                cur_r, cur_c = cur_r + dr, cur_c + dc
        # print(l)
        return l  # 좌표들 리턴

    def backtracking(m, graph):
        global count
        if m == n:  # 퀸을 모두 찾았음
              # 횟수 증가
            count += 1
            # print('here', count)
            return

            # 탐색
        # stack: True 에서 False 로 변화시킨 좌표들 저장 + 백트래킹으로 false -> true 로 저장
        for c in range(n):  # 해당 행(m) 만 탐색 -> 한 행에 퀸 하나 씩이니깐 (아래쪽만 판단하면 된다)
            if graph[m][c]:  # 퀸을 놓을 수 있다면
                stack = find_unable_position(m, c, graph)  # 아래 세방향으로 못 놓는 좌표 찾는 함수 ㄱ
                # print(m, c)
                backtracking(m + 1, graph)  # 다음 백트래킹 시작
                while stack:  # 백 트랙: 되돌리기    --> 백 트래킹 코드 마무리 한듯한 느낌이 드는데 잘몰겟음
                    # print(1)
                    a, b = stack.pop()
                    graph[a][b] = True

    count = 0
    num = 0
    graph = [[True] * n for _ in range(n)]  # 체스판 위에서 퀸을 놓을 수 있는 곳을 True 로 저장한다.
    backtracking(num, graph)

    return count

print(solution(4))