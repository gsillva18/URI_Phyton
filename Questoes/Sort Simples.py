n1,n2,n3=input().split()
n1=int(n1)
n2=int(n2)
n3=int(n3)
print(min(n1,n2,n3))
if((n2<n1 and n1<n3)or(n3<n1 and n1<n2)):
    print(n1)
elif((n1<n2 and n2<n3)or(n3<n2 and n2<n1)):
    print(n2)
elif((n1<n3 and n3<n2)or(n2<n3 and n3<n1)):
    print(n3)
print(max(n1,n2,n3))
print("")
print(n1)
print(n2)
print(n3)