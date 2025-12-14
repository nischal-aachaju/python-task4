
# 9 num question
print("\n--------9 number question---------")
lst=[1,2,3,4]

for i in lst:
    if i==1 or i==4:
        print(i)

# 10 num question
lst=[1,2,3,4]
print("\n-----------10 number question---------")
print("printing 1 2 and 4 only")
for i in lst:
    if i==1 or i==2 or i==4:
        print(i)

#11  Given list is [1,2,3,4] but expected output is [1,"a",2,4] 
print("\n----------11 number question---------")
list=[1,2,3,4]
list1=[]
for i in list:
    
    
    if i==2:
        list1.append("a")
        list1.append(i)
    elif i==3:
        pass
    else:
        list1.append(i)

print(list1)



