# 최소 힙을 사용하여 연산 문제
# 0이 아닐 때 최소 힙에 추가
# 0일 때 가장 작은 값을 출력 / 힙이 비어있다면 0 출력

import sys
import heapq
input = sys.stdin.readline

# 연산 개수 N 입력 받음
N = int(input().strip())

# 최소 힙 리스트
heap = []

# 연산
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)


# O(N log N)