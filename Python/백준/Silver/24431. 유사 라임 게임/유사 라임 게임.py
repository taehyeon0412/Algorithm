# 24431번
#  주어진 단어 리스트에서 문자 패턴에 따라 라임이나 매칭되는 단어의 수를 계산하는 문제
# 영문 대문자로만 구성된 길이가 L인 서로 다른 단어 n개
# 최대 공통 접미사 F이상이면 "유사 라임"이라고 정의한다.
# 한 단어는 최대 하나의 유사 라임 쌍에만 속할 수 있다.(중복 안된다는 말)

"""
4 4 2
WALK TALK MILK BULK => (WALK, TALK), (MILK,BULK) 2개
4 4 3
WALK TALK MILK BULK => (WALK, TALK) 1개
"""
import itertools
import sys
input = sys.stdin.readline

# 테스트 케이스 입력 받음
T = int(input().strip())


for _ in range(T):

    # n = 단어 개수 , L = 단어 길이, F = 최대 공통 접미사
    n, L, F = map(int, input().strip().split())

    # 단어 리스트 입력 받기
    words = input().strip().split()

    # 유사 라임 사용된 단어 여부
    # ex)n = 3 / [False,False,False]
    used = [False] * n
    rhyme = 0

    # 모든 가능한 단어 쌍(2)을 검사
    for i, j in itertools.combinations(range(n), 2):
        # 둘 다 사용하지 않은 단어이고 마지막 F만큼 같으면 유사라임 +1
        if not used[i] and not used[j] and words[i][-F:] == words[j][-F:]:
            rhyme += 1
            # 쌍이 되면 True로 변경해서 사용된 걸로 표시
            used[i] = used[j] = True

    print(rhyme)