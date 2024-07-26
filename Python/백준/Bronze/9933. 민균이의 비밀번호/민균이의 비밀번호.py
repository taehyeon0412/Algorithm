# 단어를 입력했을 때 비밀번호의 길이와 가운데 글자 출력 문제
# 단어를 뒤집었을 때 똑같은 단어가 있으면 비밀번호이다.

import sys
input = sys.stdin.readline

# 숫자 입력 받음
N = int(input().strip())

# N만큼 단어 입력 받음
words_list = [input().strip() for _ in range(N)]

# for 반복문 이용 비밀번호 찾기
for pw in words_list:
    # 리스트에 있는 문자열 뒤집어서 비교
    if pw[::-1] in words_list:
        # 비밀번호 길이
        pw_len = len(pw)
        # 가운데 문자 인덱스
        pw_mid = pw[pw_len // 2]

print(pw_len, pw_mid)