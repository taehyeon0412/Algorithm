# 2529번
# k개의 부등호 기호를 입력 받고 거기에 맞는 수를 넣어서 만족하는 최댓값, 최솟값 찾기
# 0~9까지 선택 가능함

""" 
백트래킹 vs DFS 

백트래킹이란 현재 상태에서 가능한 모든 경로를 따라 들어가 탐색하다, 
원하는 값과 불일치하는 부분이 발생하면 더 이상 탐색을 진행하지 않고 전 단계로 이동

DFS는 모든 경우의 수를 탐색

https://veggie-garden.tistory.com/24
"""

import sys
input = sys.stdin.readline

# 부등호 수, 방향 입력 받음
k = int(input().strip())
direction = input().split()

max_num = None
min_num = None

# i = 현재 부등호 인덱스, num_list = 현재까지 선택된 숫자 리스트
stack = [(0, [])]

# 스택을 이용한 백트래킹
while stack:
    i, num_list = stack.pop()

    # k+1개의 숫자를 모두 사용한 경우, 결과 업데이트
    if i == k + 1:
        num = ''.join(map(str, num_list))
        if max_num is None or num > max_num:
            max_num = num
        if min_num is None or num < min_num:
            min_num = num
        continue  # continue 써서 다음 스택으로 넘어감

    # 사용 가능한 숫자: num_list에 없는 숫자
    used_numbers = set(range(10)) - set(num_list)

    # 오름차순 탐색
    for num in sorted(used_numbers):
        if i == 0 or (direction[i - 1] == '<' and num_list[-1] < num) or (direction[i - 1] == '>' and num_list[-1] > num):
            stack.append((i + 1, num_list + [num]))

print(max_num)
print(min_num)
