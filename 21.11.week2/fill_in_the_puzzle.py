import numpy as np


def fill_in_the_puzzle(gameboard, table):
    pass


def find_board(map, numbers):  # numbers :(찾아야되는 공간, 지나가야하는 공간) -> 게임보드와, 테이블이 다르기에, 같은 함수 재활용위해
    board_bundles = []
    visited = []
    find, no_find = numbers[0], numbers[1]
    index_limit = len(map) - 1
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r, row in enumerate(map):  # 연속된 보드 좌표 찾기 시작
        for c, item in enumerate(row):
            if [r, c] in visited:  # 찾아야 하는 것들만 방문처리를 할 예정, 안겹치게끔
                continue
            elif item == no_find:  # 처음 만나는 곳이 찾을 필요없는곳일때
                continue
            elif item == find:
                one_piece = []  # 보드의 좌표 연속체 담기 위해
                dfs_stack = []  # dfs 사용 - 스택 이용
                dfs_stack.append([r, c])
                # 상하좌우 탐색
                while dfs_stack:
                    p = dfs_stack.pop()  # 깊이 탐색할 보드 좌표 하나 팝 [r, c]
                    if p in visited:
                        continue
                    visited.append(p)  # 방문처리
                    one_piece.append(p)  # 좌표 담기
                    for i in range(4):  # 상하좌우에 find 있으면 dfs 스택에 넣는 용도
                        nr, nc = p[0] + direction[i][0], p[1] + direction[i][1]
                        # print(f'p: {p}, [nr, nc]: {[nr, nc]}')
                        if index_limit >= nr >= 0 and index_limit >= nc >= 0:  # 탐색좌표가 맵안의 제대로 된 좌표면, 파이썬은 크기비교 한번에 가능
                            if map[nr][nc] == find:
                                dfs_stack.append([nr, nc])  # 여기서 dfs 탐색은 끝난듯?

                board_bundles.append(one_piece) # dfs 탐색이 끝나서 한조각이 찾아지면 그 좌표를 보드 번들에 넣기

    return board_bundles


def make_board_as_rectangle(one_piece_coordinates):  # 여러 좌표들로 이루어진 보드를, 가공해 에워싸는 사각형 덩어리로 리턴하는 함수
    pass


def rotate_bundle(bundle):  # 이중리스트 90도로 한번 시계방향으로 회전한 것을 리턴하기, 이중리스트에 직접변화를 일으키도록 애초에 할 수 없겟다.-> 끝!!!
    # 하면 반복 도중에 값이 변해서 원하는대로 안될듯
    nr, nc = len(bundle[0]), len(bundle)  # 세로길이가 새로운 리스트의 가로길이가 되고, 가로길이가 세로길이가 됨

    new_bundle = [[0 for _ in range(nc)] for _ in range(nr)]
    for r, row in enumerate(bundle):
        for c, item in enumerate(row):
            new_bundle[c][nc - r - 1] = item  # 이거 그냥 손으로 좌표써서 규칙 발견했으면 훨씬 쉽게 풀었을듯

    return new_bundle


board = [[1, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0, 1],
         [1, 1, 0, 1, 1, 1],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0]]

# print(find_board(board, (0, 1))) # find_board 동작 체크

# print(np.array(rotate_bundle(board))) # rotate_bundle 동작 체크

# table = [[1, 0, 0, 1, 1, 0],
#          [1, 0, 1, 0, 1, 0],
#          [0, 1, 1, 0, 1, 1],
#          [0, 0, 1, 0, 0, 0],
#          [1, 1, 0, 1, 1, 0],
#          [0, 1, 0, 0, 0, 0]]
#
# print(fill_in_the_puzzle(board, table))
