# Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]




import csv

def read_csv(filename):
    my_list = []
    print(filename)
    with open(filename, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            my_list.append(dict(row))
    print(my_list)




filename = "file.txt"
read_csv(filename)

