def solution(distance, rocks, n):
    # 거리차 그래프를 찾아놓자
    rocks.sort()

    def break_rock(dt):  # 거리 이하의 바위를 전부 파괴하고 그 숫자 리턴하는 함수
        start, count = 0, 0
        flag = False

        for rock in rocks:
            if rock - start > dt:
                start = rock
                continue
            elif rock - start == dt:
                # print(dt, 'True')
                flag = True
                start = rock
                continue
            else:  # 거리보다 작을 때 바위파괴
                count += 1

        if distance - start < dt:  # 맨 마지막 남은거리 체크가 요구 거리보다 작아서 최소거리가 dt 가 아닐때
            # print(dt, 'false', distance - start)
            flag = False
        elif distance - start == dt:
            flag = True

        return flag, count

    s, e, m = 0, distance, 0

    while s <= e:
        m = (s + e) // 2
        flag, count = break_rock(m)
        # print(f'break_rock({m})')
        if count == n:
            # print('found', m)
            if flag:  # 최솟값일때
                return m
            else:  # 최솟값이 아니라는 뜻
                # print('here')
                e = m - 1
        elif count > n:
            # print('big', count, n)
            # print('start/end', s, e)
            e = m - 1
        else:
            # print('small', count, n)
            # print('start/end', s, e)
            s = m + 1

        if count > n:
            return m - 1
        elif count < n:
            return m + 1


print(solution(11, [1, 2, 8, 9, 10], 4)) #답 3

