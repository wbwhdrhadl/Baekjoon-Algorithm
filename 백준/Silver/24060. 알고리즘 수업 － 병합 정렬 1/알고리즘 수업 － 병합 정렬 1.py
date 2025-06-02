n,k = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
result = -1

def merge_sort(A,p,r):
    if(p < r):
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    global cnt, result
    tmp = []
    i = p
    j = q+1

    while(i<=q and j<=r):
        if(A[i]<=A[j]):
            tmp.append(A[i])
            i +=1
        else:
            tmp.append(A[j])
            j +=1

    while(i<=q):
        tmp.append(A[i])
        i+=1

    while(j<=r):
        tmp.append(A[j])
        j+=1

    for t in range(len(tmp)):
        A[p+t] = tmp[t]
        cnt+=1
        if cnt == k:
            result = tmp[t]
        
merge_sort(A,0,n-1)
print(result)
