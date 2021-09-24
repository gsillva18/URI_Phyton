x=float(input())
n=[]
n.append(x)
for i in range(100):
   print("N[{}] = {:.4f}".format(i,n[i]))
   n.append(n[i]/2)
