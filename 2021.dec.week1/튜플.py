def solution(s):  ## set 은 자동정렬 자동중복제거 구나
    dic = {
        0: []
    }
    tmp_w = ''
    l = 0
    count = 0

    for w in s:

        if w == '{':
            tmp_list = [0]  # 초기화...랄까?
            count = 0

        elif w == '}':
            # print(count + 1, tmp_list)
            dic[count + 1] = tmp_list
            if count + 1 > l:
                l = count + 1
            tmp_list = []
            count = -100

        elif w == ',':
            count += 1
            tmp_list.append(0)
            tmp_w = ''
            # print(',',tmp_list, count)

        else:  # 숫자형태들
            tmp_w += w
            tmp_list[count] = int(tmp_w)
            # print('number',tmp_list, count)

    answer = []

    for i in range(1, l + 1):
        a = list(set(dic[i]) - set(dic[i - 1]))
        answer.append(a.pop())
    return answer