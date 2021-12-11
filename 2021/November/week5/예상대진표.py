def solution(n, a, b):  # N 이 100만임 nlog n 이하로 풀어야댐


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    count = 0
    A, B = a, b
    while A != B:

        A = (A + 1) // 2
        B = (B + 1) // 2

        count += 1  # 우승해서 번호가 줄어든 것.

    return count