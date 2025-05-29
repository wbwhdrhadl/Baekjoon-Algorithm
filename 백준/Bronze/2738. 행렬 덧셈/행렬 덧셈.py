n,m = map(int,input().split())

a = []
b = []
answer = []

for i in range(n):
        row = list(map(int,input().split()))
        a.append(row)

for i in range(n):
        row = list(map(int,input().split()))
        b.append(row)

for i in range(n):
    row = []
    for j in range(m):
        row.append(a[i][j]+b[i][j])
    answer.append(row)
    
for row in answer:
    print(*row)
