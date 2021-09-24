n=int(input())
for i in range(n):
    z=0
    x,y=input().split()
    x=int(x)
    y=int(y)
    mai=max(x,y)
    men=min(x,y)
    for k in range(men+1,mai,1):
        if(k%2==1):
            z+=k
    print(z)