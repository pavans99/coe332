nums = [42,56,33,20,9,48,37,16,25,43]
list2=[]
for i in range(len(nums)):
    if(nums[i]%2==0):
        list2.append('even')
    else:
        list2.append('odd')
for i in range(len(nums)):
    print(nums[i],list2[i])
