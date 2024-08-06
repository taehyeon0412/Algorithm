# 1697번
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 문제
# 큐를 이용한 BFS 풀이

from collections import deque
import sys
input = sys.stdin.readline

# 수빈과 동생의 위치 입력 받음
N, K = map(int, input().split())

# 최대 위치 크기
maps = 100000

# 현재 위치, 시간
queue = deque([(N, 0)])

# 방문 여부 및 시간 배열
visited = [0] * (maps + 1)  # 0은 방문 안 함, 1은 방문 함

# BFS 탐색
while queue:
    current, time = queue.popleft()

    # 동생을 찾으면 시간을 기록하고 종료
    if current == K:
        print(time)
        break

    # 다음 위치 탐색
    next_positions = [current - 1, current + 1, current * 2]

    for next_position in next_positions:
        if 0 <= next_position <= maps and not visited[next_position]:
            # 큐에 추가하고 방문 표시
            queue.append((next_position, time + 1))
            visited[next_position] = 1
