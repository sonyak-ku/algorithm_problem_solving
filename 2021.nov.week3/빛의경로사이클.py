def solution(grid): # 500 * 500 총 25000 개 그리드에 , 4방향탐색이면 최대 10만회의 탐색
    answer = []
    # 상0 오른1 하2 왼3 ->시계방향
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    save = [[[] for __ in _] for _ in grid] # 방향을 저장할 공간 -> 이거 움직인 방향 그냥 저장해도 됨:: 그래야 완전탐색이 가능해짐.
    board = [[g for g in _] for _ in grid]
    # 빛의 움직임을 구현 해봅시다.
    i = 0 # 처음은 북쪽방향 빛부터
    max_c, max_r = len(grid) - 1, len(grid[0]) - 1
    for i in range(4):
        for r in save:
            for c in r:
                if i in save[r][c]: # 이미 지나간 사이클이면 패스
                    continue

                # 처음 걸어보는 사이클일때
                count = 0
                while True:
                    if i in save[r][c]: # 깨지는 조건을 설정 : 같은 방향으로 다시 돌아올때
                        break
                    # 그게 아니라면
                    count += 1
                    save[r][c].append[i]
                    # r, c, i 변화 필요 i 먼저
                    flag = board[r][c]

                    if flag == 'L':
                        i -= 1
                    elif flag == 'R': # R
                        i += 1

                    if i == -1: # 음수처리
                        i = 3
                    if i > 3: # 방향안에서 돌게끔 나눠서 몫 사용 귀찮
                        i -= 4

                    r, c = r + move[i][0], c + move[i][1]
                    ## 벽부분 구현 냅두기 , 벽에 도달하면 반대벽에 나오는거 그거 구현해야댐


                answer.append(count)







    return answer.sort(reverse=True)

grid = ['R', 'R']