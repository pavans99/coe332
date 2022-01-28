nums = []
for i in range(3,101):
    nums.append(i)
for i in range(len(nums)):
    k=2
    j=0
    while(k<nums[i]/2+1):
        if(nums[i]%k==0):
            j=1
            break
        k=k+1
    if(j==0):
        print(nums[i])
