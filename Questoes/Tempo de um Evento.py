di,numdi=input().split()
numdi=int(numdi)
hi,mi,si=input().split(":")
hi=int(hi)
mi=int(mi)
si=int(si)
df,numdf=input().split()
numdf=int(numdf)
hf,mf,sf=input().split(":")
hf=int(hf)
mf=int(mf)
sf=int(sf)
res=(numdi*86400+3600*hi+60*mi+si)-(numdf*86400+3600*hf+60*mf+sf)
if(res<0):
    res*=-1
elif(res>0):
    res=2592000-res

w=res//86400
x=(res%86400)//3600
y=((res%86400)%3600)//60
z=((res%86400)%3600)%60

print(w, "dia(s)")
print(x, "hora(s)")
print(y, "minuto(s)")
print(z, "segundo(s)")