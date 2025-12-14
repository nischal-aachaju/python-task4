#24. given list is [1,2,3,4] but expected output is [1,8,27,64]

lst=[1,2,3,4]

temp=[]

for i in lst:
    
    temp.append(i**3)
print(temp)