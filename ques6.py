input_str = input('enter the string')
newString = ""
valid = "abcdefghijklmnopqrstuvwxyz"   
for char in input_str:
    if char in valid:
        newString += char     
print (newString)
