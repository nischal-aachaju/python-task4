#15. Python program that accepts a string and calculate the number of digits and letters

# val=input("Enter anything ")

# list_val=list(val)
# print(list_val)
# print(len(list_val))

a=input("Enter anything ")


letter=0
number=0
for i in a:
    if i.isdigit():
        number+=1
    else:
        letter+=1

print("There is ",letter,"letter")
print("there is ",number,"number")