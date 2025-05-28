n,m = map(int,input().split())
line = []
for i in range(n):
    row = input().strip()
    line.append(list(row))

min_num = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        count1 = 0
        count2 = 0

        for x in range(8):
            for y in range(8):
                current = line[i+x][j+y]
                if (x+y)%2 == 0:
                    if current != 'W':
                        count1 +=1
                    if current != 'B':
                        count2 +=1
                else:
                    if current !='B':
                        count1 +=1
                    if current !='W':
                        count2 +=1

        min_num = min(min_num, count1,count2)

print(min_num)

            