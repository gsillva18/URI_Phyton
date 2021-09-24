for i in range(0,21,2):
    if(i==0):
        i=i
    elif(i==10 or i==20):
        i=int(i/10)
    else:
        i/=10
    for k in range(1,4):
        print("I={} J={}".format(i, k+i))