# 최대 소비량을 가진 학교를 찾아내는 문제


import sys
input = sys.stdin.readline

# 테스트 케이스 수 입력 받음
T = int(input().strip())

for _ in range(T):
    # 학교 수 & 학교 정보
    N = int(input().strip())
    schools = [input().strip().split() for _ in range(N)]

    # 최대 소비량 학교
    max_school = max(schools, key=lambda x: int(x[1]))[0]

    print(max_school)

    # https://velog.io/@euisuk-chung/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%8B%9C%EA%B0%81%ED%99%94-%EB%A7%88%EC%8A%A4%ED%84%B0%ED%95%98%EA%B8%B0-%EB%9E%8C%EB%8B%A4Lambda-%ED%95%A8%EC%88%98
