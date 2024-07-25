# 큐 자료구조를 구현하는 문제
# 라이브러리 collections.deque 사용
# deque는 큐와 덱(deque, 양방향 큐)을 모두 지원하는 자료구조
# 큐는 선입선출(FIFO) 먼저 들어온게 먼저 나감

from collections import deque
import sys
input = sys.stdin.readline

# N 입력 받기 (명령의 수)
N = int(input().strip())

# 큐 초기화
queue = deque()

# for문을 이용하여 action 처리
for _ in range(N):
    action = input().strip().split()

    if action[0] == "push":
        # "push X" 명령: 정수 X를 큐에 넣음
        queue.append(int(action[1]))

    # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
    elif action[0] == "pop":
        # 큐가 비어있지 않으면 가장 앞의 정수를 출력
        if queue:
            print(queue.popleft())
            # 큐가 비어있으면 -1 출력
        else:
            print(-1)

    # 큐에 들어있는 정수의 개수를 출력
    elif action[0] == "size":
        print(len(queue))

    # 큐가 비어있으면 1, 아니면 0을 출력
    elif action[0] == "empty":
        print(1 if not queue else 0)

     # 큐의 가장 앞에 있는 정수를 출력
    elif action[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    # 큐의 가장 뒤에 있는 정수를 출력
    elif action[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

# O(N)