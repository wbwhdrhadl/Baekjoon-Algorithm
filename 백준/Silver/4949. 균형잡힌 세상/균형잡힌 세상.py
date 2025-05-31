import sys
input = sys.stdin.readline

while True:
    sent = input()
    if sent == ".\n":
        break
        
    stack = []
    is_pair = True
    for i in range(len(sent)):
        if(sent[i]=="("):
            stack.append(0)
        elif(sent[i]==")"):
            if(len(stack)>0 and stack[-1]==0):
                stack.pop()
            else:
                is_pair = False
        elif(sent[i]=="["):
            stack.append(1)
        elif(sent[i]=="]"):
            if(len(stack)>0 and stack[-1]==1):
                stack.pop()
            else:
                is_pair = False
    if(is_pair == True and len(stack)==0):
        print("yes")
    else:
        print("no")    
            