import numpy as np
def fill_in_the_puzzle(gameboard, table):
    pass

def find_board_in_table(table): # 빈공간이 0, 채워진 공간이 1
    board_bundles = []
    visited = []

    return board_bundles

def find_board_in_gameboard(board): # 테이블에서 보드 찾는 함수랑 똑같은 함수 ( 단 0을 찾냐, 1을 찾냐 그 차이)
    pass

def rotate_bundle(bundle): # 이중리스트 90도로 한번 시계방향으로 회전한 것을 리턴하기, 이중리스트에 직접변화를 일으키도록 애초에 할 수 없겟다.-> 끝!!!
    # 하면 반복 도중에 값이 변해서 원하는대로 안될듯
    nr, nc = len(bundle[0]), len(bundle)  #세로길이가 새로운 리스트의 가로길이가 되고, 가로길이가 세로길이가 됨

    new_bundle = [[0 for _ in range(nc)] for _ in range(nr)]
    for r, row in enumerate(bundle):
        for c, item in enumerate(row):
            new_bundle[c][nc-r-1] = item    # 이거 그냥 손으로 좌표써서 규칙 발견했으면 훨씬 쉽게 풀었을듯

    return new_bundle

# board = [[1, 1, 0, 0, 1, 0],
#          [0, 0, 1, 0, 1, 0],
#          [0, 1, 1, 0, 0, 1],
#          [1, 1, 0, 1, 1, 1],
#          [1, 0, 0, 0, 1, 0],
#          [0, 1, 1, 1, 0, 0]]

print(np.array(rotate_bundle(board)))
# table = [[1, 0, 0, 1, 1, 0],
#          [1, 0, 1, 0, 1, 0],
#          [0, 1, 1, 0, 1, 1],
#          [0, 0, 1, 0, 0, 0],
#          [1, 1, 0, 1, 1, 0],
#          [0, 1, 0, 0, 0, 0]]
#
# print(fill_in_the_puzzle(board, table))