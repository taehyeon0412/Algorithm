# 3098번
# 소셜 네트워크에서 모든 사람이 서로 친구가 되기까지의 일수를 계산하는 문제
# 입력 첫줄은 사람의 수 N, 처음 친구 관계 수 M
# 둘째 줄부터 정수 A,B(A,B는 친구)

""" 
3 2
1 2
2 3

3 2: 사람의 수 / 처음 친구 관계 수
1 2: 사람 1과 사람 2가 친구.
2 3: 사람 2와 사람 3이 친구.

첫 번째 날
사람 1: 현재 친구: {2} + 새로운 친구 추가: {3} = {2,3}
사람 2: 새로운 친구 없음 = {1,3}
사람 3: 현재친구: {2} + 새로운 친구 추가: {1} = {1,2}

총 일수 1일
첫째 날에 새로 형성된 친구 수 : 1 (1<->3)
"""

import sys
input = sys.stdin.readline

# 사람의 수 N, 처음 친구 관계 수 M 입력 받음
N, M = map(int, input().split())

# 각 사람의 친구를 집합으로 관리 (중복 친구 제거)
friends = [set() for _ in range(N + 1)]

# 초기 친구 관계 설정
for _ in range(M):
    A, B = map(int, input().split())
    friends[A].add(B)  # A의 친구 목록에 B를 추가
    friends[B].add(A)  # B의 친구 목록에 A를 추가

# 친구 관계 확장 초기값
days = 0
connection_list = []  # 매일 새롭게 형성된 친구 관계의 수를 저장

while True:  # 모든 사람이 서로 친구가 될 때까지 반복
    new_connections = 0  # 하루 동안 형성된 새로운 친구 관계의 수
    updated_friends = [set(friends[i]) for i in range(N + 1)]

    # 하루 동안의 친구 확장
    for person in range(1, N + 1):
        # 새로운 친구 목록을 저장할 집합
        new_friends = set()

        # 친구의 친구 추가
        for friend in friends[person]:
            # 친구의 친구들을 모두 새로운 친구 목록에 추가
            new_friends.update(friends[friend])

        # 이미 친구이거나 자신인 경우 제외
        new_friends -= friends[person]  # 이미 친구인 사람 제외
        new_friends.discard(person)  # 자신을 제외

        # 오늘 새로 추가된 친구 관계의 수
        new_connections += len(new_friends)

        # 기존 친구 목록에 새 친구들 추가
        updated_friends[person].update(new_friends)

    # 새로운 친구 관계가 없다면 중단
    if new_connections == 0:
        break  # 모든 사람들이 이미 친구가 되었으므로 종료

    # 대칭 관계로 인해 2로 나누어 추가된 관계 수 저장
    # 모든 새로운 관계가 두 방향에서 추가되므로 실제 새로 형성된 관계 수는 절반
    connection_list.append(new_connections // 2)
    friends = updated_friends  # 업데이트된 친구 목록 적용
    days += 1  # 하루 경과

# 결과 출력
print(days)  # 모든 사람이 친구가 되기까지 걸린 일수 출력
for connections in connection_list:
    print(connections)  # 각 날 새롭게 형성된 친구 관계의 수 출력
