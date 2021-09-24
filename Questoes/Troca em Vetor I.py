x=[]
for i in range(20):
    val=int(input())
    x.append(val)
x.reverse()
for k in range(20):
    print("N[{}] = {}".format(k,x[k]))