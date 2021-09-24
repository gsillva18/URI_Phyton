j=3
for i in range(1,10,2):
    j+=4
    for k in range(3):
        print("I={} J={}".format(i,j-k))
    j-=2