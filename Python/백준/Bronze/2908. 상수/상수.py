# 두 수를 입력받고 거꾸로 뒤집어 큰수를 비교하는 문제

import sys
input = sys.stdin.readline

# 두 수를 입력받음
A, B = input().split()

# 숫자를 뒤집음
reverse_A = int(A[::-1])

reverse_B = int(B[::-1])

if reverse_A > reverse_B:
    print(reverse_A)
else:
    print(reverse_B)