
list=[1,2,3,4,5]
print(list,"is list")
even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)

    else:
        odd.append(i)

print(even,"is even")
print(odd,"is odd")