# 별 찍기 문제

n = int(input())

# 별을 상수로 지정해줌
star = "*"

# for 반복문을 사용, range(start,stop) start ~ stop-1까지 생성됨
for i in range(1, n + 1):
    print(star * i)
