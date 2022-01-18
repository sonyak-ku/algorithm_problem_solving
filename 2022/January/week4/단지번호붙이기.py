N = int(input())
maps = [list(input()) for _ in range(N)] # str 형태의 0과 1로 지도 받기 성공
answer = []
total_house = 0

for r, row in enumerate(maps):
    for c, house in enumerate(row):
        #탐색 시작
        if house != '1':
            continue
        else: # 단지탐색시작
            total_house += 1
            stack = [(r, c)]
            count = 0
            while stack:
                cur_r, cur_c = stack.pop()
                if maps[cur_r][cur_c] == '1':
                    maps[cur_r][cur_c] = 0
                    count += 1
                else:
                    continue

                move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for i in range(4):
                    dr, dc = move[i]
                    new_r, new_c = cur_r + dr, cur_c + dc

                    if 0 <= new_r < N and 0 <= new_c < N: # 옳게된 좌표일때
                        stack.append((new_r, new_c))

            answer.append(count)


answer.sort()
print(total_house)
for j in answer:
    print(j)