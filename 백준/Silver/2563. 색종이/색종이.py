n = int(input())
a = [[0]*100 for _ in range(100)]
coordinates = []
for i in range(n):
    x,y = map(int,input().split())

    for j in range(x,x+10):
        for k in range(y,y+10):
            a[j][k]=1

total_area = 0
for i in range(100):
    for j in range(100):
        if (a[i][j]==1):
            total_area+=1

print(total_area)