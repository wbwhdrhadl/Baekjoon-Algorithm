n = int(input())

line = 1
while n>line:
    n-=line
    line+=1

if line % 2 == 0:
    left = n
    right = line - n +1

else:
    left = line - n + 1
    right = n

print(f"{left}/{right}")
    