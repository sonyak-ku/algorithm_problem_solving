def solution(citations):
    citations.sort(reverse=True)
    s, e, m = 0, len(citations), 0
    answer = 0
    while s <= e: # m => m 번째의 논문은 m 회 이상 인용되었는가?
        m = (s + e) // 2
        # print('s, e',s,e)
        # print(m, citations[m-1])


        if citations[m - 1] >= m: # m 번째로 많이 인용한 논문이 m 번보다 많이 인용되었을 때 -> 오른쪽탐색
            s = m + 1
            answer = min(citations[m - 1], m)
        else: # m 번째로 많이 인용한 논문이 m 번보다 적거나 같게 인용되었을 때
            e = m - 1
    return answer
print(solution([100, 98, 97, 1, 5, 7, 96]))