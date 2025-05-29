n, m = map(int,input().split())
n_arr = []
m_arr = []
for i in range(n):
    word = input()
    n_arr.append(word)
n_map = set(n_arr)

sum = 0
for j in range(m):
    word = input()
    if(word in n_map):
        sum+=1
print(sum)
    

