# introduction to strings in python
name = "Irfan"
d_name = 'Irfan'

# strings are immutable in python
'''name[0] = "i"''' # you will get error
print(name)
# strings are sequences of characters
print(name[0],name[2]) # prints first character of the string
# strings can be enclosed in single quotes or double quotes
name = "Irfan"
d_name = 'Irfan'
# strings can be concatenated using the + operator
print(name+" "+d_name)
# strings can be repeated using the * operator
repeated_string = name*3
print(repeated_string)
