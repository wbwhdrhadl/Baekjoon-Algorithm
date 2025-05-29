import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    stack = []
    str = input()
    is_true = True
    for j in range(len(str)):
        if(str[j]=="("):
            stack.append(0)
        elif(str[j]==")"):
            if(len(stack)==0):
                print("NO")
                is_true = False
                break
            else:
                stack.pop()

                
    if is_true == True and len(stack)==0:
        print("YES")
    elif is_true ==True and len(stack)!=0:
        print("NO")