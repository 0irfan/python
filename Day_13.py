# string methoods
a = " this is test"
print(a.upper()) # convert to upper case
print(a.lower()) # convert to lower case
print(a.capitalize()) # capitalize the first letter
print(a.title()) # capitalize the first letter of each word
# check if the string ends with "test"
print(a.endswith("test"))
# check if the string starts with "this"
print(a.startswith("this"))
# check if the string contains "is"
print(a.find("is"))
# replace "is" with "was"
print(a.replace("is", "was"))
# split the string into a list of words
print(a.split()) # split the string into a list of words
# check if the string is alphanumeric
print(a.isalnum())
# check if the string is alphanumeric and contains only spaces
print(a.isspace())
# check if the string is a digit
print(a.isdigit())

