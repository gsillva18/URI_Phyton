A,B,C=input().split()
A=int(A)
B=int(B)
C=int(C)
if((-100<=A,B,C)and(A,B,C<=100)):
    if((A>B) and (B<=C)):
        print(":)")
    elif((A<B) and (B>=C)):
        print(":(")
    elif((A<B) and (B<C) and (C-B)<(B-A)):
        print(":(")
    elif((A<B) and (B<C) and (C-B)>=(B-A)):
        print(":)")
    elif((A>B) and (B>C) and (C-B)>(B-A)):
        print(":)")
    elif((A>B) and (B>C) and (C-B)<=(B-A)):
        print(":(")
    elif(A==B):
        if(B<C):
            print(":)")
        else:
            print(":(")