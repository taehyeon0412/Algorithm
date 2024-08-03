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