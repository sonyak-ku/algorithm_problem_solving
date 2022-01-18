# 이중반복문 사용 금지!
# 딕셔너리로, 각 인덱스의 값들을 저장하자 { 인덱스 : 값, 인덱스 : 값, ...}
# 살아있는 인덱스 리스트를 가지고 있자. 죽으면 앞에서 popleft -> deque
# 인덱스의 값들을 저장할때, 동시에 return 할 answer 값도 append 하자
from collections import deque, defaultdict


def solution(prices):
    answer = []  # 리턴할 답
    index_list = deque()  # 가격이 떨어지지 않고 있는 index 를 저장하고 있기 위함
    index_dict = defaultdict(int)  # prices 값을 인덱스와 엮어서 저장
    prices = deque(prices)

    index_count = 0
    while prices:
        p = prices.popleft()
        if index_list:  # 가격 떨어지지 않고 있는 인덱스 값들이 있다면, 계속 떨어지지 않고 있는지 체크 한 뒤 answer 값 증가
            for idx in index_list:  # 가격이 떨어지지 않은 애들 + 1
                answer[idx] += 1

            while index_list and index_dict[index_list[-1]] > p:  # 가격이 떨어지게 된 인덱스 값들 제거
                index_list.pop()  # 인덱스 값 제거

        # p 값을 새롭게 데이터화 저장
        index_dict[index_count] = p
        index_list.append(index_count)
        index_count += 1
        answer.append(0)

    return answer
