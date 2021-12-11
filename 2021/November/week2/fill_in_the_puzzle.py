import numpy as np
import copy


def fill_in_the_puzzle(game_board, table):
    answer = 0
    empty_game_board = find_board(game_board, [0, 1])
    table_board_pieces = find_board(table, [1, 0])
    filled_piece = []  # 이미 채운 덩어리는 다시 검사 안하도록
    filled_space = []  # 이미 채운 보드 공간
    # 테이블 보드 덩어리들을 사각형 형태로 저장한다
    rec_table_pieces = [make_board_as_rectangle(piece) for piece in table_board_pieces]
    # 마찬가지로 게임보드 덩어리도
    rec_game_board_empty_spaces = [make_board_as_rectangle(space) for space in empty_game_board]
    # 일치 불일치 검사 하면 끝 - 한쪽을 회전하며 일치불일치 검사.( 이미 검사한 것은 다음 검사를 굳이 안해도 된다는점 체크 )

    for space_number, spaces in enumerate(rec_game_board_empty_spaces):  # 공간을 기준으로 for 문 돌려서 맞으면 break 터져야 되는데 -> for 문이 세개나 잇어서 그럼(원하는건 두번째 forwhdfy)
        for piece_number, pieces in enumerate(rec_table_pieces):
            if space_number in filled_space: ## 얘는 어짜피 채워지면 다시는 반복문에 ---> 얘도 같은 방식의 오류 있을 수 있음 --> 쓸모가 없는 코드라고생각하긴해 인덱스로 처리
                break
            if piece_number in filled_piece: ##### 여기서 문제 발생했을 듯, (0, 0)으로 초기화했으면 다른 좌표 출신이 같은 모양이 되어 똑같이 예외처리 될수 잇음
                continue   ##-> 해결하기위해 객체 넘버로 저장!
            else:
                boar = pieces[1]
                for i in range(4):  # 4방향 검사
                    if boar == spaces[1]:  # 공간이 딱 맞으면
                        answer += spaces[0]
                        filled_piece.append(piece_number)
                        filled_space.append(space_number)
                        # print(f"what was fitted?: piece: {pieces}, space: {spaces}, added_sum: {spaces[0]}")
                        break  # 이 for 문 탈출
                    else: # 조각이 맞지 않을 때
                        boar = rotate_bundle(boar)

    return answer


# return board_bundles
def find_board(maps, numbers):  # numbers :(찾아야되는 공간, 지나가야하는 공간) -> 게임보드와, 테이블이 다르기에, 같은 함수 재활용위해
    board_bundles = []
    visited = []
    find, no_find = numbers[0], numbers[1]
    index_limit = len(maps) - 1
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r, row in enumerate(maps):  # 연속된 보드 좌표 찾기 시작
        for c, item in enumerate(row):
            if [r, c] in visited:  # 찾아야 하는 것들만 방문처리를 할 예정, 안겹치게끔
                continue
            elif item == no_find:  # 처음 만나는 곳이 찾을 필요없는곳일때
                continue
            elif item == find:
                one_piece = []  # 보드의 좌표 연속체 담기 위해
                dfs_stack = [[r, c]]  # dfs 사용 - 스택 이용
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
                            if maps[nr][nc] == find:
                                dfs_stack.append([nr, nc])  # 여기서 dfs 탐색은 끝난듯?

                board_bundles.append(one_piece)  # dfs 탐색이 끝나서 한조각이 찾아지면 그 좌표를 보드 번들에 넣기

    return board_bundles


# return =[sum, rec(아중리스트)]
def make_board_as_rectangle(one_piece_coordinates):  # 여러 좌표들로 이루어진 보드를, 가공해 에워싸는 사각형 덩어리와, 조각의 개수로 리턴하는 함수
    rectangle = []  # sum :조각의 합, 사각형 : 사각형
    rectangle.append(len(one_piece_coordinates))
    r = sorted(one_piece_coordinates)  # 새로 만들 사각형의 r의 길이
    c = sorted(one_piece_coordinates, key=lambda x: x[1])  # 새로 만들 사각형의 c의 길이
    nr, nc = r[-1][0] - r[0][0] + 1, c[-1][1] - c[0][1] + 1
    min_r, min_c = r[0][0], c[0][1]  # 좌표를 최소화시키려구-최대한 (0,0)과 가깝게 이동시키기 위해서
    new_piece = copy.deepcopy(one_piece_coordinates)
    new_piece = list(map(lambda x: [x[0] - min_r, x[1] - min_c], new_piece))
    rec = [[0 for j in range(nc)] for i in range(nr)]  # 반환할 사각형 0으로 채워놓고
    for piece in new_piece:
        r, c = piece[0], piece[1]
        rec[r][c] = 1  # 좌표를 0에서 1로 바꾸어 준다

    rectangle.append(rec)
    return rectangle


def rotate_bundle(bundle):  # 이중리스트 90도로 한번 시계방향으로 회전한 것을 리턴하기, 이중리스트에 직접변화를 일으키도록 애초에 할 수 없겟다.-> 끝!!!
    # 하면 반복 도중에 값이 변해서 원하는대로 안될듯
    nr, nc = len(bundle[0]), len(bundle)  # 세로길이가 새로운 리스트의 가로길이가 되고, 가로길이가 세로길이가 됨

    new_bundle = [[0 for _ in range(nc)] for _ in range(nr)]
    for r, row in enumerate(bundle):
        for c, item in enumerate(row):
            new_bundle[c][nc - r - 1] = item  # 이거 그냥 손으로 좌표써서 규칙 발견했으면 훨씬 쉽게 풀었을듯

    return new_bundle


# dummy = [[4, 3], [5, 3], [5, 4], [5, 2]]
# p = make_board_as_rectangle(dummy)
# print(p)
# print(rotate_bundle(p['rec']))
# board = [[1, 1, 0, 0, 1, 0],
#          [0, 0, 1, 0, 1, 0],
#          [0, 1, 1, 0, 0, 1],
#          [1, 1, 0, 1, 1, 1],
#          [1, 0, 0, 0, 1, 0],
#          [0, 1, 1, 1, 0, 0]]

# print(find_board(board, (0, 1))) # find_board 동작 체크

# print(np.array(rotate_bundle(board))) # rotate_bundle 동작 체크

# table = [[1, 0, 0, 1, 1, 0],
#          [1, 0, 1, 0, 1, 0],
#          [0, 1, 1, 0, 1, 1],
#          [0, 0, 1, 0, 0, 0],
#          [1, 1, 0, 1, 1, 0],
#          [0, 1, 0, 0, 0, 0]]

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

print(fill_in_the_puzzle(board, table))

