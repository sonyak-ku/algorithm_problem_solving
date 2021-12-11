import copy
from itertools import product
from copy import deepcopy
def knapsack(weight_cap, weights, values):
    # Write your code here
    weight_value_dict = {}
    for w, v in zip(weights, values):
        if weight_value_dict.get(w, 0):  # in dict
            weight_value_dict[w].append(v)
        else:  # not in dict
            weight_value_dict[w] = [v]   # 리스트를 생각하고 한거라

    q = dict(zip(weights, values))  # 이렇게 한번에 묶어서 dict화 할 수 있네용
    print(q)

    weight_combination = []
    ## 제한된 무게 내에서 무게 조합 짜는게 이렇게 어려운줄을 듯랐네? --> 만들수 있는 모든조합(0, 1) 짜고 sum 이 cap을 넘어버리면 없애는 식으로 플레이해볼까?->0, 1로 중복조합
    ## ->큰무게 부터처리해야 초장에 break되는게 나와서 편할
    weight = sorted(weights, reverse=True)
    p = product([0, 1], repeat=len(weight)) # 0:no_carry, 1:carry
    for _ in p:
        cap = weight_cap
        for i, w in zip(_, weight):
            if i:
                cap -= w
            if cap < 0:
                break
        else:
            weight_combination.append(_)
    max_value = 0
    for group in weight_combination:
        sum = 0
        for i, w in zip(group, weight):
            wvd = copy.deepcopy(weight_value_dict)
            if i:# 무게는 같지만 밸류는 다른 경우를 위해서 ..
                b = wvd[w]
                b.sort()
                sum += b.pop()

        max_value = max(max_value, sum)

    return max_value

weight_cap = 10
weights = [3, 6, 8]
values = [50, 60, 100]
print(knapsack(weight_cap, weights, values))
