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