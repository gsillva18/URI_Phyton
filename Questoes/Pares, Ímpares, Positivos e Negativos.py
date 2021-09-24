n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
x=0
y=0
z=0
w=0
if(n1%2==0):
    x+=1
else:
    y+=1
    
if(n2%2==0):
    x+=1
else:
    y+=1
    
if(n3%2==0):
    x+=1
else:
    y+=1
    
if(n4%2==0):
    x+=1
else:
    y+=1
    
if(n5%2==0):
    x+=1
else:
    y+=1
    
if(n1>0):
    z+=1
elif(n1<0):
    w+=1

if(n2>0):
    z+=1
elif(n2<0):
    w+=1

if(n3>0):
    z+=1
elif(n3<0):
    w+=1

if(n4>0):
    z+=1
elif(n4<0):
    w+=1

if(n5>0):
    z+=1
elif(n5<0):
    w+=1
    
print(x, "valor(es) par(es)")
print(y, "valor(es) impar(es)")
print(z, "valor(es) positivo(s)")
print(w, "valor(es) negativo(s)")