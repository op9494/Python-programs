s=input()
c=0
l=len(s)
for a in s: 
    if (a.isspace()) == True: 
        c+=1
print(l-c) 
