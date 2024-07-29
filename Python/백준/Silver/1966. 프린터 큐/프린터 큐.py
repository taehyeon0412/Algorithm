# 문서의 중요도를 관리하는 문제
# 데큐 사용

from collections import deque
import sys
input = sys.stdin.readline

# 테스트 케이스 입력 받음
T = int(input().strip())

for _ in range(T):
    # 문서 개수 N, 문서 위치 M 입력 받음
    N, M = map(int, input().strip().split())
    # 문서의 중요도 입력 받음
    important = list(map(int, input().strip().split()))
    # 큐 초기화
    queue = deque()

    for i in range(N):
        queue.append((important[i], i))

    # 인쇄 순서 초기값
    print_number = 0

    while queue:
        # 현재 문서의 중요도와 인덱스
        current = queue.popleft()

        # 나머지 문서 중에 현재 문서보다 중요도 높은 문서 확인
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            print_number += 1
            if current[1] == M:
                print(print_number)
                break