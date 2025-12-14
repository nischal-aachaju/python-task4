#28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
lst=["ram","shyam","hari",1,2,3]
for i in lst:
    if type(i)==str:
        print(f"hello!, {i}")