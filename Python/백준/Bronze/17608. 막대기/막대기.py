# N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램 문제
# 마지막에 입력된 막대기부터 역순으로 바라보는 것으로 풀이

import sys
input = sys.stdin.readline

# N 입력받음
N = int(input().strip())

# 리스트 입력받음
height_list = [int(input().strip()) for _ in range(N)]

# 리스트 역순 배치
height_list.reverse()

# 초기값 설정
# 제일 앞에 있는건 무조건 보임
count = 1

# 인덱스 0번
max_height = height_list[0]

# 각 숫자를 반복문으로 비교
for i in range(1, N):
    # 인덱스 1번부터 비교
    height = height_list[i]
    if height > max_height:
        count += 1
        max_height = height

print(count)