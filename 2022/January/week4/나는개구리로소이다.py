T = int(input())
crying = {'c', 'r', 'o', 'a', 'k'}
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cry = input()
    c, r, o, a, k = 0, 0, 0, 0, 0
    for char in cry:
        if char not in crying:
            k = -1
            break

        if char == 'c':
            if k:
                k -= 1
                c += 1
            else:
                c += 1

        if char == 'r':
            if c:
                c -= 1
                r += 1
            else:
                k = -1
                break

        if char == 'o':
            if r:
                r -= 1
                o += 1
            else:
                k = -1
                break

        if char == 'a':
            if o:
                o -= 1
                a += 1
            else:
                k = -1
                break

        if char == 'k':
            if a:
                a -= 1
                k += 1
            else:
                k = -1
                break

    if c or r or o or a:
        k = -1

    print(f"#{test_case} {k}")
