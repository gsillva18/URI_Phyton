z=0
while(z!=1):
    n=0
    notaf=0
    while(n!=2):
        nota=float(input())
        if(nota>=0 and nota<=10):
            notaf+=nota
            n+=1
        else:
            print("nota invalida")
    print("media = {:.2f}".format(notaf/2))
    while(n!=3):
        print("novo calculo (1-sim 2-nao)")
        m=int(input())
        if(m==1):
            n=3
        elif(m==2):
            z=1
            n=3