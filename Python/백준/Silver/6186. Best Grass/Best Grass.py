# 풀 무더기 개수 구하기 문제
# #기호 하나 또는 인접한 두 개 이상의 #기호로 이루어진 연결 된 영역

import sys
input = sys.stdin.readline

# Row = 행(가로) / Column 열(세로)
# 행,열 입력 받음
R, C = map(int, input().split())

# 들판 입력 받음
field = [list(input().strip()) for _ in range(R)]

# 인접한 이동 방향 (위,아래,왼,오)
nearby = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0

# 탐색 루프
for i in range(R):
    for j in range(C):
        if field[i][j] == "#":
            stack = [(i, j)]
            field[i][j] = "."

            while stack:
                x, y = stack.pop()
                for nearby_x, nearby_y in nearby:
                    nx, ny = x + nearby_x, y + nearby_y
                    if 0 <= nx < R and 0 <= ny < C and field[nx][ny] == "#":
                        field[nx][ny] = "."
                        stack.append((nx, ny))
            count += 1

print(count)
