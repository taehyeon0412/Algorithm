# 입력된 단어들을 반대 순서로 뒤집어 출력하는 문제

import sys
input = sys.stdin.readline

# N 입력 받음
N = int(input().strip())

# 반복문을 이용 반대로 뒤집기
# 출력이 case1번부터 시작하니 range는 1부터 N + 1까지
for i in range(1, N + 1):
    # 문장 한줄 입력받고 공백을 기준으로 리스트화
    word_list = input().strip().split()
    # 리스트 반대로 뒤집기
    word_list_reverse = word_list[::-1]
    # 출력
    print(f"Case #{i}: {' '.join(word_list_reverse)}")