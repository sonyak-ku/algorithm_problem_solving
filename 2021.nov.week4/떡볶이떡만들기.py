# import sys
n, m = map(int, input().split()) #n: 떡의 개수, m: 손님이 요구한 떡의 총 길이
# rice_cakes = set(list(sys.stdin.readline().strip(' '))) # ['1', ' ', '2', ' ', '3', ' ', '4', '\n'] rstrip 이 없으면 개행 문자 생김
#
rice_cakes = map(int, input().split())# iter 리스트 자료형으로 결과물이 나오지만, sys 는 그렇지 않음
# # 긴 한 줄을 받고 싶으면 input 을 쓰고, 매우 많은 여러 줄을 받고 싶으면 sys 를 쓰자.
# print(rice_cakes)
def find_left_rice_cake(limit, cakes):
    leftover = list(map(lambda x: max(0, x - limit), cakes))
    return sum(leftover)

def solution(n, m, cakes):
    pass

print(find_left_rice_cake(15, rice_cakes))