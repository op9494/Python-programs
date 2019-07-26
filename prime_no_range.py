l,u=map(int,input().split()) 
ad=0   
for n in range(l,u+1):
   if n> 1:  
        for i in range(2,n):  
            if (n% i) == 0:  
                 break  
        else:  
            ad=ad+1    
    
print(ad)
