# 입력한 문자열에 대한 해시 값을 계산하는 문제

import sys
input = sys.stdin.readline

# 상수 값
r = 31
M = 1234567891

# 문자열의 길이 및 문자열 입력 받기
L = int(input().strip())
string = input().strip()

# 해시 값 초기화
hash_value = 0

# 문자열의 각 문자에 대해 해시 값 계산
for i in range(L):
    char_value = ord(string[i]) - ord('a') + 1
    hash_value += char_value * (r ** i)
    hash_value %= M  # 매번 모듈러 연산을 통해 값이 너무 커지지 않도록 함

# 최종 해시 값 출력
print(hash_value)