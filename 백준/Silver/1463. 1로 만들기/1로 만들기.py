n = int(input())
n_number = [0] * (n+1)

if n >= 1:
    n_number[1] = 0
if n >= 2:
    n_number[2] = 1
if n >= 3:
    n_number[3] = 1


for i in range(4,n+1):
    if (i%3 == 0 and i%2 == 0 ):
        cnt = min(n_number[i//3], n_number[i//2], n_number[i-1])
    elif (i%3 == 0 and i%2!=0):
        cnt = min(n_number[i//3], n_number[i-1])       
    elif (i%3 != 0 and i%2==0):
        cnt = min(n_number[i//2], n_number[i-1])      
    else:
        cnt = n_number[i-1]

    n_number[i] = cnt+1
    
    


print(n_number[n])