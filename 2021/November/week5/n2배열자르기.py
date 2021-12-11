def solution(n, left, right):  #
    answer = []
    start_index = [left // n, left % n]  # (r , c)
    end_index = [right // n, right % n]

    r, c = start_index
    print(start_index, end_index)
    while start_index != end_index: # 반복횟수가 right - left 인것을 알고있는데 , while 쓴게 실패
        r, c = start_index
        answer.append(max(r + 1, c + 1))
        c += 1
        if c == n:
            start_index[1] = 0
            start_index[0] += 1
        else:
            start_index[1] += 1

    end_point = max(end_index[0] + 1, end_index[1] + 1)
    answer.append(end_point)
    return answer