a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

is_true = True
for n in range(n0, 101): 
    if a1 * n + a0 > c * n: 
        is_true = False
        break
        
print(1 if is_true else 0)
