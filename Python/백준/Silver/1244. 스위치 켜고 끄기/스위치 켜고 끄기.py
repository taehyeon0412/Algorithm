# 정해진 규칙에 따라 스위치를 바꾸는 문제
# 남학생 = 주어진 숫자의 배수에 해당하는 스위치
# 여학생 = 주어진 숫자를 중심으로 좌우대칭 구간 / 구간에 속한 스위치 개수는 항상 홀수

import sys
input = sys.stdin.read

# 입력
# 전체를 한번에 받아서 data에 저장함
data = input().split()

# 스위치 개수 첫번째 요소
switch_num = int(data[0])

# 스위치 상태 공백을 기준으로 리스트
# 데이터의 두번째 요소 ~ switch_num +1까지(마지막은 안들어감)
switch = list(map(int, data[1:switch_num + 1]))

# 학생 수
student_num = int(data[switch_num + 1])

# 학생 정보 끝까지
student_data = data[switch_num + 2:]

# 스위치 상태
# 학생 수만큼 반복
for i in range(student_num):
    # 각 학생의 성별을 가져옴
    gender = int(student_data[2 * i])
    # 각 학생의 받은 숫자를 가져옴
    num = int(student_data[2 * i + 1])

    # 남학생
    if gender == 1:
        # 스위치 3번이면 인덱스는 2번 / 인덱스는 0부터 시작하기 때문
        for k in range(num - 1, switch_num, num):
            if switch[k] == 0:
                switch[k] = 1
            else:
                switch[k] = 0

    # 여학생
    elif gender == 2:
        # 인덱스 초기화
        idx = [num - 1]
        # 좌우 대칭 구간 찾기
        for j in range(1, switch_num):
            left, right = num - j, num + j
            # 인덱스가 범위를 벗어나면 중단
            if left < 1 or right > switch_num:
                break
            # 좌우 대칭이 아니면 중단
            if switch[left - 1] != switch[right - 1]:
                break
            # 대칭이면 인덱스에 추가
            else:
                idx.append(left - 1)
                idx.append(right - 1)

        # 대칭일때 변경
        for j in idx:
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0

# 출력
for i in range(0, switch_num, 20):
    print(" ".join(map(str, switch[i:i + 20])))