A, B = map(int, input().split())
# input.split = 사용자가 입력한 문자열을 공백을 기준으로 분리
# map을 사용하여 분리된 리스트를 int로 바꿔줌

if A > 0 and B < 10:
    print(A-B)
else:
    print("A는 0보다 커야되고 B는 10보다 작아야 됩니다.")