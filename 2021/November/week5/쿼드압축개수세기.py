from collections import defaultdict


def solution(arr):
    num = defaultdict(int)

    def quad_list_split(l: list):  # 리스트를 네개로 쪼개 봅시다
        i = len(l) // 2  # 자르기
        a = [j[i:] for j in l[i:]]
        b = [j[i:] for j in l[:i]]
        c = [j[:i] for j in l[i:]]
        d = [j[:i] for j in l[:i]]
        # print(a, b, c, d, 'here')
        return a, b, c, d

    def quad_find(l: list, n):  # 네개로 쪼갠거를 더해봅시다.
        if len(l) == 1:
            if l[0][0] == 1:
                n[1] += 1
                return
            else:
                n[0] += 1
                return

                # 총 합 구하기
        total = sum(list(map(sum, l)))
        # print(total)
        if total == 0:
            n[0] += 1

            return

        if total == (len(l) ** 2):
            n[1] += 1

            return

        a, b, c, d = quad_list_split(l)
        return quad_find(a, n), quad_find(b, n), quad_find(c, n), quad_find(d, n)

    quad_find(arr, num)

    return [num[0], num[1]]