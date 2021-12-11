# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    # 여기에 else 를 박아두면, 처음에 바로 부모노드가 자신이 아니라면, 리턴값이 없게 된다.!!!
    return parent[x]

def union_parent(parent, x, y):   ## 이 부분이 책의 코드와 살짝 다름
    ## 루트노드가 아닌 애들끼리 붙었을때, 지들끼리 비교해서 부모노드를 바꿔버리면 개 무쓸모에요!!!
    print('union',x, y)
    x, y = find_parent(parent, x), find_parent(parent, y)
    print('if', x, y)
    if x > y:  # 내 코드가 나을 듯.
        parent[x] = y
    else:
        parent[y] = x
    print(parent)

v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종비용을 담을 함수
result = 0
edges = [] # 노드 vertex, 간선 edge

for i in range(1, v + 1): # 부모노드를 자신으로 초기화
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 비용순으로 정렬하기 위해서 비용을 첫번째 아이템으로

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent, b): # 사이클이 아닌 경우
        result += cost # 비용저장
        union_parent(parent, a, b) # 같은 집합으로 합친다.



print(result)

for i in range(1, v + 1):
    find_parent(parent, i)
print(parent)

