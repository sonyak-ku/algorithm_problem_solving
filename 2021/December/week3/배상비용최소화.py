import heapq


# 힙큐로 가장 큰 애 계속 뽑으면서 n을 하나씩계속 뽑고 나머지 제곱해서 더하면 된다.

def solution(no, works):
    # 최댓값을 뽑을수있는 힙구조여야한다.
    que = []  # 힙큐로 사용할것
    for i in works:  # 마이너스를 곱해서 큰 수가 먼저 뽑히도록 하는 식으로 풀겟음 -> 어짜피 제곱해서 더할것들임
        heapq.heappush(que, i * (-1))

    while no > 0:  ## 전부 다 0 이 되었을 때(일 전부 끝), n 이 돌아가면 숫자가 늘어남 >>> 이거어케 찾지 이런오류는 ㄷ

        no -= 1
        item = heapq.heappop(que)
        heapq.heappush(que, item + 1)
        if sum(que) == 0:  # 일이 전부 끝났다면!! 전부 0 일때
            return 0  # 여기서 종료!

    answer = 0
    while que:
        answer += que.pop() ** 2

    return answer

# N이 works 의 일을 전부 다 처리할 수 있는 경우가 히든이엇다