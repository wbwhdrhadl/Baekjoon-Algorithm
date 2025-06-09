n = int(input())
score = []
score2 = [] 
score = list(map(int,input().split()))
max = max(score)
sum = 0
for i in range(n):
    score[i]=score[i]/max*100
    sum=sum+score[i]

print(sum/n)
    