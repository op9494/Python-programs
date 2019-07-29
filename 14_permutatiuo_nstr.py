def permute(data,i,length):
    if i==length:
      print(''.join(data))
    else:
      for j in range(i,length):
        data[i],data[j]=data[j],data[i]
        permute(data,i+1,length)
        data[i],data[j]=data[j],data[i]
string=input()
n=len(string)
data=list(string)
permute(data,0,n)
