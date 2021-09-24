n=int(input())
if(n>=1 and n<=100):
    for i in range(n):
        y=0
        x=int(input())
        for k in range(1,x+1):
            if(x%k==0):
                y+=1
        if(y==2):
            print(x, "eh primo")
        elif(y!=2):
            print(x, "nao eh primo")