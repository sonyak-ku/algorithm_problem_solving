import re
def solution(s):
    n = s
    zero_num = 0
    count = 0

    while len(n) > 1:

        re_zero = re.sub('[0]','',n)
        zero_num = zero_num + len(n) - len(re_zero)  # 줄어질 0 개수 저장
        n = len(re_zero) # 0 줄이기.

        n = format(int(n), 'b')  # 이진수 변환 코드 -> str 으로 반환함

        count += 1

    return [count, zero_num]

print(solution("110010101001"))

# print(type(format(8, 'b')))
# print("110010101001001".strip('0'))

# p = "110010101001001"
# k = re.sub('[0]','', p)
# print(type(k))