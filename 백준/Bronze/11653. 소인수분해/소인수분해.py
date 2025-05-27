n = int(input())

while(n!=1):
    for j in range(2,n+1):
        while(n%j==0):
            if(n%j==0):
                n=n//j
                print(j)
            