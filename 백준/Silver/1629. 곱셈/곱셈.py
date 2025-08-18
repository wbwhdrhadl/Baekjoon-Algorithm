import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())


def power(a,b,c):
    if b == 0:
        return 1

    half = power(a,b//2,c)
    half = (half*half) % c
    if b % 2 ==0:
        return half
    else:
        return (half*a) % c
    
print(power(a,b,c))