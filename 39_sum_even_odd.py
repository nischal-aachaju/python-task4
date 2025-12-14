
#39. Write a for loop to find the sum of even and
#odd numbers separately in a range from 1 to 100.
sum_even=0
sum_odd=0
for i in range(1,101):
    if i %2==0:
        sum_even+=i


    else:
        sum_odd+=i

print(sum_odd,"is sum of odd number from 1 to 100")
print(sum_even,"is sum of even number from 1 to 100")