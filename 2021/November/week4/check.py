def solution(n, times):

    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid
        else:
            start = mid + 1

    answer = start
    return answer

print(solution(6, [4, 10]), '\nanswer: 20')
print(solution(	1, [2, 2]), '\nanswer: 2')
print(solution(	5, [1, 1, 10]), '\nanswer: 3')

