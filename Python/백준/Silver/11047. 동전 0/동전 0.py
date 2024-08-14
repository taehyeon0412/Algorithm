# 11047번
# 동전 값의 합을 K로 만들 때 동전 개수의 최솟값 문제
# 그리디 알고리즘 문제

import sys
input = sys.stdin.readline

# 입력 받음
N, K = map(int, input().split())

coin_list = [int(input()) for _ in range(N)]

# 값이 큰 순으로 정렬
coin_list.sort(reverse=True)

count = 0

# K가 0이 될 때까지 반복
for coin in coin_list:
    if K == 0:
        break
    if K >= coin:
        count += K // coin  # 동전의 개수를 한 번에 계산
        K %= coin  # K를 coin으로 나눈 나머지로 갱신

print(count)
