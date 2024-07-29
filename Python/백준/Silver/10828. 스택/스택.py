# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령 처리 문제
"""
스택 = LIFO
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
input = sys.stdin.readline

#  N 입력 받음
N = int(input().strip())

# 스택 초기값
stack = []

# 명령 처리
for _ in range(N):
    action = input().strip().split()

    if action[0] == "push":
        stack.append(int(action[1]))

    elif action[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif action[0] == "size":
        print(len(stack))

    elif action[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif action[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
