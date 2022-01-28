list1 = [1,2,3,4,5,6,7,8,9,10]
list2=[]
list3=[]
for i in range(len(list1)):
        list2.append(list1[i]**2)
        list3.append(list1[i]**3)
for i in range(len(list1)):
    print(list1[i],' ', list2[i],' ',list3[i])

