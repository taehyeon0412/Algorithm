import sys
input = sys.stdin.readline

# 입력 받음
N, K = map(int, input().split())
coin_list = []

for _ in range(N):
    coin_list.append(int(input().strip()))

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