a = int(input())
s = 0

while a != 0:
    if a > s:
        s = a
    a = int(input())

print(s)