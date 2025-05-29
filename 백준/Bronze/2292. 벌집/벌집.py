n = int(input())

sum = 1
if(n==1):
    print(1)
else:
    for i in range(1,n+1):
        if(sum<n):
            sum+=6*i
        elif(sum>=n):
            print(i)
            break
        
        
    