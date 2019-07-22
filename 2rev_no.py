N=int(input())    
Rev=0    
while(N>0):    
    Rem=N%10    
    Rev=(Rev*10)+Rem    
    N=N//10    
print(Rev)
