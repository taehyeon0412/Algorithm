import sys
input = sys.stdin.readline

# N 입력 받음
N = int(input().strip())

# 좌표 입력 받음
coords = list(map(int, input().strip().split()))

# 중복 제거 후 정렬
unique_coords = sorted(set(coords))

# 좌표 값 매핑
coord_map = {coord: index for index, coord in enumerate(unique_coords)}

# 원래 좌표에 대한 압축 좌표 변환
compressed_coords = [coord_map[coord] for coord in coords]

# 결과 출력
print(' '.join(map(str, compressed_coords)))