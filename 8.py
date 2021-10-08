def perevod(p):
    d=''
    while p>0:
        d=str(p%n)+d
        p = p//n    
    print ("число в заданной Вами системе счисления:", d)
try:
    print ("введите число") 
    p=int(input())
    print ("введите систему счисления от 1 до 9")
    n=int(input())
except ValueError:
    print ("введены некорректные данные")
    exit()
if (n<10) and (n>1) and (p>-1):
    perevod(p)
else: 
    print ("введены некорректные данные")