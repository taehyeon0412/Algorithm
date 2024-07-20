# 한종류 이상의 과일이 5개 있는경우 yes 출력 문제

import sys
input = sys.stdin.read

# 입력 데이터 한번에 읽음(줄단위로 분리)
data = input().strip().split("\n")

# 카드의 개수 N 입력받음(data의 첫번째)
N = int(data[0])

# 과일 초기값 설정
fruit_dict = {
    "STRAWBERRY": 0,
    "BANANA": 0,
    "LIME": 0,
    "PLUM": 0
}

for i in range(1, N + 1):
    # 과일 이름, 과일 개수를 입력받음
    fruit, fruit_n = data[i].split()
    # 정수로 바꿔줌
    fruit_n = int(fruit_n)
    # 해당 과일의 개수를 누적해 줌
    fruit_dict[fruit] += fruit_n

# 판단
answer = any(count == 5
             for count in fruit_dict.values())

# 결과를 출력합니다.
if answer:
    print("YES")
else:
    print("NO")

# any함수 :  요소 중 하나라도 True이면 True를 반환하고, 그렇지 않으면 False를 반환
# any함수 안에 for문을 넣어 5인 값을 찾음