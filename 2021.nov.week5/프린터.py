from collections import deque


def solution(priorities, location):
    dummy = [0] * len(priorities)
    dummy[location] = 1  # 우리가 뽑아야할 아이의 위치를 파악할 수 있도록 하려구
    pri = deque(priorities)
    dum = deque(dummy)
    count = 0
    while pri:
        if not pri[0] == max(pri):  # 가장앞에 있는 애가 우선순위가 가장 높은 애가 아니면
            pri.rotate(-1), dum.rotate(-1)
        else:  # 가장 앞에 잇는애가 우선순위 탑이라면
            pri.popleft()
            k = dum.popleft()
            count += 1

            if k:
                return count

    return count