# 알고리즘 수행 시간을 출력하는 문제

""" 
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

첫번째 for문 // 1부터 n-2까지 반복 = 총 n-2번 반복
두번째 for문 // i+1부터 n-1 까지 반복 = 총 n-i-1번 반복
세번째 for문 // j+1부터 n까지 반복 = 총 n-j번 반복 

3중첩 for문 O(n³)로 표기
=차수는 3
"""

import sys
input = sys.stdin.readline

n = int(input())

# 수행 횟수가 정수로 나와야 하므로 //를 사용
print((n * (n - 1) * (n - 2)) // 6)
print(3)