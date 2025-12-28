from itertools import product
count = 1
for p in product('УОА', repeat=6):
    if ''.join(p) == 'ОУУУОО':
        break
    count += 1
print(count)