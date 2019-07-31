m1,k1=map(int,input().split())
h=(input().split())[0:m1]
i=0
while i<k1:
  m1,n=map(int,input().split())
  i+=1
  print(min(h[m1-1:n]))
