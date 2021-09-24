n,k=input().split()
n=int(n)
k=int(k)
lista=[]
for i in range(n):
    nome=input()
    lista.append(nome)
lista.sort()
print(lista[k-1])
    