# 자연수 N과 M이 주어졌을 때,조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성 문제

# backtracking 함수 사용

import sys
input = sys.stdin.readline

# N과 M을 입력받음
N, M = map(int, input().split())


def create_sequences(N, M):
    def backtrack(sequence):
        # 현재 수열의 길이가 M과 같으면 수열 출력
        if len(sequence) == M:
            print(' '.join(map(str, sequence)))
            return

        # 반복문 1부터 N까지의 숫자
        for i in range(1, N + 1):
            # 현재 수열에 i가 포함x일 때
            if i not in sequence:
                # i를 수열에 추가
                sequence.append(i)
                # backtrack 함수를 호출하여 다음 숫자를 추가
                backtrack(sequence)
                # 마지막에 추가한 숫자를 제거 후 다음 숫자를 추가
                sequence.pop()

    # 빈 리스트로 시작하는 backtrack 함수를 호출
    backtrack([])


# 함수를 호출하여 수열을 생성
create_sequences(N, M)