# 𝑓(𝑛)=𝑎1×𝑛+𝑎0f(n)=a1×n+a0가 빅-오 표기법 𝑂(𝑛)O(n)의 정의를 만족하는지 확인하는 문제

# 입력 받기
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())


def is_big_o_of_n(a1, a0, c, n0):
    # n0부터 100까지 검사 (문제의 조건에 따라 100까지만 검사하면 충분)
    for n in range(n0, 101):
        # 조건을 만족하지 않으면 0반환 만족하면 1반환
        if a1 * n + a0 > c * n:
            return 0
    return 1


print(is_big_o_of_n(a1, a0, c, n0))