import heapq
import sys

input = sys.stdin.read
data = input().split()

index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    K = int(data[index])
    index += 1
    file_sizes = list(map(int, data[index:index + K]))
    index += K
    
    # 파일 크기 리스트를 최소 힙으로 변환
    heapq.heapify(file_sizes)
    
    # total_cost : 모든 장을 합치는데 필요한 비용
    total_cost = 0
    
    # 힙에서 두 개의 파일을 꺼내서 합치는 과정을 반복
    while len(file_sizes) > 1:
        first = heapq.heappop(file_sizes)
        second = heapq.heappop(file_sizes)
        cost = first + second
        total_cost += cost
        heapq.heappush(file_sizes, cost)
    
    results.append(total_cost)

print("\n".join(map(str, results)))