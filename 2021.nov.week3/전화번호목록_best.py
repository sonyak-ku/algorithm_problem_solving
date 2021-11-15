def solution(phoneBook): ## string 의 특징을 교묘하게 살려서 잘 푼 문제
    phoneBook = sorted(phoneBook)
    print(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(f'p1:{p1}, p2:{p2}')
        if p2.startswith(p1):
            return False
    return True


print(solution(['119', '450', '600', '1190']))