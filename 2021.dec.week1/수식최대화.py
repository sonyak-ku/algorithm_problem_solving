import re # 확실히 카카오 인턴문제는 뭔가 어렵긴하네
from itertools import permutations


def solution(expression):
    answer = 0
    numbers = list(map(int, re.findall('\d+', expression)))
    sign_order = re.findall('\D', expression)

    sign_list = list(permutations(set(signs), 3))

    for signs in sign_list:  # 우선 순위대로 나열된 사인들
        ans = 0
        dummy_sign = sign_order  # ['+', '-']
        dummy_number = numbers  # [300, 200,100]
        for sign in signs:  # 먼저 처리해야하는 사인을 먼저 나열해줌 ex: '+'
            for i in len(dummy_sign):
                if dummy_sign[i] == sign:
                    a, b = dummy_number.pop(i), dummy_number.pop(i)
                    if sign == '+':
                        dummy_number

    return max(answer)