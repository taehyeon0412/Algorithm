# 1926번
# 도화지에 그려진 그림의 개수와, 넓이가 가장 넓은 그림의 넓이 출력 문제
"""
0: 공백
1: 색칠 된 부분
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
"""

import sys
input = sys.stdin.readline

# 가로, 세로 입력 받음
n, m = map(int, input().split())

# 그림판 입력 받음
maps = [list(map(int, input().split())) for _ in range(n)]

# 인접한 이동 방향 (위, 아래, 왼, 오)
nearby = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 그림 개수 / 최대 넓이
count = 0
max_drawing = 0

# 1행씩 순차적으로 탐색함
# 그림을 발견하면 DFS를 사용하여 해당 영역의 연결된 그림을 탐색함
for i in range(n):  # 행
    for j in range(m):  # 열
        if maps[i][j] == 1:  # 그림 발견
            maps[i][j] = 0  # 방문 표시
            current_drawing = 0  # 현재 그림 넓이
            stack = [(i, j)]

            while stack:
                x, y = stack.pop()
                current_drawing += 1  # 넓이 증가

                for nearby_x, nearby_y in nearby:
                    nx, ny = x + nearby_x, y + nearby_y
                    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                        maps[nx][ny] = 0  # 방문 표시
                        stack.append((nx, ny))
            count += 1
            # max로 더 큰값으로 갱신
            max_drawing = max(max_drawing, current_drawing)

print(count)
print(max_drawing)
