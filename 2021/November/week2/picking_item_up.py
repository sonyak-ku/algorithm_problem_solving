import numpy as np
import sys


def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [[0 for j in range(51)] for i in range(51)]  # 걸어 다닐 수 있는 좌표들을 1 로 적을꺼양
    min_cord = []  # 가장 최솟점 찾기위해서   #################-----------------> 가장 작은 수를 스타트로 한다는 생각이 살짝 위험할 수도 있겠다
    for rec in rectangle:  # 사각형의 최소꼭짓점과 최대꼭지점을 하나씩 빼서
        rectangle_line = find_rectangle_coordinates(rec)  # 사각형의 변들이 좌표로 되어잇음
        all_x, all_y = [rec[0], rec[2]], [rec[1], rec[3]]
        min_cord.append((all_x[0], all_y[0]))  # 모든 사각형의 Min 좌표를 미리 저장해놓는다
        for cord in rectangle_line:
            x, y = cord  # 좌표를 풀어
            if x in all_x and y in all_y:  # 사각 형의 꼭짓점에 해당하는 좌표일 때 - 꼭짓점에서는 절대 만나지 않는다는 규칙이 잇으므로
                maps[x][y] = 2  # 꼭짓점은 2로 표시한다
            else:  # 꼭짓점이 아닐때 -- 일반 선분이 위치하거나, 교차점이 발생한다.
                if maps[x][y] == 1:
                    maps[x][y] = 3  # 교차점은 3 으로 표시한다.
                else:
                    maps[x][y] = 1  # 일반 선분은 1 로 표시한다.

    ## 꼭짓점에서 start 가 출발해버리면, 진짜 개 졷될거같음, 두방향으로 움직이는 로직만 생각햇는데, 꼭짓점이 스타트 지점이면 어떻게 움직일 방향을 선택하지? 해결!!
    ## 해결 --> 그냥 1,1 혹은 가장 최소지점 부터 루프를 돌고, 캐릭터좌표나, 아이템 좌표를 만나면 카운트 시작해서, 다시 만나면 카운트를 멈추는 식으로 한쪽의 거리 측정뒤에
    ## 한바퀴를 돌아서 나오는 전체 거리에서 빼면, 양방향으로 거리 비교를 할 수 있다!!!
    character = (characterX, characterY)
    item = (itemX, itemY)
    move_direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위, 오른, 아래, 왼
    x, y = min(min_cord)  # 가장 최소의 좌표 를 스타트로
    minmin = min(min_cord)
    between, total_len = 0, 0
    flag = False  # 아이템이나 캐릭터를 만났는지 여부
    i = 9  # 처음 어느 방향먼저 움직일지

    while True:  ##### 확실하지 않음 여기는
        # print(f'(x, y): ({x}, {y}), charcter: {character}, item: {item}')
        if (x, y) == character or (x, y) == item:       ## 현재 위치한곳이 캐릭터나 아이템의 위치인지 체크
            flag = not flag  # 플래그 반대로 변경
        if flag:  # 둘 중 하나 만난 상태면 사이 거리 측정 시작
            between += 1

        move_i = i % 4
        nx, ny = x + move_direction[move_i][0], y + move_direction[move_i][1]
        if maps[nx][ny] == 0:
            i += 1
            continue  # 방향을 시계 방향으로 바꾼뒤에 다시시작
        elif maps[nx][ny] == 1:
            total_len += 1
            x, y = nx, ny
        elif maps[nx][ny] == 2:
            total_len += 1
            x, y = nx, ny  # 똑같이 이동하지만, 방향을 시계방향으로 한번 움직인다
            i += 1
        elif maps[nx][ny] == 3:
            total_len += 1
            x, y = nx, ny  # 똑같이 이동하지만, 방향을 반시계방향으로 한번 움직인다
            i -= 1

        if (x, y) == minmin: # 한바퀴 다돌았으면 반복문 종료
            break
        if total_len > 1000: # 그냥 에러때문에 루프가 안종료될때 1000번 찍으면 끝나게
            # print('while 문이 끝나지 않음 1000회 넘음')
            break
        # 지도 탐색 시작

    return min(between, total_len - between)


# 꼭짓점이랑 교차점에서 이동방향을 바꾸는 식으로 플레이를 해봅시다.
def find_rectangle_coordinates(rectangle):  # 좌표뽑기 코드
    # 위로, 오른쪽으로, 아래로, 왼쪽으로
    minx, miny, maxx, maxy = rectangle
    move_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우리가 생각하는 그래프(row, column) 이 아닌 좌표 x, y 축 상을 기준으로
    x, y = minx, miny
    count = [maxy - miny, maxx - minx]
    rec_cord = []
    for i, cord in enumerate(move_direction):
        k = i % 2
        for _ in range(count[k]):
            x += cord[0]
            y += cord[1]
            rec_cord.append((x, y))  # 여기서 꼭짓점 교찻점 표시할지, 맵에 표시할지 그런거 생각 ㄱ
    return rec_cord  # 좌표만 리턴 할게용


rec = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
cx, cy = 1, 3
ix, iy = 7, 8

np.set_printoptions(threshold=sys.maxsize)
# print(np.array(solution(rec, cx, cy, ix, iy)))
print(solution([[1, 1, 4, 4], [2, 2, 5, 5], [3, 3, 7, 8]], 1, 1, 5, 3))

# minx, miny, maxx, maxy = [1,1,7,7]
# count = [maxy - miny, maxx - minx]
# move_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우리가 생각하는 그래프(row, column) 이 아닌 좌표 x, y 축 상을 기준으로
# x, y = minx, miny
#
# for i, cord in enumerate(move_direction):
#     k = i % 2
#     for _ in range(count[k]):
#         x += cord[0]
#         y += cord[1]
#         print(x, y)
