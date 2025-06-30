n = int(input())
A = []
for i in range(n):
    row = list(map(int,input().split()))
    A.append(row)

visited = [False] * n 
min_value = float('inf')

def backtracking(depth, idx):
    global min_value
    
    if(depth == n//2):
        start_team = []
        link_team = []

        for i in range(n):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)

        start_score = 0
        link_score = 0

        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                start_score += A[start_team[i]][start_team[j]]
                link_score += A[link_team[i]][link_team[j]]
        diff = abs(start_score - link_score)
        min_value = min(min_value, diff)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i]= True
            backtracking(depth+1, i+1)
            visited[i] = False    


backtracking(0,0)
print(min_value)
            
    