def permute(d,i,l):
    if i==l:
      print(''.join(d))
    else:
      for j in range(i,l):
        d[i],d[j]=d[j],d[i]
        permute(d,i+1,l)
        d[i],d[j]=d[j],d[i]
string=input()
n=len(string)
data=list(string)
permute(data,0,n)
