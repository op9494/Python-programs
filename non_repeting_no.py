def firstNonRepeating(arr, n): 
    for i in range(n): 
        j = 0
        while(j < n): 
            if (i != j and arr[i] == arr[j]): 
                break
            j += 1
        if (j == n): 
            return arr[i] 
    return -1
n=int(input())
arr=list(map(int,input().strip().split()))[:n]
print(firstNonRepeating(arr, n)) 
