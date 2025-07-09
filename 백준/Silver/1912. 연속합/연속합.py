n = int(input())
n_array = list(map(int, input().split()))
f = [-1000] * (n+1)
def find_max(n_array,n):
    f[0] = n_array[0]
    for i in range(1,n):
        if f[i-1]>0:
            f[i]= f[i-1] + n_array[i]
        else:
            f[i] = n_array[i]
    return max(f)

print(find_max(n_array,n))
