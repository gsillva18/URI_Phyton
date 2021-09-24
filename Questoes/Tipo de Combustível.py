op=1
a=0
g=0
d=0
while(op>=1):
    op=int(input())
    if(op==1):
        a+=1
    elif(op==2):
        g+=1
    elif(op==3):
        d+=1
    elif(op==4):
        op=0
print("MUITO OBRIGADO")
print("Alcool:", a)
print("Gasolina:", g)
print("Diesel:", d)