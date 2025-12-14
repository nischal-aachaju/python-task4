#42. Write a for loop that removes
# all vowels (a, e, i, o, u) from a string.

list=("a","e","i","o","u")
str="Nischal"
after_vowel_remove=""
for i in str:
    if i in list:
        continue
    after_vowel_remove+=i


print(after_vowel_remove)
