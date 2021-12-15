import heapq


def solution(n, works):
    que = []

    # 시간이 너무 충분해서 일을 다 끝낼 수 있을 경우 --> 얘를 앞에서 넣자
    if sum(works) <= n:
        return 0

    for work in works:
        heapq.heappush(que, work * (-1))

    while n > 0:
        n -= 1
        item = heapq.heappop(que)
        heapq.heappush(que, item + 1)

    answer = 0
    while que:
        answer += que.pop() ** 2

    return answer