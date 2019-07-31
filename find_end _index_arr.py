n,kl=map(int,input().split())
m=list(map(int,input().split()))
q=[]
for i in range(0,kl):
    d1 = []
    d1=list(map(int,input().split()))
    s = m[d1[0]-1]
    for j in range(min(d1),max(d1)):
        s=s^m[j]
    q.append(s)
for i in range(0,len(q)):
    print(q[i])
