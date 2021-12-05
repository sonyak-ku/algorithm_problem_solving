from collections import deque


def solution(n, words):
    stack = deque(words)
    used = set()
    previous = stack.popleft()
    used.add(previous)
    count = 1
    while stack:
        w = stack.popleft()
        count += 1

        if w in used:  # 사용된애라면
            if count % n == 0:
                return [n, count // n]

            num, order = count % n, count // n + 1
            return [num, order]

        if w.startswith(previous[-1]):  # 끝말잇기가 잘 된다면
            previous = w  # 지금 단어를 이전 단어에 저장한다.
            used.add(previous)
        else:  # 끝말잇기가 실패했다면
            if count % n == 0:
                return [n, count // n]

            num, order = count % n, count // n + 1
            return [num, order]

    return [0, 0]