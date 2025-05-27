arr = list(map(int,input().split()))

for i in range(-999,1000):
    for j in range(-999,1000):
        if(i*arr[0]+j*arr[1]==arr[2] and i*arr[3]+j*arr[4]==arr[5]):
            print(i, j)