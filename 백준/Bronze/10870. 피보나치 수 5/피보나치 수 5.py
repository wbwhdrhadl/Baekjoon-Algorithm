n = int(input())

def pibo(x):
    if(x==0):
        return 0
    elif(x==1):
        return 1
    else:
        return pibo(x-2)+pibo(x-1)

print(pibo(n))