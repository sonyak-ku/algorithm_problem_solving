def solution(n):
    ans = 0
    # print(n)
    while n > 1:
        if n % 2 == 0:  # 딱 나누어 떨어지면 0 이 나옴
            n = n // 2
        else:
            n = (n - 1) // 2
            ans += 1
        # print(n)

    return ans + 1


# bin(n).count('1')  # 이진법으로 표시한 다음 1의 개수를 세는 것!