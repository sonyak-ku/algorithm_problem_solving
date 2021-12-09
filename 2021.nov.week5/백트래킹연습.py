n, m = map(int, input().split()) # 1부터 n 까지의 숫자중 중복없이 m 개 뽑기  --> 백트래킹으로 풀어보자


l = []
visited = [False] * (n + 1)

def back_tracking(num): # 재귀함수는 항상 종료시점을 먼저 쓰고 들어간다
    if num == m:
        # 어떤 것을 작동할 것인지
        print(" ".join(map(str,l)))
        return

    for i in range(1, n + 1):
        if visited[i] == False:
            visited[i] = True
            l.append(i)
            back_tracking(num + 1)
            ## 여기가 중요, 이 for 문에서 나오고 다음 for 문 진행할 때, 영향받은 visited와 리스트를 그렇지 않은 상태로 돌려야된다.
            l.pop()
            visited[i] = False
        else:
            continue

back_tracking(0)