def solution(w, h):  # 두 숫자의 최대공약수 찾기 but 숫자가 1억!   --> 유클리드 호제법을 직접 사용해본 최초의문제
    # 유클리드 호제법을 사용
    # a 를 b 로 나눈 나머지가 r 이라고 할때 (a > b)
    # a 와 b 의 최대공약수는, b 와 r 의 최대공약수와 같다
    a, b = max(w, h), min(w, h)
    gcd = 0
    while a >= b:  # 최대공약수를 구했다.
        r = a % b

        if r == 0:
            gcd = b
            break

        a, b = b, r

    # 선이 그어진 뭉탱이의 수가 gcd 만큼의 수라는 것
    # 선이 그어진 블락의 수는 (W + h - gcd)
    print('gcd:', gcd)
    answer = (w * h) - (w + h - gcd)
    return answer