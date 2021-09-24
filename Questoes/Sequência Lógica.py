n=int(input())
if(n>1 and n<1000):
    for i in range(1,n+1):
        for k in range(1,3):
            x=i**2
            y=i**3
            if(k==2):
                x=i**2+1
                y=i**3+1
            print(i, x, y)