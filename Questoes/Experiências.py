n=int(input())
total=0
rato=0
sapo=0
coelho=0
for i in range(n):
    q,a=input().split()
    q=int(q)
    total+=q
    if(a=="R"):
        rato+=q
    elif(a=="S"):
        sapo+=q
    elif(a=="C"):
        coelho+=q

print("Total: {} cobaias".format(total))
print("Total de coelhos:", coelho)
print("Total de ratos:", rato)
print("Total de sapos:", sapo)
print("Percentual de coelhos: {:.2f} %".format((coelho*100)/total))
print("Percentual de ratos: {:.2f} %".format((rato*100)/total))
print("Percentual de sapos: {:.2f} %".format((sapo*100)/total))