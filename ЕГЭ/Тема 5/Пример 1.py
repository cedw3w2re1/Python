def f(n):
    b = bin(n)[2:]
    b += '1' if b.count('1') % 2 == 0 else '0' # b += str(1 - b.count('1') % 2)
    b += '1' if b.count('1') % 2 == 0 else '0'
    return int(b, 2)

n = 1
while True:
    r = f(n)
    if r > 54:
        print(r)
        break
    n += 1