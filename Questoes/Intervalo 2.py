n=int(input())
y=0
z=0
for i in range(n):
    x=int(input())
    if(x>=10 and x<=20):
        y+=1
    else:
        z+=1
        
print(y, "in")
print(z, "out")
