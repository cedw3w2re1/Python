from itertools import product, permutations

"""
for s in product('АВСD', repeat=3):
    print(s)
"""
"""
for s in product('135', '246', '135'):
    print(s)
"""

"""
for s1 in 'ABCD':
    for s2 in 'ABCD':
        for s3 in 'ABCD':
            print(s1, s2, s3)
"""

for p in permutations('ABCD', 3): # перестановки без повторений
    print(''.join(p))