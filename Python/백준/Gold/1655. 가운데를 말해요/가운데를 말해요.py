# 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 문제
# 최대힙, 최소힙 사용 풀이
# 최대힙 = 중간값 이하 저장 / 최소힙 = 중간값 이상 저장

import heapq
import sys
input = sys.stdin.readline

# N 입력 받음
N = int(input().strip())

# heap 초기값
max_heap = []
min_heap = []

for _ in range(N):
    num = int(input().strip())

    # 최대 힙과 최소 힙의 크기 조정 및 삽입
    if len(max_heap) == len(min_heap):
        # 최대 힙에 값을 추가 (음수로 저장하여 최대 힙처럼 사용)
        heapq.heappush(max_heap, -num)
    else:
        # 최소 힙에 값을 추가
        heapq.heappush(min_heap, num)

    # 힙의 루트 값 비교 및 교환
    if min_heap and -max_heap[0] > min_heap[0]:
        # 최대 힙의 루트 값이 더 크면 두 힙의 루트 값을 교환
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # 현재 중간값 출력 (최대 힙의 루트 값)
    print(-max_heap[0])
