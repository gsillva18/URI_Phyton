val=int(input())
x=[val]
for i in range(10):
    print("N[{}] = {}".format(i,x[i]))
    x.append(x[i]*2)