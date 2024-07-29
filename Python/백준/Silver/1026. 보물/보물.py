# 두 배열 A와 B에 대해 S의 값을 최소화하는 문제
# S = A요소 * B요소 // A배열 재배열

import sys
input = sys.stdin.readline

# 입력 받음
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A를 오름차순 정렬, B를 내림차순 정렬
A.sort()
B.sort(reverse=True)

# S의 최솟값 계산
S = 0
for i in range(N):
    S += A[i] * B[i]

print(S)
