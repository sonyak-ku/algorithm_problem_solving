from itertools import combinations

def solution(line):
    combi = list(combinations(line, 2)) # 선분들을 두개씩 묶어서
    cords = [check_int_or_float(find_intersection(lines[0], lines[1])) for lines in combi] # 정수 좌표들 바로 출력(None) 포함되어잇음
    int_cords = [cord for cord in cords if cord is not None]
    return express_cords_in_graph(int_cords)

def find_intersection(list_a, list_b):# Ax + By + C = 0 이라 할때 [A, B, C] 의 형태의 리스트가 두개 파라미터로 들어간다
    first_a, first_b, first_c = list_a
    second_a, second_b, second_c = list_b  # 좌표를 일단 풀자

    if first_a == 0 and second_a == 0:
        return
    if first_b == 0 and second_b == 0: # 둘 다 0일 때 -> 수펼
        return
    # 수평인 케이스 사라졋고! 상수+상수, 상수+직선, 직선+직선 케이스 남음
    if first_a != 0 and first_b != 0: # 첫번째 선분이 직선형태일때
        if second_a != 0 and second_b != 0: # 두번째 선분이 직선형태 일때
            x = (first_c / first_b - second_c / second_b) / (-first_a / first_b + second_a / second_b)
            y = (-first_a / first_b) * x - first_c / first_b  # 수학적으로 아에 풀어서 좌표 구하는 식 완성
            return [x, y]
        elif second_a == 0: # y = -C/B 의 형태일때
            y = -second_c/second_b
            x = (-first_b * y - first_c) / first_a
            return [x, y]
        elif second_b == 0: # x = -C/A
            x = -second_c/second_a
            y = (-first_a * x - first_c) / first_b
            return [x, y]
    elif first_a == 0:
        if second_b == 0: # 둘이 수직 일 때
            x = -second_c/second_a
            y = -first_c/first_b
            return [x, y]
        else: # second 가 직선형태
            y = -first_c / first_b
            x = (-second_b * y - second_c) / second_a
            return [x, y]
    elif first_b == 0:
        if second_a == 0:
            x = -first_c / first_a
            y = -second_c / second_b
            return [x, y]
        else:
            x = -first_c / first_a
            y = (-second_a * x - second_c) / second_b
            return [x, y]


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
    return final_graph
# a = 3.0
# b = 4.9  --> int 형변환 하면 소수부가 자동으로 0 처리가 된다.
# print(a == int(a)) #True
# print(b == int(b)) #False

# print(check_int_or_float(find_intersection([3, 1, -1], [0, 1, 1])))
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))