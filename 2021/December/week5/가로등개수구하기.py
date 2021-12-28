from collections import deque


def solution(l, v):
    light = v
    light.sort()

    def check_road(i, lights):  # 빛이 제 거리를 커버하고 있는지 아닌지 체크하기 위함
        print(lights)
        d = deque(lights)
        print(d)
        start = 0 - i
        while d:
            # print('left:', start + i, 'right:', d[0])
            if start + i >= d[0] - i:  # 도로의 시작부터 첫 가로등이 커버치고있을 때
                start = d.popleft()
            else:
                return False  # 사이에 빛이 비추어지지 않는 도로가 있다는 뜻

        if start + i < l:  # 마지막 가로등이 비추는 빛이 도로 끝을 비추지 못할 때
            return False
        else:
            return True
    #
    s, m, e = 0, 0, l

    while s < e:  # 이진탐색 시작
        print(s, e)
        m = (s + e) // 2
        # print('light', light)
        if check_road(m, light):  # True 가 뜬다면 빛이 비추는 거리가 여유있음 을 나타냄 > 좀 더 줄여보자
            e = m
        else:  # False 가 뜨면 빛이 비추는 거리가 짧음 >> 늘려야함
            s = m + 1
    # print(check_road(2, light))
    return (s + e) // 2

print(solution(15, [15, 5, 3, 7, 9, 14, 0]))