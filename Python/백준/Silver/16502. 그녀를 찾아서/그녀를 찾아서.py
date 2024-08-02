# 16502번
# 특정 시간 이후에 각 노드(매장)에서 그녀가 있을 확률을 계산하는 문제

import sys
input = sys.stdin.readline

# 쇼핑 시간 (단위: 10분) 입력 받기
time = int(input().strip())

# 간선의 개수 입력 받기
M = int(input().strip())

# 초기 확률 설정: A, B, C, D에 동일 확률로 분포
probability = {
    'A': 0.25,
    'B': 0.25,
    'C': 0.25,
    'D': 0.25
}

# 이동 확률 그래프 초기화
transitions = {'A': {}, 'B': {}, 'C': {}, 'D': {}}

# 간선 정보 입력 받기
for _ in range(M):
    start, end, prob = input().strip().split()
    prob = float(prob)
    transitions[start][end] = prob

# 쇼핑 시간 동안 확률 갱신
for _ in range(time):
    next_probs = {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0}

    # 현재 매장에서 다른 매장으로의 이동 확률 계산
    for current_shop in probability:
        current_prob = probability[current_shop]
        for next_shop, transition_prob in transitions[current_shop].items():
            next_probs[next_shop] += current_prob * transition_prob

    # 다음 상태의 확률을 현재 상태로 갱신
    probability = next_probs

# 결과 출력
for shop in ['A', 'B', 'C', 'D']:
    print(f"{probability[shop] * 100:.2f}")