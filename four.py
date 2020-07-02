# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?



list_names = ["Ram", "shyam", "hari", "krishna"]
print(list_names)
print(id(list_names))
list_names.append("gopal")
print(list_names)
print(id(list_names))

list_names.sort()
print(list_names)

# output
# ['Ram', 'shyam', 'hari', 'krishna']
# 140122578560256
# ['Ram', 'shyam', 'hari', 'krishna', 'gopal']
# 140122578560256
# ['Ram', 'gopal', 'hari', 'krishna', 'shyam']