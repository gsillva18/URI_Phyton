lista=input().split()
a=int(lista[0])
n=int(lista[len(lista)-1])
b=0
for i in range(n):
    if(i>=0 and i<=n-1):
        b+=a+i
print(b)