
## 리스트의 경우 리스트의 맨 앞에서 삽입 삭제 가 일어나면, 그것을 삭제하고 뒤에잇는애들을 앞으로 당겨와 옮겨주는 작업이 필요 O(N)
## 반면 링크드 리스트 형식으로 연결된 Deque 는 앞에서 삽입 삭제가 일어나더라도 O(1) 의 시간 밖에 걸리지 않는다
## 따라서 처리해야 하는 선형구조의 데이터의 양이 많을 때는 deque 를 사용하도록 하자

import heapq
from collections import deque


def solution(operations):
    d = deque()

    for op in operations:
        order, num = op.split()
        if order == 'I':
            d.append(int(num))

        if order == 'D':
            if len(d) > 0:
                d = deque(sorted(d, key=lambda x: x))
                if num == '1':  # 최댓값 삭제
                    d.pop()
                else:
                    d.popleft()

    if len(d) == 0:
        return [0, 0]
    else:
        d = deque(sorted(d, key=lambda x: x))
        return [d.pop(), d.popleft()]