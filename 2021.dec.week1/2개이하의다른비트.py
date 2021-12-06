def solution(numbers):
    answer = []

    def find_min_target(s):  # 스트링형태의 이진수 들어옴, 이진수를 10진수형태, int('0bxxx', 2)
        zero = -1
        one = -1
        ans = ''
        # print(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':  # 가장 낮은 단위에서 숫자 올릴 수 있을 때
                zero = i
                break
            else:
                one = i  # 가장 큰 1의 위치를 저장

        if one == 0:  # 전부 1이라는 뜻
            ans = '10' + s[1:]
        else:  # 전부 1이 아닐때 0을 1로 바꾸어 주고 가능하다면 1을 0으로 바꾸어준다
            if one == -1:
                ans = s[0: zero] + '1' + s[zero + 1:]
            else:
                ans = s[0: zero] + '1' + s[zero + 1: one] + '0' + s[one + 1:]

        ans = '0b' + ans

        return int(ans, 2)

    for i in numbers:
        s = format(i, 'b')
        answer.append(find_min_target(s))

    return answer
