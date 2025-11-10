def f(n):
    b = bin(n)[2:]
    b = b.replace('0','/').replace('1','0').replace('/','1')
    r = int(b,2)
    return r

