import itertools
n = 0
list_v = itertools.product('01234567', repeat = 5)

for str in list_v:
    line = ''.join(str)
    if line.count('6') == 1 and line.count('16') == 0 and line.count('61')==0 and line.count('63') ==0 and line.count('36') == 0 and line.count('76') == 0 and line.count('67') == 0 and line.count('56') == 0 and line.count('65') == 0 and line[0] != '0':
        n += 1
print(n)



