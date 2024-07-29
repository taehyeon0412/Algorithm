# 알파벳 N개를 받으면 정렬하기 문제
# 길이가 짧은순, 길이가 같으면 사전 순 / 중복된 단어 제거

import sys
input = sys.stdin.readline

# 알파벳 개수 입력 받음
N = int(input().strip())

# 알파벳 입력 받음 /set으로 중복 제거
words = {input().strip() for _ in range(N)}

# 정렬 / len(x) = 길이순, x = 사전순
sort_words = sorted(words, key=lambda x: (len(x), x))

for word in sort_words:
    print(word)