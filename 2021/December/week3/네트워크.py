def solution(n, computers): # 똑같은 영역문제
    visited = [False] * n
    count = 0

    for i in range(n): # 탐색 시작
        if visited[i]: # 방문했던 곳이면 pass
            continue

        count += 1 # 영역개수 늘리기
        stack = [i]
        visited[i] = True

        while stack:
            cur = stack.pop()

            for j, is_next in enumerate(computers[cur]):
                if is_next == 1 and visited[j] == False:
                    visited[j] = True
                    stack.append(j)

    return count



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))