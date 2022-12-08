from toolbox.data_reader import read_file
from toolbox.timer import Timer
from toolbox.pretty_printer import print_solution_1, print_solution_2
import sys

data = read_file('day7.txt')
# print(data)

# start with / is 0
# ls or cd <some dir>
# ls > num <file name> or dir <letter>

# what to do with command?
# ls > process file sizes
# cd > go into dir or out

def process_directory_files(file_line_list):
    """reads files in directory"""    
    if(file_line_list[0].isnumeric()):
        return int(file_line_list[0])
    else:
        return -1

def get_dir_key(current_dir):
    return "-".join(current_dir)

def update_parent_size(dir_size, stack, current_dir): 
    temp_dir_size = dir_size.copy()
    temp_stack = [x for x in stack]
    temp_cur_dir = [x for x in current_dir]

    cur_dir_key, _ = temp_stack.pop()
    temp_cur_dir.pop() #remove cur_directory
    parent_dir_key = get_dir_key(temp_cur_dir)
    temp_dir_size[parent_dir_key] += temp_dir_size[cur_dir_key]

    if(parent_dir_key == "/"):
        return temp_dir_size
    else:
        return update_parent_size(temp_dir_size, temp_stack, temp_cur_dir)
    

t = Timer()

# stack to store current dir (<dirname>, <size>)
stack = []
# dictionary storing directory sizes
directory_size = {}
# an ordered array of traverse directories
current_directory = []


t.start()

for line in data:
    line_list = line.split(" ")

    if(line_list[0] == "$"): # command
        cmd = line_list[1]

        if(cmd == "cd"):
            cmd_input = line_list[2]
            if(cmd_input == ".."): # move out of directory
                # adjust size of parent directory
                current_directory.pop()
                prev_directory, _ = stack.pop()

                dir_key = get_dir_key(current_directory)
                directory_size[dir_key] += directory_size[prev_directory]

            else: # move into directory
                current_directory.append(cmd_input)
                
                dir_key = get_dir_key(current_directory)

                stack.append((dir_key, 0))
                directory_size[dir_key] = 0

        else: # ls, move to the next line
            continue
    
    else: # file
        res = process_directory_files(line_list)
        dir_key = get_dir_key(current_directory)
        
        if(res > 0): # is file size
            directory_size[dir_key] += res

directory_size = update_parent_size(directory_size, stack, current_directory)

answer = 0

for size in directory_size.values():
    if(size < 100000):
        answer += size
        
t.stop()

print_solution_1(answer, t.last_elapsed_time())


# Part 2
t = Timer()

answer = 0
tota_disk_space = 70000000
unused_space_needed = 30000000

t.start()

current_unused_space = tota_disk_space - directory_size["/"]

inv_directory_size = {v: k for k, v in sorted(directory_size.items(), key=lambda item: item[1], reverse=True)}

needed_space = unused_space_needed - current_unused_space
smallest_directory_size_needed = sys.maxsize

for (v, k) in inv_directory_size.items():
    if(v >= needed_space and v < smallest_directory_size_needed):
        smallest_directory_size_needed = v    
    elif(v < needed_space):
        break
    
answer = smallest_directory_size_needed

t.stop()

print_solution_2(answer, t.last_elapsed_time())