# 의상을 조합해서 겹치지 않게 입어야 되는 문제
# 종류별로 의상의 개수를 찾고 조합 계산하여 풀이

from collections import Counter
import math
import sys
input = sys.stdin.readline

# 테스트 케이스 수 입력 받음
test = int(input().strip())

# 결과 초기값
results = []

# 각 테스트 케이스
for _ in range(test):
    # 의상 수
    n = int(input().strip())
    # 의상 수 0일 때 0을 추가하고 다음 테스트 케이스로 넘어감
    if n == 0:
        results.append(0)
        continue

    # 의상 종류 리스트
    clothes = []

    # 의상 정보 리스트 저장
    for _ in range(n):
        name, clothes_type = input().strip().split()
        clothes.append(clothes_type)

    # 종류별로 의상 개수 찾기
    clothes_count = Counter(clothes)

    # 종류별로 의상 개수 + 1 해서 리스트로 만듦
    counts = [count + 1 for count in clothes_count.values()]

    # 조합 계산 후 result에 추가
    results.append(math.prod(counts) - 1)

# 결과 출력
for result in results:
    print(result)


# prod = 모든 요소를 곱한 값을 반환

""" 
의상 종류별로 분류:
headgear: hat, turban (2가지)
eyewear: sunglasses (1가지)

각 종류별 경우의 수 계산:
headgear를 입는 경우: hat, turban
headgear를 입지 않는 경우: 아무 것도 입지 않음
따라서, headgear의 경우의 수 = 3가지 (hat, turban, 입지 않음)

eyewear를 입는 경우: sunglasses
eyewear를 입지 않는 경우: 아무 것도 입지 않음
따라서, eyewear의 경우의 수 = 2가지 (sunglasses, 입지 않음)

모든 경우의 수  = 3 * 2 = 6
2개 전부 아무것도 입지 않는 경우 제외 = 5가지 
"""