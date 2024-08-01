import sys

# 입력 받기
input = sys.stdin.readline
T = int(input().strip())  # 테스트 케이스 수

for _ in range(T):
    N, M = map(int, input().strip().split())
    # M개의 간선 정보는 입력받지만 사용하지 않음 (항상 연결 그래프)
    for _ in range(M):
        a, b = map(int, input().strip().split())
    # 최소 스패닝 트리의 간선 수는 항상 N-1
    print(N - 1)