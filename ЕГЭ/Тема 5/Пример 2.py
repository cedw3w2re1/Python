def f(n):
    b = bin(n)[2:]
    b += b[1] + b[0]
    return int(b, 2)

n = 2
while True:
    if f(n) > 90:
        print(n)
        break
    n += 1