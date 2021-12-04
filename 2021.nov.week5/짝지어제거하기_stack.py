def solution(s): # 스택을 이용하면 그냥 아주 쉽게 풀리는 문제엿다
    stack = []

    for w in s:
        if stack:  # 스택이 있다면
            if stack[-1] == w:
                # print('same!', stack[-1], w)
                stack.pop()
            else:  # 같지 않다면
                stack.append(w)

        else:  # 비어져있다면
            stack.append(w)

    # print(stack)
    if len(stack) > 0:
        return 0
    else:
        return 1