#40. program to check given number 
# is palindrome or not

num=int(input("enter number"))
str_num=str(num)
rev_num=""
for i in str_num[::-1]:
    
    rev_num+=i


if (rev_num)==num:
    print(f"{num} is palindrome")

else :
    print(f"{num} is not palindrome")