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
    xstr=input('x= ')

    a=aint(astr)
    b=aint(bstr)
    c=aint(cstr)
    x=aint(xstr)
    
    y=x*x*a+x*b+c
    print(' ')
    print('y=',y)
    print(' ')
