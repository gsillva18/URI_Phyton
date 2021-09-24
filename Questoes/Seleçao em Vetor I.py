x=[]
for i in range(100):
    v=float(input())
    x.append(v)
    if(v<=10):
        print("A[{}] = {}".format(i,x[i]))