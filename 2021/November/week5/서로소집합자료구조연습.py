# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    # 여기에 else 를 박아두면, 처음에 바로 부모노드가 자신이 아니라면, 리턴값이 없게 된다.!!!
    return parent[x]

def union_parent(parent, x, y):   ## 이 부분이 책의 코드와 살짝 다름  ---> 내가 틀렸음 의도해서 같은 걸로 박으신듯 ( 크루스칼 알고리즘쪽 참조!!)
    a, b = find_parent(parent, x), find_parent(parent, y)
    if a > b:  # 내 코드가 나을 듯.
        parent[x] = b
    else:
        parent[y] = a

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(v + 1): # 부모노드를 자신으로 초기화
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='') # end = '' 는 나란히 출력되게 해준다.
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
