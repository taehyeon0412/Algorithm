# 3의배수인지 구하는 문제 (재귀)

# X 입력 받음
X = input().strip()

# 카운트 초기값
count = 0

# X를 정수로 만들고 배열로 저장함
X_list = [int(num) for num in X]

# 배열 합 초기값
X_sum = sum(X_list)


# 첫 변환
if X_sum >= 10:
    count += 1


# 한자리 수가 되어야 되니까 10이상이면 반복
while X_sum >= 10:
    # X_sum을 다시 문자로 만들어 분해 후 리스트로 만들고 정수로 바꿈
    X_list = [int(num) for num in str(X_sum)]
    X_sum = sum(X_list)
    count += 1


# 출력
print(count)

if X_sum % 3 == 0:
    print("YES")
else:
    print("NO")