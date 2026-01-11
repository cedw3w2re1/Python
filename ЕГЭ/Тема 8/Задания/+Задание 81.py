import  itertools

string = 'РОСМАХ'



r= 'РСМХ'
o = 'ОА'

def check_repetitions(s):
    if s.count('Р')!= 1 :
        return False
    elif s.count('О')!= 2 :
        return False
    elif s.count('С')!= 1 :
        return False
    elif s.count('М')!= 1 :
        return False
    elif s.count('А')!= 2 :
        return False
    elif s.count('Х')!= 1 :
        return False
    else:
        return True


def check_two_letters(s):
    for i in range(len(s)-1):
        if s[i] in r and s[i+1] in r:
            return False
        elif s[i] in o and s[i+1] in o:
            return False
    return True


if __name__ =="__main__":
    list_v = itertools.product('РОСМАХ', repeat = 8)

    count = 0
    for combo in list_v:
        word = ''.join(combo)
        if(check_repetitions(word) and check_two_letters(word)):
            count+=1

    print(count)





answer = 288
#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 81, answer, '48aedb8880cab8c45637abc7493ecddd'))