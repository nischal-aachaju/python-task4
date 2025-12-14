
#33. Write a for loop which appends the type of each element in the first list to the second list.

list=[1,2,3,4,"a","b"]
list2=[]
for i in list:
    if type(i)==int:
        
        list2.append("int")
    

    else:
       
        list2.append("Str")

print(list)
print(list2)