k = int(input())

w = k%10

if w == 1 and k%100 != 11:
    print('гриб')
elif 2 <= w <= 4 and 12 < k%100 > 14:
    print("грибa")
else:
    print("грибов")