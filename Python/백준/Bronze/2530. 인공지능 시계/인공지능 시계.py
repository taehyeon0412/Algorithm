A, B, C = map(int, input().split())
# input.split = 사용자가 입력한 문자열을 공백을 기준으로 분리
# map을 사용하여 분리된 리스트를 int로 바꿔줌
D = (int(input()))
# 정수로 받음

total = A * 3600 + B * 60 + C + D
# 전체 시간을 초로 바꾸고 오븐구이 시간을 더해줌

if D <= 500000:
    total %= 86400
    # 하루는 86400초
    # //는 정수부분만 가져옴
    hour = total // 3600
    minutes = (total % 3600) // 60
    seconds = total % 60

    print(hour, minutes, seconds)

else:
    print("500,000 이하로 숫자를 넣어주세요")