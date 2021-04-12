def rev(str):
    if len(str) == 0:
        return str
    else:
        return rev(str[1:]) + str[0]


mystr = input('enter the string')

print("The Given String  is: ", mystr)

print("Reversed String is: ", rev(mystr))
