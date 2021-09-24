lista_sim=[]
lista_nao=[]
cont=[""]
verificar=[]
cond=True
while(cond):
    nome=input().split()
    if(nome[0]=="FIM"):
        cond=False
    elif(nome[1]=="YES" and nome[0] not in lista_sim):
        lista_sim.append(nome[0])
        verificar.append(nome[0])
        if(len(nome[0])>len(cont[0])):
            cont=[]
            cont.append(nome[0])
        elif(len(nome[0])==len(cont[0])):
            cont.append(nome[0])
    elif(nome[1]=="NO"):
        lista_nao.append(nome[0])
        
lista_sim.sort()
lista_nao.sort()
lista_de_inscritos=lista_sim+lista_nao

for i in lista_de_inscritos:
    print(i)
print("")
if(len(cont)> 1):
    amigo=[]
    for k in cont:
        amigo.append(verificar.index(k))
    print("Amigo do Habay:\n{}".format(verificar[min(amigo)]))

else:
    print("Amigo do Habay:\n{}".format(cont[0]))