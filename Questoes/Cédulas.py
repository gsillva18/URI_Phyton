valor=int(input())
print(valor)
x=valor//100
print(x, "nota(s) de R$ 100,00")
y=(valor%100)//50
print(y, "nota(s) de R$ 50,00")
z=((valor%100)%50)//20
print(z, "nota(s) de R$ 20,00")
k=(((valor%100)%50)%20)//10
print(k, "nota(s) de R$ 10,00")
w=((((valor%100)%50)%20)%10)//5
print(w, "nota(s) de R$ 5,00")
q=(((((valor%100)%50)%20)%10)%5)//2
print(q, "nota(s) de R$ 2,00")
m=((((((valor%100)%50)%20)%10)%5)%2)//1
print(m, "nota(s) de R$ 1,00")