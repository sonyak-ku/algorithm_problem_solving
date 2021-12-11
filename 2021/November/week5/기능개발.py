from collections import deque


def solution(progresses, speeds):
    answer = []
    pro = deque(progresses)
    sp = deque(speeds)
    while pro:
        count = 0
        for i in range(len(sp)):  # 하루동안 작업진행
            if pro[i] == 100:
                continue
            pro[i] = pro[i] + sp[i]
            if pro[i] > 100:
                pro[i] = 100

        # 작업 완료된것 있는지 체크
        if pro[0] == 100:
            print(pro, 'up')
            while pro and pro[0] == 100: # 덱이 존재하고 첫째 값이 100일때 --> 아래에서while 문돌다가 덱이 비었을 때 탈출하게끔 도와줌
                count += 1
                pro.popleft(), sp.popleft()
                print(pro, 'middle')
            print('out')
            answer.append(count)
        # pro.popleft(), sp.popleft()

    return answer

print(solution([93, 30, 55],[1, 30, 5]))