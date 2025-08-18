import sys
input = sys.stdin.readline

MOD = 1_000_000_007

n,k = map(int,input().split())

fac = [1] * (n+1)
for i in range(1, n+1):
    fac[i]= fac[i-1]*i % MOD
    
def recursion(n):
    return pow(n,MOD-2,MOD)
answer = fac[n] * recursion(fac[k]) % MOD
answer = answer * recursion(fac[n-k]) % MOD

print(answer)