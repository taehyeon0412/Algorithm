# 1743번
# 제일 큰 음식물 쓰레기의 크기를 구해서 출력하는 문제

import sys
input = sys.stdin.readline

# 세로, 가로, 쓰레기 개수 입력 받음
N, M, K = map(int, input().split())

# 쓰레기 좌표
garbage = [[0] * M for _ in range(N)]

# 방향
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 최대 음식물 크기
max_garbage = 0

# 쓰레기 좌표 입력 받음
for _ in range(K):
    r, c = map(int, input().split())
    garbage[r-1][c-1] = 1  # 인덱스는 0부터 시작 / 쓰레기 1로 표시


# DFS 탐색
for i in range(N):
    for j in range(M):
        if garbage[i][j] == 1:  # 음식물이 있는 경우
            stack = [(i, j)]
            garbage[i][j] = 0  # 방문 표시
            size = 0  # 현재 음식물 크기

            while stack:
                x, y = stack.pop()
                size += 1  # 크기 증가

                for dx, dy in move:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < N and 0 <= ny < M and garbage[nx][ny] == 1:
                        garbage[nx][ny] = 0  # 방문 표시
                        stack.append((nx, ny))

            max_garbage = max(max_garbage, size)  # 최대 크기 갱신

print(max_garbage)
