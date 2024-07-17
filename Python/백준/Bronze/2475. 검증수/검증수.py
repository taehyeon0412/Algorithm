a = map(int, input().split())
# input.split = 사용자가 입력한 문자열을 공백을 기준으로 분리
# map을 사용하여 분리된 리스트를 int로 바꿔줌
result = 0

for i in a:
    result += i*i
# for문 반복을 통해 입력받은 숫자의 제곱을 더해서 result에 넣음

result %= 10
# result에 10을 나눈 나머지값을 넣음

print(result)