n=int(input())
test_list =list(map(int,input().strip().split()))[:n] 
for i in range(len(test_list)): 
    print (test_list[i],end = " ") 
    print (i) 
    
