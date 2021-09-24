A1=int(input())
A2=int(input())
A3=int(input())

t1=(4*A3)+(2*A2)
t2=(2*A1)+(2*A3)
t3=(4*A1)+(2*A2)
if(t1<t2 and t1<t3):
    print(t1)
elif((t2<t1 and t2<t3)or(t2==t1 or t2==t3)):
    print(t2)
elif(t3<t1 and t3<t2):
    print(t3)