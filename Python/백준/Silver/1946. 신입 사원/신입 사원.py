# 1946번
# 테스트케이스 비교해서 종목 하나라도 나으면 채용 / 둘다 낫으면 탈락

import sys
input = sys.stdin.readline

# 테스트 케이스 입력 받음
T = int(input().strip())

for _ in range(T):
    # 지원자수 입력 받음
    N = int(input().strip())
    # 시험 성적 입력 받음
    number = sorted([tuple(map(int, input().split())) for _ in range(N)])

    # 최소 인원 초기값 1명은 선발됨
    count = 1

    # 첫 번째 지원자의 면접 순위 초기값
    best = number[0][1]

    for i in range(1, N):
        # 현재 지원자가 best보다 성적이 좋은 경우
        if number[i][1] < best:
            count += 1  # count증가
            best = number[i][1]  # 최고 성적 갱신

    print(count)