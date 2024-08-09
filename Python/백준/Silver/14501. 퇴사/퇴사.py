# 14501번
# 상담을 했을 때 얻을 수 있는 최대 수익 구하는 문제
# T = 상담 기간, P = 금액
#  N (1 ≤ N ≤ 15)
# 스택을 이용한 백트래킹으로 풀이

# 입력 받음
N = int(input().strip())

advice_list = [tuple(map(int, input().strip().split())) for _ in range(N)]

max_pay = 0

# 현재 날짜 = 1일, 이익 0 초기값
stack = [(1, 0)]

# 스택 빌 때까지 반복
while stack:
    day, current_pay = stack.pop()

    # 최대 이익 갱신
    if current_pay > max_pay:
        max_pay = current_pay

    # N일이 넘으면 다음 스택으로 넘어가게 continue사용
    if day > N:
        continue

    # 상담 안 할 때 다음날 이동
    stack.append((day + 1, current_pay))

    # 상담 할 때
    if day <= N:
        time, pay = advice_list[day - 1]  # 해당 날짜 정보 들고 옴
        if day + time - 1 <= N:  # -1 하는 이유 : 당일 포함해서 계산 이거 때문에 계속 틀림
            stack.append((day + time, current_pay + pay))

print(max_pay)