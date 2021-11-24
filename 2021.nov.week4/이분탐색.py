def solution(n, times):
    times.sort()  # 입국심사관들 걸리는 시간 오름차순 정렬

    def get_n(x):  # 시간을 넣어서 해당시간까지 심사종료된 사람 수를 리턴하는 함수
        n = 0
        for time in times:
            n += x // time
        return n

    start, end = 0, n * times[-1]

    while start <= end:
        mid = (start + end) // 2
        get = get_n(mid)
        if get == n:
            return mid
        elif get < n:  # 타겟 넘버가 생각보다 큼
            start = mid + 1
        else:  # 타겟 넘버가 생각보다 작음
            end = mid - 1

# 만약 [7, 10] 이고 29가 넣어졋을 때 n 이 딱 떨어지는 문제는 어떻게 해결할 것인가? ->같은 n 을 출력하는 boundary 내에서 최솟값을 어떻게 뽑을 것인가?