# 알고리즘 수행 시간을 출력하는 문제

""" 
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

첫번째 for문 // i가 1부터~n-1까지 반복  = 총 n-1번 반복
두번째 for문 // j가 i+1부터 n까지 반복 = 총 n-i번 반복

중첩 for문 O(n²)로 표기
= 등차수열의 합을 구하는 것, 차수는 2
"""

import sys
input = sys.stdin.readline

n = int(input())


print((n * (n - 1)) // 2)
print(2)