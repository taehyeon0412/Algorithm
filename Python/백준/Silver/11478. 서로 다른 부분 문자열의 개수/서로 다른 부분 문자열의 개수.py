# 문자열을 입력 받고 문자열의 서로 다른 부분 개수 구하기

import sys
input = sys.stdin.readline

# 입력 받음
S = input().strip()

# 중복 방지 초기값
word = set()

# 문자열 구하기
i = 0
while i < len(S):
    j = i + 1
    while j <= len(S):
        word.add(S[i:j])
        j += 1
    i += 1

print(len(word))