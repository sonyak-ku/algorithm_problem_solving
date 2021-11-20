def solution(n, left, right):  # 1초에 2천만번 연산이고, 슬라이싱 한번 있기 때문에 큰 연산 두번이면 2천 안에 해결 가능해
    # 그냥 리스트 크게 짜고 말그대로 슬라이실 하라는 뜻인가?
    # super_big_list = [[max(i, j) + 1 for j in range(n)] for i in range(n)]  # 천만번연산 ==> 애초에 틀렷다 천만 ^ 천만 하고 잇엇네
    make_one_dim_array = []

    # for row in super_big_list:  # 연산 크기가 몇일까? - 천만번연산인듯  -> 여기서 해결하자 : 필요한 부분만 자르는 식으로 총 연산을 줄이자
        # make_one_dim_array = make_one_dim_array + row

    answer = []
    # left 숫자와 right 숫자로 인덱스와 엮어서 해석 가능 할 것 같다. 아까 했듯이
    start_r, start_c = left // n, left % n   # 나눈 몫과 나머지
    # end_r, end_c = right // n, right % n
    for i in range(right - left + 1):
        answer.append(max(start_r, start_c) + 1)
        start_c += 1
        if start_c == n:
            start_c = 0
            start_r += 1




    return 1
