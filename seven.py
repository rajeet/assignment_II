# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.


tupname1 = ('Rajeet', 'Mangrati', 22)
tupname2 = ('Shyam', 'KC', 20)
tupname3 = ('Hari', 'Lama', None)
tupname4 = ('Bishal', 'Tamang', 26)

tup_list = []
total_age = 0
num = 0
tup_list.append((tupname1, tupname2, tupname3, tupname4))
for i in tup_list[0]:
    if type(i[2]) == int:
        total_age += i[2]
        num += 1
average_age = total_age/num
for i in tup_list[0]:
    if type(i[2]) == int:
        if(i[2]) < average_age:
            print("Name: {} {}".format(i[0],i[1]))
            print("=============>Below the average age")
        else:
            print("Name: {} {}".format(i[0],i[1]))
            print("=============>above the average age")
            