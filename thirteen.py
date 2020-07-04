# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22John,54 Love Ave,21
import csv

def csv_file(filename, data):
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows([("Name", "Address", "Age")])
        writer.writerows(data)


file_name = "file.txt"
data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
csv_file(file_name, data)



# output
# Name,Address,Age
# George,4312 Abbey Road,22
# John,54 Love Ave,21
