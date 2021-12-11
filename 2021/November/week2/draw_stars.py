from itertools import combinations

def solution(line):
    combi = list(combinations(line, 2))# 선분들을 두개씩 묶어서
    inter = []
    for duo in combi:
        result = find_intersection(duo[0], duo[1])
        if result: # None 이 아닐때
            final_result = check_int_or_float(result)
            if final_result:
                inter.append(final_result)


    return express_cords_in_graph(inter)

def find_intersection(list_a, list_b):# Ax + By + C = 0 이라 할때 [A, B, C] 의 형태의 리스트가 두개 파라미터로 들어간다
    a, b, e = list_a
    c, d, f = list_b  # 좌표를 일단 풀자
    if a * d - b * c == 0: # 두 직선은 평행 또는 일치
        return
    else:
        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)
        return (x, y)



    ## 함수 구현 끝
    # 이 식이 b가 0 일 때는 제대로 작동 안하는게 확실 0 으로 나누는 에러 , 반면 a 가 0 일때는 작동 할 수도 잇음 체크 --> a 가 0일때는 작동함.
    ## b 가 0 일 때 zerodivision error 나오는 부분 구현하면 끝날듯
    ## 주어진 두 선분이 수평이 경우도 존재! -> 기울기가 같은 경우 체크
    # return x, y

def check_int_or_float(cord): # 3.0 과 3 은 같다고 나오는 성질을 이용해서 정수형변환 가능한지 아닌지를 리턴
    x = cord[0]
    y = cord[1]
    if x == int(x) and y == int(y):
        return [int(x), int(y)]  # 정수로 형변환 해서 리선
    else:
        return

def express_cords_in_graph(cords : list):
    tr = sorted(cords, key=lambda x: x[1])[-1][1] - sorted(cords, key=lambda x: x[1])[0][1] + 1  # y좌표의 차이가 그래프의 r 의 길이가 된다.
    tc = sorted(cords)[-1][0] - sorted(cords)[0][0] + 1
    maxy, minx = sorted(cords, key=lambda x: x[1])[-1][1], sorted(cords)[0][0]
    final_graph = [['.' for c in range(tc)] for r in range(tr)]
    reordered_cords = list(map(lambda x: [abs(x[1] - maxy), x[0] - minx], cords)) # 리스트좌표 재조정
    for cords in reordered_cords:
        r, c = cords[0], cords[1]
        final_graph[r][c] = '*'

    for i, row in enumerate(final_graph):
        k = ''.join(row)
        final_graph[i] = k

    return final_graph
# a = 3.0
# b = 4.9  --> int 형변환 하면 소수부가 자동으로 0 처리가 된다.
# print(a == int(a)) #True
# print(b == int(b)) #False

# print(check_int_or_float(find_intersection([3, 1, -1], [0, 1, 1])))
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))