# 알파벳 대소문자를 입력하여 가장 많이 사용된 알파벳 구하기 문제

import sys
input = sys.stdin.readline

# 알파벳을 입력받고 전체를 소문자로 변환
A = input().strip().upper()

# 알파벳을 하나씩 쪼개서 리스트에 저장
A_list = list(A)

# 알파벳 초기값
a_dic = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
    'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
    'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
    'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
}

# 반복문 / 알파벳이 있을 경우 누적해 줌
for i in A_list:
    if i in a_dic:
        a_dic[i] += 1

# 최대값 초기값
max_count = 0
# 가장 많이 사용된 알파벳 초기값
most_A = ""
# 가장 많이 사용된 알파벳이 여러 개 존재 초기값
tie = False

for A, count in a_dic.items():
    # 최대값보다 많은 수가 나오면 교체해줌
    if count > max_count:
        max_count = count
        most_A = A
        tie = False
    # 최대값이 동률이면 tie를 true해줌
    elif count == max_count and count > 0:
        tie = True


if tie:
    print("?")
else:
    print(most_A)