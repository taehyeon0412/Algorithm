# 첫 세 음과 일치하는 노래 제목을 찾아내는 문제
# 일치하는 노래가 1개면 제목 출력
# 일치하는 노래가 2개 이상이면 ? 출력
# 일치하는 노래가 없으면 ! 출력

import sys
input = sys.stdin.readline

# 노래 개수 N, 맞히기 시도 개수 M
N, M = map(int, input().strip().split())

# 노래 목록 초기값
music_list = []

# 입력한 노래 목록 추가 for문
for _ in range(N):
    music_data = input().strip().split()
    # 노래 이름
    music_name = music_data[1]
    # 첫 세 음을 비교하기 쉽게 join로 합쳐서 넣어줌
    music_note = "".join(music_data[2:5])
    music_list.append((music_name, music_note))

# 노래 목록에 있는 음이름과 입력한 음이름 비교
for _ in range(M):
    input_note = "".join(input().strip().split())

    # 일치하는 노래 찾기
    match = None
    for music_name, music_note in music_list:
        if music_note == input_note:
            if match is None:
                match = music_name
            else:
                match = "?"
                break

    if match is None:
        print('!')
    else:
        print(match)

    # None = 아무것도 없음