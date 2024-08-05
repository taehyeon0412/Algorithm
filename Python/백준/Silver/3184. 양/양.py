# 3184번
# 아침에 살아남은 양과 늑대의 수를 출력하는 문제
# '.'은 빈 필드, #은 울타리, o는 양, v는 늑대
# 같은 영역에서 양이 많으면 양이 생존, 적거나 같으면 늑대 생존

import sys
input = sys.stdin.readline

# 세로, 가로 입력 받음
R, C = map(int, input().split())

# 마당 입력 받음
maps = [list(input().strip()) for _ in range(R)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

sheep = 0
wolf = 0

# DFS 탐색
for i in range(R):
    for j in range(C):
        # 울타리와 방문한 곳이 아닌 경우
        if maps[i][j] != '#' and maps[i][j] != 'x':
            stack = [(i, j)]

            # 해당 지역 양, 늑대
            local_sheep = 0
            local_wolf = 0

            while stack:
                x, y = stack.pop()

                # 현재 위치 양 늑대 카운트
                if maps[x][y] == 'o':
                    local_sheep += 1
                elif maps[x][y] == 'v':
                    local_wolf += 1

                maps[x][y] = 'x'  # 방문 표시

                for dx, dy in move:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] != '#' and maps[nx][ny] != 'x':
                        stack.append((nx, ny))

            # 결과 갱신
            if local_sheep > local_wolf:
                sheep += local_sheep
            else:
                wolf += local_wolf

print(sheep, wolf)
