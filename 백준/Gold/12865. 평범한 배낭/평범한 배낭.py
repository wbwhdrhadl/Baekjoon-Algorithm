n, k = map(int,input().split())

pairs = []

for i in range(n):
    a,b = map(int,input().split())
    pairs.append((a,b))

pairs.sort()


# dp 작성
dp = [0] * (k+1)


for a, b in pairs:
    for weight in range(k, a-1, -1):
        dp[weight] = max(dp[weight], dp[weight-a] + b) 

print(max(dp))
    
    