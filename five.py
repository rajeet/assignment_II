# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.


tupname1 = ('Rajeet', 'Mangrati', 22)
tupname2 = ('Shyam', 'KC', 20)
tupname3 = ('Hari', 'Lama', 25)
tupname4 = ('Bishal', 'Tamang', 26)


people = []
people.extend((tupname1, tupname2, tupname3, tupname4))

people.sort(key = lambda x: x[2])
print(people)

# sorted using age
# [('Shyam', 'KC', 20), ('Rajeet', 'Mangrati', 22), ('Hari', 'Lama', 25), ('Bishal', 'Tamang', 26)]
