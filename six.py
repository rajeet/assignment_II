# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.


list_name = ['Ram', 'Hari', 'Shyam', 'Gopal', 'John' , 'Rajeet', 'Jiwan']
print(list_name)



def search_john(name):
    x = 0
    for i in list_name:
        if i == name:
            x = 1
            break
    else:
        x = 0
    return x


to_find = search_john("John")
print(to_find)
if to_find == 1:
    print("Result Found")
else:
    print("Result Not Found")

    

        
# ['Ram', 'Hari', 'Shyam', 'Gopal', 'John', 'Rajeet', 'Jiwan']
# 1
# Result Found
