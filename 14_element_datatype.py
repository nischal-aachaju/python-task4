
#14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
list=[1,2,3,4,"a","b"]
list2=[]
for i in list:
    if type(i)==int:
        
        list2.append("int")
    

    else:
       
        list2.append("Str")

print(list)
print(list2)