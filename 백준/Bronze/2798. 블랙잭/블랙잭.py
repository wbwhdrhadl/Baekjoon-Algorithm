n, m = map(int,input().split())
card = list(map(int,input().split()))
max = 0
for i in range(0, len(card)):
    total = 0
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            total = card[i]+card[j]+card[k]
            if(total<=m and max<total):
                max = total

print(max)