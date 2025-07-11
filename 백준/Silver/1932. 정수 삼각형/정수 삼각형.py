n = int(input())
tri = []

for _ in range(n):
    row = list(map(int,input().split()))
    tri.append(row)

for i in range(n-2,-1,-1):
    for j in range(len(tri[i])):
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])

print(tri[0][0])