from collections import defaultdict 
import sys 
def lss(a,n): 
	mp = defaultdict(lambda:0) 
	dp = [0 for i in range(n)] 
	maximum = -sys.maxsize 
	for i in range(n): 
		if a[i] - 1 in mp: 
			lastIndex = mp[a[i] - 1] - 1
			dp[i] = 1 + dp[lastIndex] 
		else: 
			dp[i] = 1
		mp[a[i]] = i + 1
		maximum = max(maximum, dp[i]) 
	return maximum 

n =int(input()) 
a =list(map(int,input().split()))
print(lss(a, n)) 
