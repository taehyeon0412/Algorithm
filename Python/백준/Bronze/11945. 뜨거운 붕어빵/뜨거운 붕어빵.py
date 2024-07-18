# 입력 배열 반대로 뒤집기 문제

rows, columns = map(int, input().split())

# for 반복문을 이용하여 rows번 반복
# input().strip() 문자열의 양 끝에 있는 공백 문자(스페이스, 탭, 줄 바꿈 문자 등)를 제거
pattern = [input().strip() for _ in range(rows)]

# 좌우로 뒤집기 및 출력
# a = 'hello' => a[::-1] olleh로 슬라이싱
for line in pattern:
    print(line[::-1])