hour, minutes = map(int, input().split())
cook = int(input())

total = hour * 60 + minutes + cook

hour = total // 60
minutes = total % 60

if hour >= 24:
    hour %= 24

print(hour, minutes)