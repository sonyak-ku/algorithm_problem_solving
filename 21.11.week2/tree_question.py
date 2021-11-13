def solution(n, wires):
    answer = n + 1
    adj_list = {

    }  # 1:[2, 3], 2: [1, 5] ...
    for i in range(1, n + 1):
        adj_list[i] = []  # 송전탑의 인접리스트를 표현하기위해 미리 공간 세팅하기.

    for wire in wires:  # 인접리스트 채우기
        i, j = wire[0], wire[1]
        adj_list[i].append(j)
        adj_list[j].append(i)

    for wire in wires: # 전력망 끊어 보기
        i, j = wire[0], wire[1]
        if len(adj_list[i]) == 1 or len(adj_list[j]) == 1:
            continue # 하나밖에 연결 안된 애들 끊어봐야 탐색하는 소스가 아까워서
        stack = [i] # i 를 탐색합시당
        visited = []
        # 전체 전력망개수는 n 이라고 나와있으므로, 하나만 탐색하면 된다.
        while stack:
            s = stack.pop()
            if s not in visited:
                visited.append(s)
                adj = adj_list[s]
                for a in adj:
                    if a != j: # 끊긴 애만 아니라면
                        stack.append(a)  # 스택에 넣습니다.
        diff = abs((n - len(visited)) - len(visited))
        # 스택 탐색이 끝났을 때
        answer = min(answer, diff)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
