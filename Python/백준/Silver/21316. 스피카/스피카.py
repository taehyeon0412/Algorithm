# 21316번
# 선분들의 정보가 주어질 때, 가장 밝은 별인 Spica가 몇 번 별인지 맞추는 문제
# 반드시 그림과 같은 모습임이 보장된다.

"""풀이 : 7이랑 연결된 숫자를 보면 3,6,8이고 각각의 차수를 구하면 
    3의 차수는 2,4,7 => 3
    6의 차수는 7 => 1
    8의 차수는 7,9 => 2
    3개 차수의 합은 6이므로
    찾은 별 i의 연결된 별 3개의 차수의 합이 6이 되는 것을 찾으면 됨
    
## 차수 : 특정 노드에 연결된 간선의 개수
    """

from collections import defaultdict
import sys
input = sys.stdin.readline

# 선분 입력 받음
edges = [list(map(int, input().strip().split())) for _ in range(12)]

# 차수 계산 라이브러리 초기값
degree = defaultdict(int)

# 각 지점 차수 계산
for x, y in edges:
    degree[x] += 1
    degree[y] += 1

# 스피카 초기값
spica = None

for node in degree:
    if degree[node] == 3:
        degree_sum = 0  # 차수 합 초기값
        for x, y in edges:
            if x == node:
                degree_sum += degree[y]
            elif y == node:
                degree_sum += degree[x]

        # 스피카 조건 확인
        if degree_sum == 6:
            spica = node
            break

print(spica)
