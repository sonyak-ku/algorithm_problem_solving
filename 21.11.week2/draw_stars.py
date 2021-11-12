def find_intersection(list_a, list_b):# Ax + By + C = 0 이라 할때 [A, B, C] 의 형태의 리스트가 두개 파라미터로 들어간다
    first_a, first_b, first_c = list_a
    second_a, second_b, second_c = list_b  # 좌표를 일단 풀자
    x = (first_c/first_b - second_c/second_b) / (-first_a/first_b + second_a/second_b)
    y = (-first_a/first_b) * x - first_c/first_b  # 수학적으로 아에 풀어서 좌표 구하는 식 완성
    # 이 식이 b가 0 일 때는 제대로 작동 안하는게 확실 0 으로 나누는 에러 , 반면 a 가 0 일때는 작동 할 수도 잇음 체크 --> a 가 0일때는 작동함.
    print(f'x:{x}, y:{y}')   # 다 float 형식으로 나옴
    # b 가 0 일 때 zerodivision error 나오는 부분 구현하면 끝날듯

# a = 3.0
# b = 4.9  --> int 형변환 하면 소수부가 자동으로 0 처리가 된다.
# print(a == int(a)) #True
# print(b == int(b)) #False

find_intersection([-1, 0, 4], [-1, 1, 0])