def findMaxNum(arr, n): 
      

    hash = [0] * 10
      

    for i in range(n): 
        hash[arr[i]] += 1
      
 
    for i in range(9, -1, -1): 
          
    
        for j in range(hash[i]): 
            print(i, end = "") 
  

if __name__ == "__main__":
        n=int(input())
t=list(map(int,input().strip().split()))[:n]    
    
findMaxNum(t,n) 

 
