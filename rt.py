import random
astr=input('times= ')
a=int(astr)
d=0
e=0
for c in range(1,a+1):
    b=random.randint(0,39)
    if(b==0):
        e=e+1
    else:
        f=0
    d=d+1
print(e,' ',d)
print(d/e)
           