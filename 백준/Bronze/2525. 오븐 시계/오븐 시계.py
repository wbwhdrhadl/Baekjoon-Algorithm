a,b=input().split()
a = int(a)
b = int(b)
c = int(input())

hour = c//60
min = c%60
if(b+min>=60 and a+hour+1>=24):
        a=a+hour+1-24
        b=b+min-60
        print(a, b)
elif(b+min>=60 and a+hour+1<24):
        a=a+hour+1
        b= b+min-60
        print(a, b)
elif(b+min<60 and a+hour>=24):
        a=a+hour-24
        b=b+min
        print(a, b)
else:
        a=a+hour
        b=b+min
        print(a, b)