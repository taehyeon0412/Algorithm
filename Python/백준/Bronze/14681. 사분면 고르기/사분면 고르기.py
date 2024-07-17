a = int(input())
b = int(input())


if 0 < a and 0 < b:
    print(1)
elif a < 0 and 0 < b:
    print(2)
elif a < 0 and b < 0:
    print(3)
elif 0 < a and b < 0:
    print(4)