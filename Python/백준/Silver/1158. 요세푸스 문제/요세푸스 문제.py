# 요세푸스 문제
# 원형 리스트에서 매 K번째 사람을 제거 // 큐를 이용해서 풀이

from collections import deque
import sys
input = sys.stdin.readline


# N, K 입력 받기
N, K = map(int, input().strip().split())

# 큐 초기값
queue = deque(range(1, N + 1))

# 결과 초기값
answer = []

# 큐에서 k번째 제거
while queue:
    # K-1명 큐의 뒤로 이동
    queue.rotate(-(K-1))

    # k 제거하고 결과에 추가
    answer.append(queue.popleft())

# 출력
print("<" + ", ".join(map(str, answer)) + ">")