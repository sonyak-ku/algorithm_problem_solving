from collections import Counter, defaultdict
import re


def solution(s):
    l = re.findall('\d+', s)
    k = Counter(l)

    p = sorted(k.items(), key=lambda x: x[1], reverse=True)
    answer = [int(i[0]) for i in p]
    # print(l)
    # print(k)
    return answer