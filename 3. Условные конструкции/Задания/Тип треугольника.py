a = int(input())
b = int(input())
c = int(input())
h = max(a,b,c)
k1 = min(a,b,c)
k2 = sum(a,b,c) - (h+k1)


if a + b > c and b + c > a and c + a > b:
    if h**2 == k1**2 + k2**2:
        print('пр')
    if h**2 > k1**2 + k2**2:
        print('ту')
    if h**2 < k1**2 + k2**2:
        print('ос')
else:
    print("не с")
