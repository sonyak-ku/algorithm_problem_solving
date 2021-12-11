import heapq


def solution(scoville, K): #스코빌 리스트의 길이는 100만
    heap = scoville
    heapq.heapify(heap)  # 리스트 heap 이 최소정렬로 전환된다.시간 복잡도는 O(n) 이다. 반면 리스트 sort의 경우 nlogN 의 시간복잡도(좀 더 시간 걸림)
    count = 0
    if heap[0] >= K: # 만약 최소값이 이미 기준치보다 높을 때
        return 0
    while len(heap) > 1: # 안에 내용물 없으면 반복문 종료  ### 힙큐를 반복문에서 처음 돌리면 인덱스 에러를 체크해야 함.
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + b * 2)
        count += 1
        if heap[0] >= K:
            return count
    return -1


scovile = [1, 2, 3, 9, 10, 12]
k = 200

print(solution(scovile, k))