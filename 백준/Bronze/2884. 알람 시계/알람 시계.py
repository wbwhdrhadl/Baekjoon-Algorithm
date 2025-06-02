a, b = input().split()
a = int(a)
b = int(b)
if(b<45 and a==0):
    a = 23
    b = b+15
    print(a)
    print(b)
elif(b<45 and a!=0):
    a = a-1
    b = b+15
    print(a)
    print(b)
else:
    b=b-45
    print(a)
    print(b)