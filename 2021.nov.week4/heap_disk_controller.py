import heapq
import copy

def solution(jobs): # 솔직히 감은 바로 오진 않지만, 그냥 대기 하고 있는 애들 중에서 소요시간이 가장 짧은 애 부터 처리 해라?
    able_to_start = []
    current_time = 0
    answer = 0
    j = copy.deepcopy(jobs)    # 데이터구조 [작업이 요청되는 시점, 작업의 소요시간]
    heapq.heapify(j)

     ## 여기를 못나오고 잇어
    while current_time >= j[0][0]:
        able_to_start.append(heapq.heappop(j)) # 0 초때에 처리할 수 있는 애들 만들어 놓기
    # print('able_to_start',able_to_start)

    while able_to_start or j: # 둘 중에 하나라도 살아잇으면 반복하기
        print('current_time',current_time)
        while j:  ## 여기를 못나오고 잇어
            print('f',j)
            if current_time >= j[0][0]:
                o = heapq.heappop(j)
                able_to_start.append(o)
                print('here')
                print('l', j)
                # print('a',able_to_start)
                # print(j)
            else:
                print('end')
                break
            # print('l',j)

        # 소요시간이 짧은 순서로 먼저 처리한다
        able_to_start.sort(key=lambda x: x[1])
        processing = able_to_start.pop(0)
        # print('processing',processing)
        # print('able_to_start',able_to_start)
        # 시간 지남 처리
        current_time += processing[1]

        # 일 처리시간 더해 놓기 --> 작업종료된 현재시점 - 작업이 요청된 시점
        answer += (current_time - processing[0])

    return answer // len(jobs)

a = [[1, 9], [0, 3], [2, 6]]
# heapq.heapify(a)
# print(a)
print(solution(a))