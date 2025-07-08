MAX = 100
f = [0] * (MAX+1)
f[1] = f[2] = f[3] = 1
f[4] = f[5] = 2
for i in range(6, MAX+1):
    f[i]= (f[i-1]+ f[i-5])

n = int(input())
for i in range(n):
    t = int(input())
    print(f[t])