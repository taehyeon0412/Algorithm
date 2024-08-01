# 16173번
# 쩰리가 정사각형 구역 내에서 움직이며 게임의 승리 지점에 도달할 수 있는지 판단 문제
# 오른쪽이나 아래로 이동가능 위나 왼쪽으로 이동 불가
# 이동 가능한 칸의 수는 반드시 해당 칸에 적힌 숫자만큼

import sys
input = sys.stdin.readline

# 게임 구역 크기 입력 받음
N = int(input().strip())

# 게임판 입력 받음
board = [list(map(int, input().strip().split())) for _ in range(N)]

# 시작점 스택 초기값
stack = [(0, 0)]

# 결과 초기값
result = "Hing"

# 스택이 빈값일 때까지 계속 DFS 탐색
while stack:
    # 현재위치 pop으로 받음
    x, y = stack.pop()

    # 도달 여부 / 도달 했으면 break로 빠져나감
    if board[x][y] == -1:
        result = "HaruHaru"
        break

    # 현재 위치의 이동 가능한 수
    move = board[x][y]

    # 현재 위치 방문 처리 / 0로 변경
    board[x][y] = 0

    # 오른쪽 이동
    ny = y + move
    # ny가 게임판 범위 내에 있고 방문하지 않은 위치라면
    # 스택에 새로운 위치를 추가
    if ny < N and board[x][ny] != 0:
        stack.append((x, ny))

    # 아래쪽 이동
    nx = x + move
    if nx < N and board[nx][y] != 0:
        stack.append((nx, y))


print(result)


""" 
DFS(Depth-First Search, 깊이 우선 탐색)는 
그래프나 트리에서 한 노드로부터 출발하여 최대한 깊게 탐색하다가 
더 이상 갈 곳이 없으면 돌아와서 다른 경로를 탐색하는 알고리즘입니다.

탐색 방식: 한 경로를 끝까지 탐색한 후에 다른 경로를 탐색합니다.
스택 사용: 재귀 호출이나 명시적인 스택을 사용하여 구현할 수 있습니다.
응용 분야: 경로 찾기, 연결 요소 찾기, 사이클 검출, 미로 찾기 등 다양한 문제에 응용됩니다.
"""
