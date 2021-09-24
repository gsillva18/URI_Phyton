t=int(input())
cont=0
for i in range(1000):
    if(cont==t):
        cont=0
    print("N[{}] = {}".format(i,cont))
    cont+=1
