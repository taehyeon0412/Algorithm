# 1388번
# 방 바닥을 장식하는 나무 판자의 개수를 세는 문제

""" 
6 9
-||--||--         가로 : 15개
--||--||-         세로 : 16개
|--||--||           합 : 31개
||--||--|
-||--||--
--||--||-
"""

import sys
input = sys.stdin.readline


# Row = 행(가로) / Column 열(세로)
# 행,열 입력 받음
R, C = map(int, input().split())

# 바닥 입력 받음
floor = [list(input().strip()) for _ in range(R)]

count = 0

# 판자가 이어지는지 여부만 판단하면 됨
# 판자가 발견되고 그다음 인덱스에 -가 없으면 count+1 해주는 방식

# 가로
i = 0
while i < R:
    j = 0
    while j < C:
        # - 발견
        if floor[i][j] == "-":
            count += 1
            # 마지막줄이 아니고 -이 없을 때 까지 j 증가
            while j < C and floor[i][j] == "-":
                j += 1
        else:
            j += 1
    i += 1

# 세로
j = 0

while j < C:
    i = 0
    while i < R:
        # | 발견
        if floor[i][j] == "|":
            count += 1
            # 마지막줄이 아니고 |이 없을 때 까지 i 증가
            while i < R and floor[i][j] == "|":
                i += 1

        else:
            i += 1
    j += 1

print(count)