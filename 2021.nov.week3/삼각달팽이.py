def solution(n):
    ### n = 1000 -> O(N) 으로 끝낼 수 있는 문제를 굳이 while 문돌려서 버러지짓 안해서 다행
    base = [[0 for j in range(i)] for i in range(1, n+1)]

    move = [(1, 0), (0, 1), (-1, -1)] # 3방향 이동 구현 아래, 옆, 대각 위
    r, c, i, idx = 0, 0, 0, 1 # 스타트 로우 컬럼, 스타트방향, 넣을 숫자
    fin_num = n * (n + 1) // 2

    for k in range(1, fin_num + 1):

        base[r][c] = k

        # 다음 r c 정해줘야함
        nr, nc = r + move[i][0], c + move[i][1]
        if nr == n or nc == n or base[nr][nc] != 0:
            i = (i + 1) % 3
            nr, nc = r + move[i][0], c + move[i][1]
            r, c = nr, nc
        else:
            r, c = nr, nc

    # while idx <= fin_num:
    #     if base[r][c] == 0: # 첨 방문한 곳이면 숫자입력하고 방문숫자 1 증가
    #         base[r][c] = idx
    #         idx += 1
    #
    #     # 탐색할 좌표 갱신코드
    #     nr, nc = r + move[i][0], c + move[i][1]
    #     if nr == n or nc == n or base[nr][nc] != 0: # 벽에 부딪히면 방향 바꾸기 or 값 있는 곳이면 방향 바꾸기
    #         i = (i + 1) % 3  # 방향 바꿔주고 루프 진행
    #     else:
    #         r, c = nr, nc

    answer = [num for r in base for num in r]

    return answer

print(solution(4))