# 상근이가 가지고 있는 숫자 카드 N개에 M개의 같은 카드가 있는지 여부를 확인하는 문제

import sys
from collections import Counter
input = sys.stdin.readline

# 상근이가 가지고 있는 숫자 카드 N개 입력 받음
N = int(input())

# 상근이가 가지고 있는 숫자 카드 목록
N_list = list(map(int, input().split()))

# 찾아야 되는 카드의 개수
M = int(input())

# 찾아야 되는 카드 목록
M_list = list(map(int, input().split()))

# 숫자 카드의 개수를 카운팅하는 Counter 생성(라이브러리)
M_count = Counter(N_list)

# 결과값 배열로 초기화
answer = []

# 숫자 카드 확인
for i in M_list:
    answer.append(M_count[i])

# 결과 출력
print(" ".join(map(str, answer)))

""" 
counter("hello world") 
=> Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
"""


# https://velog.io/@eunhye_/python-collections-Counter