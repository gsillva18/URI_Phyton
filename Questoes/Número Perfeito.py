n=int(input())
if(n>=1 and n<=20):
    for i in range(n):
        y=0
        x=int(input())
        for k in range(1,x):
            if(x%k==0):
                y+=k
        if(x==y):
            print(x, "eh perfeito")
        elif(x!=y):
            print(x, "nao eh perfeito")