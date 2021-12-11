from bisect import bisect_left


def solution(n, times):
    times.sort()  # 입국심사관들 걸리는 시간 오름차순 정렬

    def get_n(x):  # 시간을 넣어서 해당시간까지 심사종료된 사람 수를 리턴하는 함수
        n = 0
        for time in times:
            n += x // time
        return n

    start, end = 0, n * times[-1]
    tmp_answer_n = 0
    while start <= end:
        mid = (start + end) // 2
        get = get_n(mid)
        if get == n:
            tmp_answer = mid
            break
        elif get < n:  # 타겟 넘버가 생각보다 큼
            start = mid + 1
        else:  # 타겟 넘버가 생각보다 작음
            end = mid - 1

    start, end = 0, (n - 1) * times[-1]
    tmp_answer_n_1 = 0
    while start <= end:
        mid = (start + end) // 2
        get = get_n(mid)
        if get == n:
            tmp_answer_1 = mid
            break
        elif get < n:  # 타겟 넘버가 생각보다 큼
            start = mid + 1
        else:  # 타겟 넘버가 생각보다 작음
            end = mid - 1

    # tmp_answer 가 n의 숫자만 맞추고 최솟값이 아닌 경우가 있기 때문에 n이 n-1이 될때까지, tmp-answer를 1씩 떨어뜨려본다.
    # 이거 시간오류 날거 같은데 일단 이거 밖에 생각이 안떠오른다
    l = list(map(lambda x: get_nx(x, times), [i for i in range(tmp_answer_1, tmp_answer + 1)]))

    # i = bisect_left(l, n)
    return 1


def get_nx(x, times):  # 시간을 넣어서 해당시간까지 심사종료된 사람 수를 리턴하는 함수
    n = 0
    for time in times:
        n += x // time
    return n
# 만약 [7, 10] 이고 29가 넣어졋을 때 n 이 딱 떨어지는 문제는 어떻게 해결할 것인가? --> 하나씩 떨어뜨려 보는 과정이 필요할 것 같다.
# 이런식으로 Lower bound 찾아보려고 햇으나 역시 시간 초과가 난다.
# 그래도 44점은 먹엇다