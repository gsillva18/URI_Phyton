n=int(input())
if(n>2 and n<1000):
    for i in range(1,11):
        print("{} x {} = {}".format(i,n,i*n))