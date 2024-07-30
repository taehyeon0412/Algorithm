# 학생들이 학교 식당에 도착하고 식사를 준비하는 정보를 순서대로 처리
# 줄을 서서 대기하는 학생 수가 최대가 되었던 순간의 학생 수와 그때 줄의 맨 뒤에 대기한 학생의 번호를 구하기
# 1 a: 정수 a가 인 / 2: 제일 앞에 있는 학생 1명 아웃
# FIFO / deque 사용 풀이

"""
5
1 2        2번 줄 = [2]
1 1        1번 줄 = [2,1]
2          2번 아웃 = [1]
1 3        3번 줄 = [1,3]
2          1번 아웃 = [3]

최대 수 2
마지막 학생 번호중 가장 작은 수 1
그래서 print 2 1
"""

from collections import deque
import sys
input = sys.stdin.readline

# n을 입력 받음
n = int(input().strip())

# 줄을 입력 받음
waiting = [input().split() for _ in range(n)]

# 최대 길이, 마지막 학생 초기값
queue = deque()
max_len = 0
last_student = None


# 줄서기 처리
for action in waiting:
    # 줄 서는 액션 / 학생 번호 가져와서 큐에 추가 / 길이 확인
    if action[0] == "1":
        student_num = int(action[1])
        queue.append(student_num)
        queue_len = len(queue)

        # 최대 길이 보다 길면 바꾸고 마지막 학생 갱신
        if queue_len > max_len:
            max_len = queue_len
            last_student = student_num

        # 최대 길이하고 같을 때 둘 중 작은 학생 넣기
        elif queue_len == max_len:
            last_student = min(last_student, student_num)

    # 나가는 액션
    else:
        queue.popleft()

print(max_len, last_student)