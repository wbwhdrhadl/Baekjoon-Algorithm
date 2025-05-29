n = int(input())
stack = []

for i in range(n):
    num = int(input())
    if(num == 0):
        stack.pop()
    else:
        stack.append(num)

sum = 0
for j in range(len(stack)):
    sum+=stack[j]

print(sum)