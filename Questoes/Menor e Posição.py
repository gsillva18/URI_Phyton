x=[]
n=int(input())
val=input().split()
for i in range(n):
    x.append(int(val[i]))

print("Menor valor:", min(x))
print("Posicao:", x.index(min(x)))