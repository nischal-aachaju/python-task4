#21. Python program to calculate the sum of all the odd numbers within the given range.
var=int(input("Enter number : "))
sum_odd=0
for i in range(1,var+1):
    if i%2!=0:
        sum_odd+=i

print(sum_odd ,"is sum of odd")

#22. Python program to calculate the sum of all the even numbers within the given range

var=int(input("Enter number : "))
sum_even=0
for i in range(1,var+1):
    if i%2==0:
        sum_even+=i

print(sum_even,"is sum of even ")
