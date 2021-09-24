x=1
while(x!=0):
    x=int(input())
    if(x!=0):
        a=""
        for i in range(1,x+1):
            i=str(i)
            a+=i
            i=int(i)
            if(i<x):
                a+=" "
        print(a)