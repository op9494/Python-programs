def iPower(x, y):
   while (x%y == 0):
       x = x / y
   if x == 1:
       print("yes")
   else:
        print("no")
        
l,n=map(int,input().split())        
iPower(l,n)
