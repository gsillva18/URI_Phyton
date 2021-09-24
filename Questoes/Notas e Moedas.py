val=float(input())
print("NOTAS:")
x=val//100
print("{:.0f} nota(s) de R$ 100.00".format(x))
y=(val%100)//50
print("{:.0f} nota(s) de R$ 50.00".format(y))
z=((val%100)%50)//20
print("{:.0f} nota(s) de R$ 20.00".format(z))
a=(((val%100)%50)%20)//10
print("{:.0f} nota(s) de R$ 10.00".format(a))
b=((((val%100)%50)%20)%10)//5
print("{:.0f} nota(s) de R$ 5.00".format(b))
c=(((((val%100)%50)%20)%10)%5)//2
print("{:.0f} nota(s) de R$ 2.00".format(c))
print("MOEDAS:")
d=((((((val%100)%50)%20)%10)%5)%2)//1
print("{:.0f} moeda(s) de R$ 1.00".format(d))
e=(((((((val%100)%50)%20)%10)%5)%2)%1)//0.50
print("{:.0f} moeda(s) de R$ 0.50".format(e))
f=((((((((val%100)%50)%20)%10)%5)%2)%1)%0.50)//0.25
print("{:.0f} moeda(s) de R$ 0.25".format(f))
g=(((((((((val%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)//0.10
print("{:.0f} moeda(s) de R$ 0.10".format(g))
h=((((((((((val%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)//0.049
print("{:.0f} moeda(s) de R$ 0.05".format(h))
i=(((((((((((val%100)%50)%20)%10)%5)%2)%1)%0.50)%0.25)%0.10)%0.05)//0.0099
print("{:.0f} moeda(s) de R$ 0.01".format(i))