n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
n5=float(input())
n6=float(input())
if(n1!=0 and n2!=0 and n3!=0 and n4!=0 and n5!=0 and n6!=0):
    x=0
    if(n1>0):
      x+=1
    if(n2>0):
      x+=1
    if(n3>0):
      x+=1
    if(n4>0):
      x+=1
    if(n5>0):
      x+=1
    if(n6>0):
      x+=1
    print("{} valores positivos".format(x))