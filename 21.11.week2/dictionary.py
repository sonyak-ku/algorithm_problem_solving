from itertools import product


def solution(word):
    words = ['A', 'E', 'O', 'I', 'U']
    word_list = []
    for i in range(1, 6):  # 단어 개수 순서대로 뽑기
        word_comb = list(product(words, repeat = i))
        for wo in word_comb:
            word_list.append(''.join(wo))

    word_list.sort()

    return word_list.index(word) + 1

print(solution("AAAAE"))