# 다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램

import sys
input = sys.stdin.readline

# 후보자 수 입력
N = int(input().strip())

# 득표수 리스트
vote = [int(input().strip()) for _ in range(N)]

# 매수해야 되는 초기값
count = 0

# 각 참가자 득표수
dasom = vote[0]

while True:
    if N == 1:
        break

    # 다솜 제외 최대 득표수
    max_vote = max(vote[1:])

    if dasom > max_vote:
        break

    # max_vote를 가진 인덱스를 1부터 찾음
    max_index = vote.index(max_vote, 1)
    vote[max_index] -= 1
    dasom += 1
    count += 1

print(count)
