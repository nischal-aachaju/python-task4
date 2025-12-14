
num=1634
p=0

str_num=str(num)
for i in str_num:
    p=int(i)**3+p

if num==p:
    print(f"{num} is armstrong")

else:
    print(f"{num} is not armstrong")
