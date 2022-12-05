from toolbox.data_reader import read_file_no_strip
from toolbox.timer import Timer
from toolbox.pretty_printer import print_solution_1, print_solution_2
import numpy as np

demo = False
data = []
if(demo):
    data = read_file_no_strip('day5_demo.txt')
else:
    data = read_file_no_strip('day5.txt')
# print(data)


# last row is always filled (thank god), can extract number of columns from there
# every column is a multiple of three omg

# check if column numbers
# def check_if_column_numbers_line:
def extract_crate(crate):
    return crate[1]


def parse_crates_into_stacks(crates_list, number_of_columns):
    stacks = [[] for x in range(number_of_columns)]

    for crates in crates_list:
        column = 0
        count = 0
        for crate in crates:           
            if(crate == ""):
                count+=1
                # print(count)
                if(count == 4):
                    column+=1
                    count=0
            elif(crate[0] == "["):
                c = extract_crate(crate)
                # print("column", column)
                stacks[column].append(c)
                column+=1
    return stacks


def process_rearrangement(procedure, stacks):
    number_of_crates = int(procedure[1])
    from_stack = int(procedure[3]) - 1
    to_stack = int(procedure[5]) - 1
    # s = stacks
    for x in range(number_of_crates):
        crate = stacks[from_stack].pop()
        stacks[from_stack] = stacks[from_stack]
        # print("pop! - ", crate)
        # print(f"stack: {from_stack} ", stacks[from_stack])
        stacks[to_stack].append(crate)
        # print(f"stack: {to_stack} ", stacks[to_stack])

    return stacks

# t = Timer()
if(demo):
    crate_lines = 3
    columns = 3
else:
    crate_lines = 8
    columns = 9

x = 0
moves_lines = crate_lines+2
crates_list = []
stacks = []
for line in data:
    
    if(x < crate_lines): # dont hardcode..
        # print(line.split(" "))
        crates_list.append(line.split(" "))
    elif(x == crate_lines):
        # print(crates_list)
        stacks = parse_crates_into_stacks(crates_list[::-1], columns)        
    elif(x >= moves_lines):
        procedure = line.strip().split(" ")
        # print(procedure)
        # print(stacks)
        stacks = process_rearrangement(procedure, stacks)

    x+=1

# for x in range(columns):
#     print(stacks[x].pop())




# Part 2

def process_rearrangement_2(procedure, stacks):
    number_of_crates = int(procedure[1])
    from_stack = int(procedure[3]) - 1
    to_stack = int(procedure[5]) - 1

    index = len(stacks[from_stack]) - number_of_crates
    stacks[to_stack] = stacks[to_stack] + stacks[from_stack][index:]
    stacks[from_stack] = stacks[from_stack][:index]

    print(f"stack: {from_stack} ", stacks[from_stack])
    print(f"stack: {to_stack} ", stacks[to_stack])

    return stacks

x=0
moves_lines = crate_lines+2
crates_list = []
stacks = []
for line in data:
    
    if(x < crate_lines): # dont hardcode..
        # print(line.split(" "))
        crates_list.append(line.split(" "))
    elif(x == crate_lines):
        # print(crates_list)
        stacks = parse_crates_into_stacks(crates_list[::-1], columns)        
    elif(x >= moves_lines):
        procedure = line.strip().split(" ")
        print(procedure)
        # print(stacks)
        stacks = process_rearrangement_2(procedure, stacks)

    x+=1


for x in range(columns):
    print(stacks[x].pop())

