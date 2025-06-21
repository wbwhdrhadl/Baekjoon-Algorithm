arr= []
n,m = map(int,input().split())
for i in range(n):
    arr.append(0)
for i in range(m):
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        arr[i-1]=c
print(*arr)
    

    
    
    