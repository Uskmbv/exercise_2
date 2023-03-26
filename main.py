#1

numbers = [34, 6, 5, 4, 7, 5, 5, 9]
integer = 5

def count_integer(numbers, integer):
    count = 0
    for i in numbers:
        if i == integer:
            count += 1
    if count == 0:
        return 42
    else:
        return count
print(count_integer(numbers, integer))

#2

numbers = [2, 4, 6, 8, 10]
integer = 4

def list_func(numbers, integer):
    original_list = numbers.copy()

    if integer in numbers:
        index = numbers.index(integer)
        numbers[index] = 6
    else:
        return []

    numbers.reverse()
    print(numbers)

    return original_list

result = list_func(numbers, integer)

print(result)

#3

list1 = ["apple", 13, 7.5, "march", 23, 65, 11]
list2 = ["march", 78.1, 0.02, 13, 99, 4.34, "football"]

def compare_lists(list1, list2):
    common_elements = []

    for element in list1:

        if element in list2:

            common_elements.append(element)

    return common_elements
result = compare_lists(list1, list2)

print(result)

#4

lst = [1, 2, 3, 4, 5, 6, 7, 7, 8]

def remove_duplicates(lst):
    # Convert the list to a set to remove duplicates
    unique_lst = set(lst)

    # Convert the set back to a list
    unique_lst = list(unique_lst)

    # Return the list without duplicates
    return unique_lst
result = remove_duplicates(lst)

print(result)

#5

def dict_func(dictionary):

    if "Type" not in dictionary:
        dictionary["Type"] = "unknown type"
    if "Brand" not in dictionary:
        dictionary["Brand"] = "unknown brand"
    if "Price" not in dictionary:
        dictionary["Price"] = "unknown price"

    print(f"You have a {dictionary['Type']} from {dictionary['Brand']} that costs {dictionary['Price']}.")

    dictionary.setdefault('OS', 'Linux')

    print(dictionary)

    return dictionary

my_dict = {"Type": "phone", "Brand": "Samsung", "Price": "$999"}
dict_func(my_dict)
