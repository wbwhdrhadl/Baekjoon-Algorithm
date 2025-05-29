a,b,v = map(int,input().split())

if(v-a) % (a-b) == 0:
    days = (v-a) // (a-b) 
else:
    days = (v-a) // (a-b) + 1
    
print(days + 1)
