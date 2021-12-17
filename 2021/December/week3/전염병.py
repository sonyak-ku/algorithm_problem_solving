from collections import deque

def solution(m, n, infests, vaccinateds): # 일반인 0, 백신 접종자 1, 감염자 2
    graph = [[0] * (n + 1) for _ in range(m + 1)] # 사무실
    total, inf, vac, day = m * n, len(infests), len(vaccinateds), 0 # 사무실 총 인원, 총 감염자, 총 백신러\

    if total == inf + vac: # 처음부터 모든 직원이 전염병, 백신일때
        return 0

    for vacs in vaccinateds:
        r, c = vacs
        graph[r][c] = 1 # 백신접종자 입력

    for infs in infests:
        r, c = infs
        graph[r][c] = 2  # 감염자 입력

    infests, n_infests = deque(infests), deque()
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while infests:
        cur_r, cur_c = infests.popleft()

        for dr, dc in move:
            nr, nc = cur_r + dr, cur_c + dc
            if 1 <= nr <= m and 1 <= nc <= n and graph[nr][nc] == 0: # 유효한 좌표일때 & 일반인일때
                graph[nr][nc] = 2 # 감염자 처리하기
                inf += 1 # 감염자 수 증가
                n_infests.append((nr, nc)) # 새로운 감염자 리스트에 넣기

        if not infests and n_infests: # 의도: 감염자큐는 비었고, 신규감염자큐는 채워있을때b -> 내가 원하는 대로긴함
            # print(infests, n_infests)
            # print('change', graph)
            infests = n_infests
            n_infests = deque() # 신규확진자 담을 곳 비우기
            day += 1 # 신규감염자의 날을 체크

    # print('out', graph)
    # print(total, inf, vac)
    if total == inf + vac: # 전부 감염 or 백신이므로 감염까지 걸린 날 리턴
        return day
    else: # 전부 감염이 아니므로 -1
        return -1



print(solution(2, 4, [[1, 4], [2, 2]], [[1, 2]]))
print(solution(2, 3, [[2, 2]], [[1, 2], [2, 1], [2, 3]]))
print(solution(2, 2, [[1, 1], [2, 2]], [[1, 2], [2, 1]]))
print(solution(2, 2, [[2, 2]], [[1, 2], [2, 1]]))
