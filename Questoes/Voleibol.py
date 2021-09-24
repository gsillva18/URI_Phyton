n=int(input())
st=0
bt=0
at=0
sc=0
bc=0
ac=0
for g in range(n):
    nome=input()
    s,b,a=input().split()
    s1,b1,a1=input().split()
    st+=int(s)
    bt+=int(b)
    at+=int(a)
    sc+=int(s1)
    bc+=int(b1)
    ac+=int(a1)
print("Pontos de Saque: {:.2f} %.".format((sc*100)/st))
print("Pontos de Bloqueio: {:.2f} %.".format((bc*100)/bt))
print("Pontos de Ataque: {:.2f} %.".format((ac*100)/at))