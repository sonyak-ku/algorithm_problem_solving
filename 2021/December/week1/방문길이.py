def solution(dirs):  # 변 이라는 걸 어떻게 처리해야 될까?
    points = set()
    maps = [[0] * 11 for _ in range(11)]  # 움직일 때 0인 곳으로 움직여야 새로운 길을 걸은 것으로 체크
    direc = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    r, c = 5, 5
    count = 1
    maps[r][c] = count  # 마지막 좌표의 숫자에서 1을 빼야 걸은 거리가 됨

    for w in dirs:
        idx = direc[w]  # (r, c)
        nr, nc = r + idx[0], c + idx[1]

        if 0 <= nr <= 10 and 0 <= nc <= 10:  # 제대로된 좌표라면
            point = ((r + nr) / 2, (c + nc) / 2)
            r, c = nr, nc
            points.add(point)

    return len(points)


# 좌표의 사이 를 표현할 수 있게 되었다.