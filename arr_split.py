def fa(arr, n): 

	found = False
	lsum = 0
	for i in range(n - 1): 
	
		lsum += arr[i] 
		rsum = 0
		for j in range(i + 1, n): 
			rsum += arr[j] 
		if (lsum * (n - i - 1) == rsum * (i + 1)): 
			print("yes") 
			found = True


	if (found == False): 
		print("no") 


if __name__ == "__main__":
  n= int(input())
  arr=[]
  arr=list(map(int,input().strip().split()))[:n]
  fa(arr,n) 


