# 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주는 문제
# 다른 국가 이동할 때 다른 국가 거쳐 가도 됨(이미 방문한 국가도)

import sys
input = sys.stdin.readline

# 입력 받기
T = int(input().strip())  # 테스트 케이스 수

for _ in range(T):
    # 국가 수, 비행기 경로 수
    N, M = map(int, input().strip().split())
    # M개의 간선 정보는 입력받지만 사용하지 않음 (항상 연결 그래프)
    for _ in range(M):
        input().strip()
    # 최소 스패닝 트리의 간선 수는 항상 N-1
    print(N - 1)


""" 
노드 수가 
N개인 그래프의 최소 스패닝 트리는 항상 
N−1개의 간선으로 구성됩니다.
"""