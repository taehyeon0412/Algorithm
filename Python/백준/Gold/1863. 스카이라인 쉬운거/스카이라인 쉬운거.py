import sys
input = sys.stdin.readline

# n입력 받음
n = int(input().strip())

# 고도 변화와 x좌표 입력 받음
points = [tuple(map(int, input().split())) for _ in range(n)]

# 스택과 건물 수 초기화
stack = []
building_count = 0

for x, y in points:
    # 현재 스택의 최상단 높이보다 낮은 높이로 변하는 경우
    while stack and stack[-1][1] > y:
        stack.pop()
    # 현재 스택이 비어있거나, 현재 높이가 스택의 최상단 높이보다 높을 경우
    if not stack or stack[-1][1] < y:
        if y != 0:
            stack.append((x, y))
            building_count += 1

print(building_count)