def compare(a, b):
    c=0 
    for x,y in zip(a,b):
        if(x!=y):
          c=c+1
    if(c==1):   
        print("yes")
    else:
        print("no")




l,u=map(str,input().split())
compare(l,u)
