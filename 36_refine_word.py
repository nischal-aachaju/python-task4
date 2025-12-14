#36. removal bad characters from the 
# given string. Given 
# bad_chars = [';', ':', '!', "*"], 
# string = "py;th* o:n ! ;py * t*h:o !n".  
# Expected output = pythonpython
str="py;th* o:n ! ;py * t*h:o !n"

bad_chars = [';', ':', '!', "*"," "]
output=""
for i in str:
    if i in bad_chars:
        continue

    output+=i

print(output)
