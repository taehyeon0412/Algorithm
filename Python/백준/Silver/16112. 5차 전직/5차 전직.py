# 경험치의 합을 최대화하는 문제

import sys
input = sys.stdin.readline

# 경험치 수 / 활성화 수 입력 받음
n, k = map(int, input().split())

# 경험치 입력 받음
exp_list = sorted(map(int, input().split()))

total = 0
stone = 0

for i in range(n):
    total += exp_list[i] * stone

    if stone < k:
        stone += 1

print(total)