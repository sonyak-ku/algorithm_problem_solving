import heapq
import copy

def solution(jobs): # 솔직히 감은 바로 오진 않지만, 그냥 대기 하고 있는 애들 중에서 소요시간이 가장 짧은 애 부터 처리 해라?
    able_to_start = []
    current_time = 0
    answer = 0
    j = copy.deepcopy(jobs)    # 데이터구조 [작업이 요청되는 시점, 작업의 소요시간]
    heapq.heapify(j)

    ## 여기서도 똑같이 터지는 애들이 있는 거같음
    # 하나 뽑고 바로 j 가 비어버리는 경우 에러발생.

    while able_to_start or j: # 둘 중에 하나라도 살아잇으면 반복하기

        while j:  # 여기는 런타임 에러가 없을 거라고 예상! 왜?
            if current_time >= j[0][0]:
                able_to_start.append(heapq.heappop(j))
            else:
                break
        print(j)
        # 소요시간이 짧은 순서로 먼저 처리한다
        ############ 항상 able_to_start 가 j 보다 많을거라고만 생각했지만, 실제로는 당장 처리할 애들은 없고 잠시 소강 상태에 접했을 수도 있다
        ########### 그것을 처리하지 못해 생겨난 오류 및 에러
        if able_to_start:
            able_to_start.sort(key=lambda x: x[1])
            processing = able_to_start.pop(0)
            # 시간 지남 처리
            current_time += processing[1]
            # 일 처리시간 더해 놓기 --> 작업종료된 현재시점 - 작업이 요청된 시점
            answer += (current_time - processing[0])
        else:
            current_time += 1 # 할 일은 남아있지만, 당장 처리 할 수 있는 일이 없을 때 시간을 증가시킨다.

    return answer // len(jobs)

a = [[1, 9], [0, 3], [2, 6]]
# heapq.heapify(a)
# print(a)
print(solution(a))