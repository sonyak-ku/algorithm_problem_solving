from itertools import permutations

def solution(k, dungeons):
    answer = 0
    max_visit = len(dungeons) # 최대로 방문할 수 있는 던전의 개수
    # 최소피로도가 낮은 수으로 정렬을 해보자
    order_dungeon = list(permutations(dungeons, max_visit))

    ## 그냥 전체 탐험해서 결과 뽑아도 될거같애, 던전이 많아봐야 8개니깐 --> 완전탐색문제
    for dungeons in order_dungeon: # 순열로 뽑아낸 모든 던전의 케이스들이 잇음
        current_k = k # 현재 피로도
        visited = 0
        for dungeon in dungeons: # [최소 필요피로도, 소모피로도]
            if current_k < dungeon[0]:
                break
            else: # 던전방문
                current_k -= dungeon[1]
                visited += 1

        answer = max(answer, visited)
        if answer == max_visit: # 최대로 방문한케이스가 있으면 던전탐색 끝내기
            return answer


    return answer

print(solution(80, [[80,20],[50,40],[30,10], [10,10]])) # 현재피로도, [ 최소피로도, 소모피로도 ]