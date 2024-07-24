# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

import sys
input = sys.stdin.readline

# N과 M을 입력받음
N, M = map(int, input().split())


def create_sequences(N, M):
    # backtrack함수는 현재까지 만들어진 수열을 나타내는 리스트 sequence를 인자로 받음
    def backtrack(start, sequence):
        # 현재 수열의 길이가 M과 같으면 수열 출력
        # backtrack의 매개변수인 sequence로
        if len(sequence) == M:
            print(' '.join(map(str, sequence)))
            return

        # 반복문 1부터 N까지의 숫자
        for i in range(start, N + 1):
            # 현재 수열에 i가 포함x일 때
            if i not in sequence:
                # i를 수열에 추가
                sequence.append(i)
                # backtrack 함수를 호출하여 다음 숫자를 추가
                backtrack(i + 1, sequence)
                # 마지막에 추가한 숫자를 제거 후 다음 숫자를 추가
                sequence.pop()

    # 빈 리스트로 시작하는 backtrack 함수를 호출하고 만들어진 수열이 추가됨
    backtrack(1, [])


# 함수를 호출하여 수열을 생성
create_sequences(N, M)