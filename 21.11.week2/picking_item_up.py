def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maps = [[0 for j in range(50)] for i in range(50)]  # 걸어 다닐 수 있는 좌표들을 1 로 적을꺼양
    return answer


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


# rec = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]]
# cx, cy = 1, 3
# ix, iy = 7, 8

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