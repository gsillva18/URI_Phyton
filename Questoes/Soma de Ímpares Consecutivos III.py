n=int(input())
for i in range(n):
    x,y=input().split()
    x=int(x)
    y=int(y)
    b=0
    a=0
    while(a!=y):
        if(x%2==1):
            a+=1
            b+=x
        x+=1
    print(b)