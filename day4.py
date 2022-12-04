from toolbox.data_reader import read_file

data = read_file('day4.txt')
# print(data)

# contained means 

# section y is contained in x if
# x1 <= y1 and x2 => y2 OR
# where x1 is smallest number and x2 largest number

# section x is contains in y if
# y1 <= x1 and y2 => x2

# section is e.g. "2-8"
def is_section_x_contained_in_section_y(section_x, section_y):
    sec_x = section_x.split('-')
    sec_y = section_y.split('-')

    x1 = int(sec_x[0])
    x2 = int(sec_x[1])
    y1 = int(sec_y[0])
    y2 = int(sec_y[1])

    if(y1 <= x1 and y2 >= x2):
        return True
    
    return False

sum_of_fully_contained_sections = 0

for pairs in data:
    list_of_pairs = pairs.split(',')

    section_x = list_of_pairs[0]
    section_y = list_of_pairs[1]
    
    if(is_section_x_contained_in_section_y(section_x, section_y) or is_section_x_contained_in_section_y(section_y, section_x)):
        sum_of_fully_contained_sections += 1

# print(sum_of_fully_contained_sections)


# Part 2


def is_section_x_overlapping_with_section_y(section_x, section_y):
    sec_x = section_x.split('-')
    sec_y = section_y.split('-')

    x1 = int(sec_x[0])
    x2 = int(sec_x[1])
    y1 = int(sec_y[0])
    y2 = int(sec_y[1])

    if((x1 >= y1 and x1 <= y2) or ((x2 >= y1 and x2 <= y2))):
        return True
    
    return False


sum_of_fully_contained_sections = 0

for pairs in data:
    list_of_pairs = pairs.split(',')

    section_x = list_of_pairs[0]
    section_y = list_of_pairs[1]

    if(is_section_x_overlapping_with_section_y(section_x, section_y) or is_section_x_overlapping_with_section_y(section_y, section_x)):
        sum_of_fully_contained_sections += 1

print(sum_of_fully_contained_sections)