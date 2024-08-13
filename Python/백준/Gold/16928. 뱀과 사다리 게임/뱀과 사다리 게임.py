# 16928번
# 100번째 정사각형에 도달하는 데 필요한 최소 주사위 굴림 수를 찾는 문제
# 최단 경로 문제 BFS

from collections import deque
import sys
input = sys.stdin.readline

# 게임의 사다리 수와 뱀의 수를 입력받습니다.
N, M = map(int, input().split())

# 사다리 정보를 저장할 딕셔너리
ladders = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y  # x번 칸에서 y번 칸으로 이동 (x < y)

# 뱀 정보를 저장할 딕셔너리
snakes = {}
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v  # u번 칸에서 v번 칸으로 이동 (u > v)

# 게임판 설정, 각 칸은 자기 자신의 위치로 초기화
board = list(range(101))
for start, end in ladders.items():
    board[start] = end  # 사다리의 시작점을 끝점으로 설정
for start, end in snakes.items():
    board[start] = end  # 뱀의 시작점을 끝점으로 설정

# BFS를 위한 큐 초기화
queue = deque([(1, 0)])  # 시작점 1과 주사위를 0번 굴린 상태로 시작
visited = [False] * 101  # 방문 여부 확인을 위한 리스트
visited[1] = True  # 시작점을 방문했다고 표시

# BFS 실행
while queue:
    current_pos, rolls = queue.popleft()  # 현재 위치와 주사위 굴린 횟수를 가져옴

    for dice in range(1, 7):  # 주사위의 모든 면(1~6)에 대해 시도
        new_pos = current_pos + dice  # 현재 위치에서 주사위 값을 더한 새 위치 계산
        if new_pos > 100:
            continue  # 새 위치가 100을 초과하면 무시 (이동 불가)
        if new_pos == 100:
            print(rolls + 1)  # 100번 칸에 도달하면 주사위 굴린 횟수 출력 후 종료
            exit()

        # 새 위치가 100이 아니고, 아직 방문하지 않은 위치라면
        if not visited[board[new_pos]]:
            visited[board[new_pos]] = True  # 사다리나 뱀을 타고 도달하는 칸을 방문 처리
            # 해당 위치와 주사위 굴린 횟수를 큐에 추가
            queue.append((board[new_pos], rolls + 1))
