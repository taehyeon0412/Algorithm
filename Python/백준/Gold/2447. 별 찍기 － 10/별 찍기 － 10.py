n = int(input().strip())

# 초기 패턴 정의
star = ["***", "* *", "***"]

# n이 3보다 크다면 패턴을 확장
size = 3
while size < n:
    temp = []
    for i in range(3):
        for line in star:
            if i == 1:  # 가운데 부분
                temp.append(line + ' ' * size + line)
            else:  # 위, 아래 부분
                temp.append(line * 3)
    star = temp
    size *= 3

# 최종 패턴 출력
for line in star:
    print(line)