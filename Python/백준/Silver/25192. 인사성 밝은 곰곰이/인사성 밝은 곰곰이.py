# 채팅방의 기록을 수집해 그 중 곰곰티콘이 사용된 횟수를 구하는 문제

import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())

# 곰티콘 초기값
gom_i = 0

# 채팅 기록 set을 써서 중복 방지
# list를 써도 되는데 list를 쓰면 시간초과가 된다. 시간복잡도를 확인하자
chat_log = set()


for i in range(N):
    log = input().strip()

    # 새로운 사람 입장 = "ENTER" 하면 초기화
    if log == "ENTER":
        chat_log.clear()
    else:
        # 유저 새로운 채팅
        if log not in chat_log:
            chat_log.add(log)
            gom_i += 1

# 출력
print(gom_i)
