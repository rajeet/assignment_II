# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.




list_item = [1,2,3,4,5,6,7,8,9]
to_find = 20

def binary_search_function(list_item, to_find):
    if to_find in list_item:
        return list_item.index(to_find)
    return -1


index_is = binary_search_function(list_item, to_find)
if index_is != -1:
    print(f"The index of number {to_find} is {index_is}")
print(index_is)


    