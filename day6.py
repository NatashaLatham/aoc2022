from toolbox.data_reader import read_file
from toolbox.timer import Timer
from toolbox.pretty_printer import print_solution_1, print_solution_2

data = read_file('day6.txt')
# print(data)

# testList = [*"blah"] #convert string into array of chars
# print([*"blah"]) 
# print(len(set(testList)) == len(testList)) # check if all values are unique

def characters_are_unique(characters):
    return len(set(characters)) == len(characters)


def find_first_time_marker_appears(input, number_of_unique_characters):
    marker = 0
    for x in range(number_of_unique_characters, len(input)):
        if(characters_are_unique(input[x-number_of_unique_characters:x])):
            # print("marker: ", x, " is it!")
            marker = x
            break
    return marker


t = Timer()

marker = 0
t.start()

for input in data:
    marker = find_first_time_marker_appears(input, number_of_unique_characters=4)

t.stop()

print_solution_1(marker, t.last_elapsed_time())


# Part 2
t = Timer()

marker = 0
t.start()

for input in data:
    marker = find_first_time_marker_appears(input, number_of_unique_characters=14)

t.stop()

print_solution_2(marker, t.last_elapsed_time())