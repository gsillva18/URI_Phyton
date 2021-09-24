n=0
vti=0
vtg=0
qg=0
empate=0
while(n!=1):
    i,g=input().split()
    i=int(i)
    g=int(g)
    if(i>g):
        vti+=1
        vencedor="Inter"
    elif(g>i):
        vtg+=1
        vencedor="Gremio"
    elif(i==g):
        empate+=1
        vencedor="Nao houve vencedor"
    qg+=1
    n1=0
    while(n1!=1):
        print("Novo grenal (1-sim 2-nao)")
        ng=int(input())
        if(ng==1):
            n1=1
        elif(ng==2):
            n=1
            n1=1
print(qg, "grenais")
print("Inter:{}".format(vti))
print("Gremio:{}".format(vtg))
print("Empates:{}".format(empate))
print(vencedor ,"venceu mais")