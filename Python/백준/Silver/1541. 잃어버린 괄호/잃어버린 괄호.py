# 1541번
# 양수와 +, -, 그리고 괄호를 가지는 식을 괄호를 쳐서 최소로 만드는 문제
# -뒤에 있는 수가 클수록 값이 작아짐
# -뒤에 있는 숫자부터 ()를 해서 크게 만들어서 풀이

import sys
input = sys.stdin.readline

# 식 입력 받음
math = input()

# -기준으로 분리
math_div = math.split("-")

# 첫번째 부분
# +를 기준으로 나누고 더해줌
first = sum(map(int, math_div[0].split('+')))

# 두번째 부분
second = 0

# 리스트의 나머지 부분들 더해줌
for a in math_div[1:]:
    second += sum(map(int, a.split("+")))

answer = first - second

print(answer)
