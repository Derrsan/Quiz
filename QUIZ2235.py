n=input()
(A,B,C)=n.split(" ")
A=int(A)
B=int(B)
C=int(C)
P=2025
if (A==B or A==C or B==C):
    print("S")
elif (A+C==B or A+B==C or B+C==A):
    print ("S")
elif (A-B==C or A-C==B or B-C==A):
    print("S")
else:
    print("N")