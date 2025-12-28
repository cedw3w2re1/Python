import itertools

list_v = itertools.product('НАСТЯ', repeat = 6)
n = 0

for str in list_v:
    line = ''.join(str)
    if line.count('А') < 2 and line.count('Я') < 2:
        n += 1
print(n)

