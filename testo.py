def aint(sst):          #输入数字处理
    sstr=sst
    if(sstr[0]=="-"):
        sstrl=sstr.partition("-")
        sstr1=sstrl[-1]
        s=0-int(sstr1)
    else:
        s=int(sst)
    return s
w=0
while(w==0):
    astr=input('a= ')
    bstr=input('b= ')
    cstr=input('c= ')
    print(' ')

    a=aint(astr)
    b=aint(bstr)
    c=aint(cstr)
    delta=b*b-4*a*c
    print('∆= ',delta)
    deltaL=[]
    if(delta>0):
        for i in range(1,delta):
            if(delta%i==0):
                g=delta/i
                deltaL.append(g)
        print(deltaL)
    if(delta<0):
        print('no real root')
    else:
        x1=((0-b)+(delta)**0.5)/(2*a)
        x2=((0-b)-(delta)**0.5)/(2*a)
        print('x1= ',x1)
        print('x2= ',x2)
        sqrO=[]
    for j in range(1,len(deltaL)+1):
        sqr=deltaL.pop(0)
        if((sqr**0.5)%1==0):
            sqrt=sqr**0.5
            sqrO.append(sqrt)
            print(sqrO)
        
    print(' ')
