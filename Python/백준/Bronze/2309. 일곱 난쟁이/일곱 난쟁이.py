# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 문제
# sorted 정렬 알고리즘 사용 풀이

import itertools
import sys
input = sys.stdin.readline

# 9명 난쟁이 입력 받음
dwarfs = [int(input().strip()) for _ in range(9)]

# 7명 난쟁이 키 조합
for combi in itertools.combinations(dwarfs, 7):
    if sum(combi) == 100:
        result = sorted(combi)
        break

for dwarf in result:
    print(dwarf)