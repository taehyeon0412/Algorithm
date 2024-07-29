# 1차 티켓팅에서 팔린 번호 제외, 가장 작은 티켓 번호 찾는 문제
# 1번부터 시작함

# 팔린 티켓
N = int(input().strip())

# 팔린 티켓 리스트 list보다 set이 빠름
sold = set(map(int, input().strip().split()))

small_number = 1

# 1부터 시작이니까 1부터 1씩 증가 시켜서 sold에 있는지 찾음 없으면 그게 답
while small_number in sold:
    small_number += 1

print(small_number)