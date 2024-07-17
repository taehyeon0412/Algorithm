A, B, C = map(int, input().split())
# input.split = 사용자가 입력한 문자열을 공백을 기준으로 분리
# map을 사용하여 분리된 리스트를 int로 바꿔줌

if A >= 2 and C <= 10000:
    print((A+B) % C)
    print(((A % C) + (B % C)) % C)
    print((A*B) % C)
    print(((A % C) * (B % C)) % C)
else:
    print("첫번째 숫자 >= 2 and 세번째 숫자 <= 10000 조건을 만족해 주세요.")