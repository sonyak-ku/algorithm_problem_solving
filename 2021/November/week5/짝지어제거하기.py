def solution(s): # s = 100 만 이하의 길이 --> nlogN으로 풀어야 댄다 --> 스택이나 큐로 풀면 시간 복잡도 O(n) 으로 풀수잇다

    def remove_until_finish(s):
        k = s
        while True:
            for i in range(len(k) - 1): # 처음 문자부터 마지막 두번째 문자까지 순서대로 다음 문자와 비교
                if k[i] == k[i + 1]: # 중복된 문자가 있다면
                    k = k[:i] + k[i+2:]
                    # print('here', k)
                    break
            else: # break 가 일어나지 않을 때 : 중복이 없을 때
                # print('for else', len(k))
                if len(k) > 0:
                    return 0
                else:
                    return 1

    answer = remove_until_finish(s)
    return answer