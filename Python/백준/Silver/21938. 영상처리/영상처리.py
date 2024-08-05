# 21938번
# 화면에서 물체가 총 몇 개 있는지 구하는 문제
# stack을 이용한 DFS 구현 풀이
# 3가지 색상 평균이 T보다 크거나 같으면 255, 작으면 0 / 255인 픽셀은 물체로 인식

import sys
input = sys.stdin.readline

# 세로, 가로 입력 받음
M, N = map(int, input().split())

# 픽셀 정보 입력 받음
pixels = [list(map(int, input().split())) for _ in range(M)]

# 경계값 입력
T = int(input().strip())

count = 0

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 이진화 리스트
img = []

# 이진화로 변경하기
for row in pixels:
    img_row = []
    # 각 줄마다 3개씩 묶기
    for R, G, B in zip(row[0::3], row[1::3], row[2::3]):
        # 평균
        avg = (R + G + B) / 3
        img_row.append(255 if avg >= T else 0)

    img.append(img_row)

# DFS 탐색
for i in range(M):  # M은 행의 개수
    for j in range(N):  # N은 열의 개수
        if img[i][j] == 255:
            stack = [(i, j)]
            img[i][j] = 0  # 방문표시

            while stack:
                x, y = stack.pop()

                for dx, dy in move:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < M and 0 <= ny < N and img[nx][ny] == 255:
                        img[nx][ny] = 0  # 방문 표시
                        stack.append((nx, ny))
            count += 1

print(count)
