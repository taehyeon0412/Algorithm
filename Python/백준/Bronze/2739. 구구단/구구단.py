# 구구단 문제

n = int(input())

# for 반복문을 사용, range(start,stop) start ~ stop-1까지 생성됨
for i in range(1, 10):
    print(f"{n} * {i} = {n * i}")