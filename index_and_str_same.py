n=int(input())
test_list =list(map(int,input().strip().split()))[:n] 
c=0
for i in range(len(test_list)): 
  if(i==test_list[i]):
      print(test_list[i],end=" ") 
  else:
      c=c+1
if c==(len(test_list)):
  print('-1') 
