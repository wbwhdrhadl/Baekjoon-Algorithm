N, B = input().split()
B = int(B)


sum = 0

for i in range(len(N)):
    
    if('0'<=N[i]<='9'):
        total = ord(N[i])-ord('0')
    else:
        total = ord(N[i])-ord('A')+10
    sum+=total*(B**(len(N)-i-1))
print(sum)