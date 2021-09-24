x=int(input())
y=int(input())
mai=max(x,y)
men=min(x,y)
z=0
for i in range(men+1,mai):
    if(i%2==1):
        z+=i
print(z)