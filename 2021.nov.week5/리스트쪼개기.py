l = [[1,2,2,3], [3, 4,5,6], [2,3,5,6], [2,3,6,7]] # 4 by 4 행렬을 2 by 2 행렬 네개로 쪼개보기

# def quad_split(a:list):
#
#
#
#     return 1



one = [i[:2]for i in l[:2]]
two = [i[:2] for i in l[2:]]
print(one)
print(two)