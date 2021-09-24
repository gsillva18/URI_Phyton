n=int(input())
if(n>1 and n<1000):
    for i in range(1,n+1):
        x=i**2
        y=i**3
        print(i, x, y)