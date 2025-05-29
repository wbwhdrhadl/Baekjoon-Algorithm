a1 = []
for i in range(9):
        row = list(map(int,input().split()))
        a1.append(row)

max = a1[0][0]
x = 1
y = 1

for i in range(9):
    for j in range(9):
        if (max<a1[i][j]):
            max = a1[i][j]
            x = i+1
            y = j+1
print(max)
print(x,y)
        
    