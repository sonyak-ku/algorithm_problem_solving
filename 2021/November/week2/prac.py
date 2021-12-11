
def solution(game_board, table):
    answer = 0
    empty_game_board = find_board(game_board, [0, 1])
    table_board_pieces = find_board(table, [1, 0])
    filled_piece = []
    filled_space = []
    rec_table_pieces = [make_board_as_rectangle(piece) for piece in table_board_pieces]
    rec_game_board_empty_spaces = [make_board_as_rectangle(space) for space in empty_game_board]
    for board_pieces in rec_game_board_empty_spaces: # 빈칸을 기준으로 하쟝
        for table_pieces in rec_table_pieces: # 책상에 놓인 애들
            if board_pieces in filled_space:
                break # 두번째 반복문 끝내깅
            if table_pieces in filled_piece: ## 여기서 문제 발생했을 듯, (0, 0)으로 초기화했으면 다른 좌표 출신이 같은 모양이 되어 똑같이 예외처리 될수 잇음
                continue # 지나가기



    return answer

# 보드좌표 묶음만 리턴함
def find_board(maps, numbers):  # dfs 를 통해 보드를 탐색한다. numbers (찾을 숫자, 지나갈 숫자)
    find, no_find = numbers[0], numbers[1]
    visited = []
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    limit = len(maps)
    board_bundle = []

    for r, rows in enumerate(maps):
        for c, item in enumerate(rows):
            if item == no_find: continue
            if not [r, c] in visited:
                item_bundle = []
                dfs_stack = [[r, c]]
                while dfs_stack:
                    cord = dfs_stack.pop()
                    if cord in visited:
                        continue
                    visited.append(cord)
                    item_bundle.append(cord)
                    for i in range(4):
                        nr, nc = cord[0] + direction[i][0], cord[1] + direction[i][1]
                        if 0 <= nr < limit and 0 <= nc < limit:
                            if maps[nr][nc] == find:
                                dfs_stack.append([nr, nc])

                    board_bundle.append(item_bundle)

    return board_bundle


def make_board_as_rectangle(one_piece_coordinates):
    one_piece_coordinates.sort()
    nr = one_piece_coordinates[-1][0] - one_piece_coordinates[0][0] + 1
    s_p = sorted(one_piece_coordinates, key=lambda x: x[1])
    nc = s_p[-1][1] - s_p[0][1] + 1
    min_r, min_c = one_piece_coordinates[0][0], s_p[0][1]
    new_piece = list(map(lambda x: [x[0] - min_r, x[1] - min_c], s_p))

    rectangle = [[0 for j in range(nc)] for i in range(nr)]

    for piece in new_piece:
        r, c = piece[0], piece[1]
        rectangle[r][c] = 1  # 좌표를 0에서 1로 바꾸어 준다

    return rectangle


def rotate_bundle(bundle):  # 사각형 회전하는 기능 구현 - 얘는 문제가 아닌듯
    r, c = len(bundle), len(bundle[0])
    new_bundle = [[0 for j in range(r)] for i in range(c)]

    for i, row in enumerate(bundle):
        for j, item in enumerate(row):
            if item == 1:
                new_bundle[j][r - 1 - i] = item  # 반환할 때 1로 채워서 반환을 해주네? 이부분 체크해보기

    return new_bundle

# k = [[3, 2], [4, 2], [4, 3], [4, 1]]
# print(make_board_as_rectangle(k))

board = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
         [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
         [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
         [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
         [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

table = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
         [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
         [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
         [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
         [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
         [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
         [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
         [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]
#
print(solution(board, table))