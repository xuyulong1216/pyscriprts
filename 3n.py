astr=input("a= ")
a=int(astr)
b=0
while(a!=1):
    if(a%2==0):
        a=a/2
    else:
        a=3*a+1
    b=b+1
    print(b," ",a)
