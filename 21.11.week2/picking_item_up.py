import numpy as np
import sys
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maps = [[0 for j in range(11)] for i in range(11)]  # 걸어 다닐 수 있는 좌표들을 1 로 적을꺼양
    for rec in rectangle: # 사각형의 최소꼭짓점과 최대꼭지점을 하나씩 빼서
        rectangle_line = find_rectangle_coordinates(rec) # 사각형의 변들이 좌표로 되어잇음
        for cord in rectangle_line:
            x, y = cord # 좌표를 풀어
            all_x, all_y = [rec[0], rec[2]], [rec[1], rec[3]]
            if x in all_x and y in all_y: # 사각 형의 꼭짓점에 해당하는 좌표일 때 - 꼭짓점에서는 절대 만나지 않는다는 규칙이 잇으므로
                maps[x][y] = 2 # 꼭짓점은 2로 표시한다
            else: # 꼭짓점이 아닐때 -- 일반 선분이 위치하거나, 교차점이 발생한다.
                if maps[x][y] == 1:
                    maps[x][y] = 3 # 교차점은 3 으로 표시한다.
                else:
                    maps[x][y] = 1 # 일반 선분은 1 로 표시한다.


    return maps


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
    return rec_cord # 좌표만 리턴 할게용



rec = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
cx, cy = 1, 3
ix, iy = 7, 8

np.set_printoptions(threshold=sys.maxsize)
print(np.array(solution(rec, cx, cy, ix, iy)))



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