# 15723번
# n단 논법 문제
# stack을 이용한 DFS로 풀이
""" 특별한 명시는 없지만 모든 전제는 “모든 a는 b이다”라는 의미이다.
하지만 “모든 b는 a이다”의 의미는 될 수 없다.
또한 a는 b이면서 c일 수 없으나, a와 b가 동시에 c일 수는 있다. """

""" 
3           # n = 3 (전제)
a is b      # 전제 1
b is c      # 전제 2
c is d      # 전제 3
3           # m = 3 (결론) N +2
a is d      # 결론 1
a is c      # 결론 2
d is a      # 결론 3
"""

""" 
defaultdict(int) => 0으로 초기화
defaultdict(list) => []으로 초기화
"""

from collections import defaultdict
import sys
input = sys.stdin.readline

# 리스트 초기화
list_ = defaultdict(list)

# n(조건) 입력 받음
n = int(input().strip())

# 조건 입력 받음
for _ in range(n):
    # a is b에서 is를 _(공백)으로 처리
    a, _, b = input().strip().split()
    # a키에 b를 넣음 = "a" : ["b"]
    list_[a].append(b)

# m(결과) 입력 받음
m = int(input().strip())

# 조건 입력 받고 검사함
for _ in range(m):
    a, _, b = input().strip().split()
    stack = [a]  # 스택 초기값
    visited = set()  # 방문한 노드 집합(중복 제거)

    # 스택 이용 DFS 탐색
    while stack:
        node = stack.pop()  # 시작값 받음
        if node == b:  # 목표 도달 확인
            print("T")
            break

        # 노드가 set에 없을 경우(방문하지 않은 경우)
        if node not in visited:
            visited.add(node)  # 방문 추가
            # 옆 노드 탐색
            for next_ in list_[node]:
                if next_ not in visited:
                    stack.append(next_)

    # while 루프가 break 없이 끝나면 else로 나오게 함
    else:
        print("F")
