# 입력받은 문자열의 개수를 구한는 문제

import sys
input = sys.stdin.readline

# strip을 사용하여 양쪽 공백을 없앰
S = input().strip()

blank = S.count(" ")

# 단어는 공백의 개수보다 1개가 더 많다
# 빈문자열일 경우에는 0으로 나오도록 조건문 추가
if S:
    word_count = blank + 1
else:
    word_count = 0

print(word_count)