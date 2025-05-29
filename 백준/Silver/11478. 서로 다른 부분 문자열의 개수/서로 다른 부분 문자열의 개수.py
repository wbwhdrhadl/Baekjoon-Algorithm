s = input()
ans = set()
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        sub = s[i:j]
        ans.add(sub)


print(len(ans))