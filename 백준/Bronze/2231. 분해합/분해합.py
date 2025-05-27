n = int(input()) 

for i in range(n):
    generator = i
    temp = i
    while temp >0:
        r=temp%10
        temp=temp//10   
        generator +=r
    if(generator == n):
        print(i)
        break
else:
    print(0)
        