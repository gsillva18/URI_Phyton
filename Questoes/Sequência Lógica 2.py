x,y=input().split()
x=int(x)
y=int(y)
if((x>1 and x<20) and (y>x and y<100000)):
    a=""
    b=0
    for i in range(1,y+1):
        i=str(i)
        a+=i
        b+=1
        if(b==x):
            print(a)
            a=""
            b=0
        else:
            a+=" "