par=[]
impar=[]
for i in range(15):
    x=int(input())
        
    if(x%2==0 ):
        par.append(x)
        if(len(par)==5 ):
            for j in range(len(par)):
                print("par[{}] = {}".format(j,par[j]))
            par=[]
    else:
        impar.append(x)
        if(len(impar)==5 ):
            for k in range(len(impar)):
                print("impar[{}] = {}".format(k,impar[k]))
            impar=[]
    if(i>=10 and len(par)+len(impar)==5):
        for k in range(len(impar)):
                print("impar[{}] = {}".format(k,impar[k]))
        impar=[]
        for j in range(len(par)):
                print("par[{}] = {}".format(j,par[j]))
        par=[]