a,b=input().split()
a=int(a)
b=int(b)
x=a-b
if(x==0):
    print("O JOGO DUROU 24 HORA(S)")
elif(x<0):
    x=x*-1
    print("O JOGO DUROU {} HORA(S)".format(x))
else:
    x=(x-24)*-1
    print("O JOGO DUROU {} HORA(S)".format(x))