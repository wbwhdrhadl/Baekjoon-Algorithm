s_arr= []
for i in range(5):
    s=input()
    s_arr.append(s)
# print(s_arr)

max_len = max(len(s) for s in s_arr)

for i in range(max_len):
    for j in range(5):
        if i< len(s_arr[j]):
            print(s_arr[j][i], end="")