n=int(input())
if(n>0 and n<46):
    a=""
    x=0
    y=0
    for i in range(n):
        z=x+y
        x=z
        z=str(z)
        a+=z
        if(i==0):
            y=1
        else:
            z=int(z)
            y=z-y
        if(i==n-1):
            print(a)
        else:
            a+=" "