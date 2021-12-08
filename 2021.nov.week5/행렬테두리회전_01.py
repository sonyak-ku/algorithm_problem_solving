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
    # print(graph)
    def rotate(query, answer):
        # print('start rotate', query)
        print(graph)
        start_r, start_c, end_r, end_c = query # 우선은 변수를 알아보기 쉽게, 나를 위해서임!
        turn = (end_r - start_r + end_c - start_c) * 2

        r, c, idx = start_r, start_c, 0
        print(r, c, graph[r][c])
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        save = graph[r][c] # 그 자리의 것을 저장해 놓기 위함
        print(save, r ,c)
        mini = save
        for i in range(turn):
            # 처음 부터 움직여서 그 자리의 것을 다음 것에 입력
            nr, nc = r + move[idx][0], c + move[idx][1]
            if nr < start_r or nr > end_r or nc < start_c or nc > end_c:
                # print(f'rotate, nr{nr}, nc{nc}, r{r}, c{c}')
                # print(nr < start_r or nr > end_r or nc < start_c or nc > start_c)
                # print(f'{nr}<{start_r} or {nr} > {end_r} or {nc} < {start_c} or {nc} > {start_c}')
                idx = (idx + 1) % 4
                nr, nc = r + move[idx][0], c + move[idx][1]
                r, c = nr, nc
            else:
                r, c = nr, nc

            # 좌표 이동후 값 갱신
            save, graph[r][c] = graph[r][c], save
            print(save, r, c)
            mini = min(mini, save)


        # 반복문이 끝나면, 최소값 저장도 되어있으면서 그래프도 갱신되었음
        answer.append(mini)

    for query in queries:
        rotate(query, answer)


    return answer


print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))