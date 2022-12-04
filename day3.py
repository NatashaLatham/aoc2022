from toolbox.data_reader import read_file

data = read_file('day3.txt')
# print(data)

# a - z => 97 - 122
# Suppose to be 1 - 26, dus minus 98

# A - Z => 65 - 90
# Suppose to be 27 - 52, dus minus 38


# print(ord('a'), ord('b'), ord('z'), ord('A'), ord('B'), ord('Z'))

def charToPriority(char):
    num = ord(char)
    if(num >= 97 and num <= 122):
        return num - 96
    elif(num >= 65 and num <= 90):
        return num - 38
    else:
        raise Exception("Foute boel")

def findTypeInItemList(list):
    halfway = int(len(list)/2)
    compartment1 = list[halfway:]
    compartment2 = list[:halfway]

    return set([x1 for x1 in compartment1 if x1 in compartment2]).pop()


sum_of_priorities = 0

for items_list in data:
    type = findTypeInItemList(items_list)
    priority = charToPriority(type)
    sum_of_priorities = sum_of_priorities + priority

print(sum_of_priorities)



# part 2

def findTypeInItemLists(list1, list2, list3):    
    return set([x1 for x1 in list1 
                   for x2 in list2 
                   for x3 in list3 
                   if (ord(x1) == ord(x2) and ord(x1) == ord(x3))]).pop()

sum_of_priorities = 0
counter = 0
lists_of_items = ["" for x in range(3)]

for items_list in data:
    lists_of_items[counter] = items_list
    
    if(counter == 2):
        type = findTypeInItemLists(lists_of_items[0],lists_of_items[1],lists_of_items[2])
        priority = charToPriority(type)
        sum_of_priorities = sum_of_priorities + priority
        counter = -1

    counter = counter + 1

print(sum_of_priorities)