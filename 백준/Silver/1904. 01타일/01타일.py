def tile(n):
    if n == 1:
        return 1
    f = [0]* (n+1)
    f[1] = 1
    f[2] = 2
    for i in range(3, n+1):
        f[i]= (f[i-2]+ f[i-1]) % 15746
    return f[n]

n = int(input())
print(tile(n))