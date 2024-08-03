# 21736번
# 캠퍼스에서 만날 수 있는 사람 수 구하기 문제
# 캠퍼스에서 상하좌우 1칸씩만 이동할 수 있음
# 스택을 이용한 DFS구현

from itertools import product
import sys
input = sys.stdin.readline

# 캠퍼스 크기 입력 받음
N, M = map(int, input().split())
# 캠퍼스 지도 입력 받음
maps = [list(input().strip()) for _ in range(N)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0

# 시작 위치를 찾고 스택에 추가
stack = []
for i, j in product(range(N), range(M)):
    if maps[i][j] == 'I':
        stack.append((i, j))
        maps[i][j] = '.'  # 방문 표시
        break

# DFS 탐색
while stack:
    x, y = stack.pop()
    # 이동값을 더해서 새로운 좌표를 만듦
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        # map안에 있는지 확인
        if 0 <= nx < N and 0 <= ny < M:
            if maps[nx][ny] == 'P':
                count += 1
                stack.append((nx, ny))
            elif maps[nx][ny] == 'O':
                stack.append((nx, ny))
            maps[nx][ny] = '.'  # 방문 표시

# 결과 출력
print(count if count else "TT")


""" 
product함수는 
두 개 이상의 시퀀스(여기서는 range(N)와 range(M))를 입력받아 
가능한 모든 조합을 생성하는 함수
이중 루프를 대체
ex)
list1 = [1, 2]
list2 = ['a', 'b']

(1, 'a')
(1, 'b')
(2, 'a')
(2, 'b')
"""