# 상근이가 가지고 있는 숫자 카드 N개에 M개의 같은 카드가 있는지 여부를 확인하는 문제

import sys
input = sys.stdin.readline

# 상근이가 가지고 있는 숫자 카드 N개 입력 받음
N = int(input())

# 문제 입력에 (같은 수가 적혀있는 경우는 없다.)라는 조건이 있어서 set을 사용
# set() = 중복을 허용하지 않는다.
N_set = set(map(int, input().split()))

# 찾아야 되는 카드의 개수
M = int(input())

# 찾아야 되는 카드 목록
# set을 쓰지 않는 이유 = 상근이가 그 수를 가지고 있는지를 확인한 결과를 순서대로 출력해야 하기 때문
# 집합(set)은 순서를 보장하지 않음
M_list = list(map(int, input().split()))

# 결과를 배열로 저장
answer = []

# 숫자 카드가 상근이의 카드에 있으면 1 없으면 0 추가
for i in M_list:
    if i in N_set:
        answer.append(1)
    else:
        answer.append(0)

# 공백으로 구분하여 한줄로 출력
print(" ".join(map(str, answer)))

# https://velog.io/@insutance/Python-set-%EC%9D%B4%EB%9E%80