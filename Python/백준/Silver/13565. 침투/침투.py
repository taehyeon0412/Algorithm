# 13565번
# 첫 줄에서 나온 전류가 마지막 줄까지 이어지는지 확인하는 문제
# stack을 이용한 DFS 구현 풀이

import sys
input = sys.stdin.readline

# 세로, 가로 입력 받음
M, N = map(int, input().split())

# 맵 입력 받음
maps = [list(map(int, input().strip())) for _ in range(M)]

# 이동값
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 스택 및 전기 초기값
stack = []
electric = False

for j in range(N):
    # 흰색에서 시작
    if maps[0][j] == 0:
        stack.append((0, j))
        maps[0][j] = 1  # 방문 표시 / 1로 변경

# DFS 탐색
while stack:
    x, y = stack.pop()

    # 마지막 줄 도착했으면 break
    if x == M - 1:
        electric = True
        break

    # 인접한 방향 탐색
    for dx, dy in move:
        nx, ny = x + dx, y + dy

        # map안에 있고 흰색 격자면 탐색
        if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] == 0:
            maps[nx][ny] = 1  # 방문 표시
            stack.append((nx, ny))

if electric:
    print("YES")
else:
    print("NO")