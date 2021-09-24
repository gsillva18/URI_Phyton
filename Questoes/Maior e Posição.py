con=[]
y=0
for i in range(100):
    x=int(input())
    con.append(x)
    if(x==max(con)):
        z=x
        y=i+1
print(z)
print(y)