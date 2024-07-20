# 입력한 문자 반복하여 새로운 문자열 만들기

# 테스트 케이스 개수 입력 받음
N = int(input())

for i in range(0, N):
    # 반복 횟수 R, 문자열 S를 입력받음
    R, S = input().split()
    # R을 숫자로 변환(split으로 받으면 문자로 받아지기 때문)
    R = int(R)
    # 문자열 P에 문자열을 lambda를 사용하여 담아줌
    # 문자열S의 각요소를 R번 곱해줌
    P = "".join(map(lambda word: word * R, S))

    print(P)