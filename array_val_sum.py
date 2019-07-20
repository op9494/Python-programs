n,k=map(int,input().split())
c=k
N=[]
s=0
for i in range(1,n+1):
        N.append(i)
for i in range(0,c):
  s=s+N[i]
print(s)
