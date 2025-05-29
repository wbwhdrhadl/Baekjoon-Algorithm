n, b = map(int,input().split())
answer = []
num = n
while num!=0 :
    rem = num % b 
    num = num // b 

    answer.append(rem)
    
for i in range(len(answer)-1,-1,-1):
    if(0 <= answer[i] <= 9):
        print(chr(ord('0')+answer[i]), end="")
    else:
        print(chr(ord('A')+answer[i]-10), end="")