# 별 찍기 문제

n = int(input())

# 별과 공백을 상수로 지정해줌
star = "*"
blank = " "

# for 반복문을 사용, range(start,stop, step)
# start ~ stop-1까지 반복되고 step만큼 움직임
for i in range(1, n + 1):
    # 공백 = (input값(n) - 회차값(i)) x 양쪽(2)
    print(star * i + blank * (2 * (n - i)) + star * i)


for i in range(n-1, 0, -1):
    print(star * i + blank * (2 * (n - i)) + star * i)