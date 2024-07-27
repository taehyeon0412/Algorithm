# 숫자 카드 묶음을 최소 비교 횟수로 합치는 문제
# 최소힙 사용

import sys
import heapq
input = sys.stdin.readline

# N 입력 받음
N = int(input().strip())

# 최소 힙 초기값
heap = []

# 카운트 초기값
count = 0

# 카드 묶음 최소 힙에 추가
for _ in range(N):
    card = int(input().strip())
    heapq.heappush(heap, card)

while len(heap) > 1:
    # 가장 작은 2개 꺼내고 합침
    heap_sum = heapq.heappop(heap) + heapq.heappop(heap)
    count += heap_sum  # 카운트 추가
    heapq.heappush(heap, heap_sum)  # 합친 것 힙에 추가

print(count)

# 힙의 크기가 1보다 클 때까지 반복
# 힙에서 가장 작은 2개를 꺼내서 합치고 다시 힙에 넣음
# 합치는 데 필요한 횟수 누적