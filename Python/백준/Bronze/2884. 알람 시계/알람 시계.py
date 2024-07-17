hour, minutes = map(int, input().split())

total = hour * 60 + minutes - 45

hour = total // 60
minutes = total % 60

if hour < 0:
    hour += 24

print(hour, minutes)