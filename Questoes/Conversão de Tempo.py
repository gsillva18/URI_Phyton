n=int(input())
x=n//3600
y=(n%3600)//60
z=(n%3600)%60
print("{}:{}:{}".format(x,y,z))