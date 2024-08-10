# 1389번
# 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램 문제
# 여러 명일 경우에는 번호가 가장 작은 사람을 출력
# 큐를 이용한 BFS 풀이

""" 
사용자 1:
2까지: 1 → 3 → 2 (2단계)
3까지: 1 → 3 (1단계)
4까지: 1 → 4 (1단계)
5까지: 1 → 4 → 5 (2단계)
합: 2 + 1 + 1 + 2 = 6

사용자 2:
1까지: 2 → 3 → 1 (2단계)
3까지: 2 → 3 (1단계)
4까지: 2 → 3 → 4 (2단계)
5까지: 2 → 3 → 4 → 5 (3단계)
합: 2 + 1 + 2 + 3 = 8

사용자 3:
1까지: 3 → 1 (1단계)
2까지: 3 → 2 (1단계)
4까지: 3 → 4 (1단계)
5까지: 3 → 4 → 5 (2단계)
합: 1 + 1 + 1 + 2 = 5

사용자 4:
1까지: 4 → 1 (1단계)
2까지: 4 → 3 → 2 (2단계)
3까지: 4 → 3 (1단계)
5까지: 4 → 5 (1단계)
합: 1 + 2 + 1 + 1 = 5

사용자 5:
1까지: 5 → 4 → 1 (2단계)
2까지: 5 → 4 → 3 → 2 (3단계)
3까지: 5 → 4 → 3 (2단계)
4까지: 5 → 4 (1단계)
합: 2 + 3 + 2 + 1 = 8

3번 4번이 숫자 5로 가장 작은데 
번호가 가장 작은 사용자가 나오게 해야 되니까 답은 3번

"""

from collections import deque
import sys
input = sys.stdin.readline

# 사용자 수와 친구 관계 수 입력
N, M = map(int, input().split())

# 그래프를 인접 리스트로 표현
# 사용자의 친구 목록 저장
friend_list = [[] for _ in range(N)]

# 반복문을 이용하여 각 친구 관계를 입력 받음
# 친구는 양방향이므로 (1,2)이면 (2,1)로도 됨
for _ in range(M):
    A, B = map(int, input().split())
    friend_list[A-1].append(B-1)
    friend_list[B-1].append(A-1)

# 초기값을 무한대(inf)로 설정
min_number = float('inf')

# 사용자는 1부터 시작함
# -1은 아무 사용자도 선택하지 않은 상태를 나타냄
best_min = -1

# 모든 사용자에 대해 BFS 수행
for i in range(N):
    # 각 사용자에 대해 최단 거리를 계산할 리스트 초기화
    distances = [-1] * N  # -1은 아직 방문하지 않았음을 의미
    distances[i] = 0  # 시작 노드의 거리는 0으로 설정

    # BFS를 위한 큐 초기화 (시작노드)
    queue = deque([i])

    # BFS 탐색 시작 / 큐가 빌 때까지 반복
    while queue:
        current = queue.popleft()

        for neighbor in friend_list[current]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 경우
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    # 현재 사용자에 대한 케빈 베이컨 수 계산
    bacon_number = sum(distances)

    # 가장 작은 케빈 베이컨 수를 가진 사용자 갱신
    if bacon_number < min_number:
        min_number = bacon_number
        best_min = i + 1  # 1-based index로 변환

# 결과 출력
print(best_min)
