# 5*x + 3*y = N

N = int(input())
sum = N
for i in range(N):
    for j in range(N):
        if(5*i + 3*j == N):
            num = i+j
            if(sum>num):
                sum = num
if(sum<N):
    print(sum)
else:
    print(-1)
            