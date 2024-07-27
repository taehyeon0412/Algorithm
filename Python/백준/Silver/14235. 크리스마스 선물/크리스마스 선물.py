# 숫자 N이 주어졌을 때 차례대로 가치가 가장 큰 선물을 주는 문제
# 최대 힙 사용

import sys
import heapq
input = sys.stdin.readline

# 연산 개수 N 입력 받음
N = int(input().strip())

# 최대 힙 리스트 초기값
heap = []

# 연산
for _ in range(N):
    # 정수로 변환
    a_list = list(map(int, input().strip().split()))

    # 아이들 만남
    if a_list[0] == 0:
        if heap:
            print(-heapq.heappop(heap))  # 최대 힙에서 가장 큰 값을 출력
        else:
            print(-1)  # 힙이 비어있으면 -1출력
    else:
        # 선물 충전
        for gift in a_list[1:]:
            heapq.heappush(heap, -gift)  # x를 최대 힙에 음수로 추가