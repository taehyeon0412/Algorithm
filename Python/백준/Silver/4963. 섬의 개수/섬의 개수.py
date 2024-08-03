# 섬의 개수를 구하는 문제
# 연결된 섬은 1개로 친다
""" 
1 1           - w,h
0
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0           -입력의 마지막 줄에는 0이 두 개 주어진다.
"""

import sys
input = sys.stdin.readline

while True:
    # 행, 열 입력 받음
    W, H = map(int, input().split())

    # 00일 때 종료
    if W == 0 and H == 0:
        break

    # 맵 입력 받음
    maps = [list(map(int, input().split())) for _ in range(H)]

    # 인접한 이동 방향 (위, 아래, 왼, 오, 대각선)
    nearby = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # 풀 무더기 개수 초기값
    count = 0

    # 1행씩 순차적으로 탐색함
    # 섬을 발견하면 DFS를 사용하여 해당 영역의 연결된 섬을 탐색함
    for i in range(H):  # 행
        for j in range(W):  # 열
            if maps[i][j] == 1:  # 땅 발견
                stack = [(i, j)]
                maps[i][j] = 0  # 방문 표시

                while stack:
                    x, y = stack.pop()
                    for nearby_x, nearby_y in nearby:
                        nx, ny = x + nearby_x, y + nearby_y
                        if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] == 1:
                            maps[nx][ny] = 0  # 방문한 땅을 바다로 변경
                            stack.append((nx, ny))
                count += 1

    print(count)
