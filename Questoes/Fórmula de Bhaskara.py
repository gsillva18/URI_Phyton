a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
delta=b**2-4*a*c
if(delta>0 and a!=0):
    x1=(-b+delta**0.5)/(2*a)
    x2=(-b-delta**0.5)/(2*a)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))
elif(delta<=0 or a==0.0):
    print("Impossivel calcular")