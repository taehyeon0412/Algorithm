# 전쟁의 승자를 출력하는 문제
# 세준이가 이기면 S를 세비가 이기면 B를 둘다 아닐 경우에는 C

import sys
input = sys.stdin.readline


# 병사 힘 입력 중복 코드를 함수로 바꿈
def get_power():
    return sorted(map(int, input().strip().split()))


# 테스트 케이스 입력 받음
T = int(input().strip())


for _ in range(T):
    space = input()
    # 테스트 케이스마다 병사 수 입력 받음
    N, M = map(int, input().split())

    # 병사 힘 입력 받음
    s_power = get_power()
    b_power = get_power()

    # 포인트
    i, j = 0, 0
    while i < N and j < M:
        if s_power[i] < b_power[j]:
            i += 1
        else:
            j += 1

    # 결과
    if i < N:
        print("S")
    else:
        print("B")