n,k=map(int,input().split())
nos=list(map(int,input().split()))[:n]
c=0
for i in range(0,len(nos)-1):
    for s in range(i+1,len(nos)-1):
        if(nos[i]+nos[s]==k):
            c+=1
if (c==1):
    print("yes")
else:
    print("no")
