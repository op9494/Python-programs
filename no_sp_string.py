s=input()
c=0
for a in s: 
   if(a.isalpha()):
       x=0
   elif(a.isdigit()):
       l=0
   elif a==" ":
       l=0    
   else:
        c = c + 1
print(c) 
