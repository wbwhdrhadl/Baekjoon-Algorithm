import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    num = input().split()
    if(num[0] == '1'):
        x = int(num[1])
        stack.append(x)
        

    elif(num[0] == '2'):
        if(len(stack)==0):
            print(-1)
        else:
            print(stack.pop())

    elif(num[0] == '3'):
        print(len(stack))

    elif(num[0] == '4'):
        if(len(stack)==0):
            print(1)
        else:
            print(0)

    else:
        if(len(stack)==0):
            print(-1)
        else:
            print(stack[-1])