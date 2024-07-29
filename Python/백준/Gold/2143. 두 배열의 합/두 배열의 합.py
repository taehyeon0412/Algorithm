# 배열 A의 모든 부분 배열의 합과 배열 B의 모든 부분 배열의 합을 더해서
# 특정 값 T가 되는 모든 부 배열 쌍의 개수를 구하는 문제
# 해시맵을 이용하여 풀이

""" 
A = {1, 3, 1, 2}
=> {[1],[3],[1],[2],[1,3],[3,1],[1,2],[1,3,1],[3,1,2],[1,3,1,2]}

B = {1, 3, 2}
=> {[1],[3],[2],[1,3],[3,2],[1,3,2]}
"""

from collections import defaultdict
import sys
input = sys.stdin.readline

# 입력 받음
T = int(input().strip())
n = int(input().strip())
A = list(map(int, input().strip().split()))
m = int(input().strip())
B = list(map(int, input().strip().split()))

# A 부분 배열 합을 계산 후 해시맵에 저장
count_A = defaultdict(int)
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += A[j]  # 부분 배열의 합 계산
        count_A[sum] += 1  # 부분 배열 합을 해시맵에 저장하고 카운트 1 증가

# B 부분 배열 합을 계산 후 해시맵에 저장
count_B = defaultdict(int)
for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += B[j]
        count_B[sum] += 1


result = 0  # 결과값 초기화
for sum_B in count_B:  # B의 부분 배열 합 순회
    if T - sum_B in count_A:  # T에서 현재 B의 부분 배열 합을 뺀 값이 A의 해시맵에 존재하는지 확인
        result += count_B[sum_B] * count_A[T - sum_B]  # 존재하면 해당 값을 결과에 더함

print(result)


# defaultdict = 존재하지 않는 키에 접근하면 자동으로 값이 0으로 초기화 됨