x=0
while(x!=1):
    y=""
    z=0
    m,n=input().split()
    m=int(m)
    n=int(n)
    if(m<=0 or n<=0):
        x=1
    else:
        for i in range(min(m,n),max(m,n)+1,1):
            i=str(i)
            y+=i
            i=int(i)
            z+=i
        y=" ".join(y)
        print("{} Sum={}".format(y,z))