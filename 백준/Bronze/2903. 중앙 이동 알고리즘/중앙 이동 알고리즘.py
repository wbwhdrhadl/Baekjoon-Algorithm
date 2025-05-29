n = int(input())
m = 0
def num(n):
    if(n == 0):
        m = 2
        return 2
    else:
        m = num(n-1)*2-1
        return num(n-1)*2-1

sum = num(n)*num(n)
print(sum)