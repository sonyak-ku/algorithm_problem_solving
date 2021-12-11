
def solution(n, times):
    times.sort()  # 입국심사관들 걸리는 시간 오름차순 정렬

    def get_n(x):  # 시간을 넣어서 해당시간까지 심사종료된 사람 수를 리턴하는 함수
        n = 0
        flag = False  # 하나라도 딱나누어 떨어진 적이 있다면 True
        for time in times:
            n += x // time
            if not x % time:  # 나누었을 때 나머지가 없이 딱떨어진 케이스면 -> 문을 딱닫았다면
                flag = True
        return (n, flag)

    start, end = 0, n * times[-1]

    mid = 0
    while start <= end:
        mid = (start + end) // 2
        print('time:', start, mid, end)
        get, flag = get_n(mid)
        print('get:', get)
        if get == n:
            print('here')
            if flag:  # 딱떨어진 케이스
                return mid
            else:  # n 은 맞췄지만, boundary 안에 있을 때
                end = mid

        elif get < n:  # 타겟 넘버가 생각보다 큼
            start = mid + 1
        else:  # 타겟 넘버가 생각보다 작음
            end = mid - 1
    print('outside')
    if get < n:
        return mid + 1
    else:
        return mid


print(solution(6, [4, 10]), '\nanswer: 20')
print(solution(	1, [2, 2]), '\nanswer: 2')
print(solution(	5, [1, 1, 10]), '\nanswer: 3')