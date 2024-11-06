import math 
a,b = input().split()
a = int(a)
b = int(b)
nums = int(a + b) 
root = int(math.isqrt(nums)) 
if (root * root) == nums: 
    print("Yes") 
else: 
    print("No")
