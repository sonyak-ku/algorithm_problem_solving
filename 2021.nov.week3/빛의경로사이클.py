def solution(grid):  # 500 * 500 총 25000 개 그리드에 , 4방향탐색이면 최대 10만회의 탐색
    answer = []
    # 상0 오른1 하2 왼3 ->시계방향
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    save = [[{} for __ in _] for _ in grid]  # 방향을 저장할 공간 -> 이거 움직인 방향 그냥 저장해도 됨:: 그래야 완전탐색이 가능해짐.
    board = [[g for g in _] for _ in grid]
    # 빛의 움직임을 구현 해봅시다.
    i = 0  # 처음은 북쪽방향 빛부터
    max_r, max_c = len(grid) - 1, len(grid[0]) - 1
    for i in range(4):
        for ir, r in enumerate(save):
            for ic, c in enumerate(r):  # c: dict 방향저장용 True, False 로 저장
                if c.get(i, False):
                    continue  # 다음 블록으로 이동해서 탐색
                #처음 만나는 블록일 때
                count = 1# 현재 방향 위치에 저장하구 r, c 위치를 변화시켜서 while 문에 넘기면 됨
                c[i] = True
                ir, ic = ir + move[i][0], ic + move[i][1]
                if ir > max_r:
                    ir = 0
                elif ir < 0:
                    ir = max_r

                if ic > max_c:  # 벽을 만날때 튀어나오는 케이스 테스트하기
                    ic = 0
                elif ic < 0:
                    ic = max_c

                while True:
                    if board[ir][ic] == 'R':
                        i += 1
                    elif board[ir][ic] == 'L':
                        i -= 1

                    if i < 0:  # i 조정시키기
                        i = 3
                    elif i > 3:
                        i = 0

                    if save[ir][ic].get(i, False): #
                        break  # 같은 방향이 있다는것(사이클이 돌았다는 뜻) 반복문 종료
                    count += 1 # 한 번 이동 체크
                    save[ir][ic][i] = True #### 화살표 방향 저장 --> 종료조건
                    ir, ic = ir + move[i][0], ic + move[i][1] # 이동할 위치 저장
                    if ir > max_r:
                        ir = 0
                    elif ir < 0:
                        ir = max_r

                    if ic > max_c:  #벽을 만날때 튀어나오는 케이스 테스트하기
                        ic = 0
                    elif ic < 0:
                        ic = max_c

                answer.append(count)

    answer.sort(reverse=True)
    return answer


grid =["SL","LR"]

print(solution(grid))
