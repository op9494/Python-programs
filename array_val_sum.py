n,k=map(int,input().split())
c=k
s=0
arr=[]
arr =list(map(int,input().strip().split()))[:n]
for i in range(0,c):
  s=s+arr[i]
print(s)
