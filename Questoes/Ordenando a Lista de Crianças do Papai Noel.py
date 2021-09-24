n=int(input())
lista=[]
comportado=0
nao_comportado=0
for i in range(n):
    sinal,nome=input().split()
    if(sinal=="+"):
        comportado+=1
    else:
        nao_comportado+=1
        
    lista.append(nome)
    
lista.sort()

for k in lista:
    print(k)
    
print("Se comportaram: {} | Nao se comportaram: {}".format(comportado,nao_comportado))