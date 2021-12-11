from collections import deque


def solution(s):
    words = [i for i in s]
    words = deque(words)
    count = 0

    if len(s) % 2 == 1:  # 홀수라면
        return 0

        ## 덱을 길이만큼 rotate 한다.
    for i in range(len(s)):
        words.rotate(-1)  # 왼쪽으로 밀기
        # print(words)
        stack = []
        # 4번을 스택으로 판단 (대괄혼지, 중괄혼지, 소괄혼지, 그게 아니라면 pop을 해서 사라질수 있는지)
        for word in words:
            if word == '[':
                stack.append(']')
            elif word == '{':
                stack.append('}')
            elif word == "(":
                stack.append(')')
            else:  # 반대모양이 나왔다는 뜻
                if stack:  # 스택안의것 파악
                    if not word == stack.pop():  # 실패한 모양이라면
                        break
                else:  # 스택이 비었는데 빼야되므로 실패한 모양
                    break
        else:  # break 안되고 무사히 끝났다면
            count += 1

    return count