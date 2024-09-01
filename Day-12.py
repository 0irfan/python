# Introduction to String slicing.
fruits = 'orange'
len(fruits)
print(fruits[-4:len(fruits)])
if fruits[-4:len(fruits)] == 'ange':
    print("True")
else:
    print("False")