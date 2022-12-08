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
test = "cd .."

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

    print("======== input ==========")
    print("temp_stack: ", temp_stack)
    print("temp_cur_dir: ", temp_cur_dir)
    print("temp_dir_size: ", temp_dir_size)
    print("")
    print("======== process ==========")
    cur_dir_key, _ = temp_stack.pop()
    temp_cur_dir.pop() #remove cur_directory
    parent_dir_key = get_dir_key(temp_cur_dir)
    temp_dir_size[parent_dir_key] += temp_dir_size[cur_dir_key]
    print("cur_dir_key: ", cur_dir_key)
    print("temp_cur_dir: ", temp_cur_dir)
    print("parent_dir_key: ", parent_dir_key)
    print("temp_dir_size[parent_dir_key]: ", temp_dir_size[parent_dir_key])
    
    print("")

    if(parent_dir_key == "/"):
        return temp_dir_size
    else:
        return update_parent_size(temp_dir_size, temp_stack, temp_cur_dir)
    

t = Timer()

# stack to store current dir (<dirname>, <size>)
stack = []

# dictionary of directories
# e.g. {"a": ["x", "y"]}
directory_parent = {}

directory_size = {}

current_directory = []

test = ["a"]
print("-".join(test))

# current_dir_size = 0

t.start()

for line in data:
    line_list = line.split(" ")
    # print("line: ", line)
    # print("sizes: ", directory_size)
    if(line_list[0] == "$"): # command
        cmd = line_list[1]
        # print("command: ", cmd)
        if(cmd == "cd"):
            cmd_input = line_list[2]
            if(cmd_input == ".."): # move out of directory
                # adjust size of parent directory
                # print("backing up..")
                prev_directory, _ = stack.pop()
                current_directory.pop()

                dir_key = get_dir_key(current_directory)

                # adjust current directory
                # print("adjusting current directory: ", current_directory, " size from to ", directory_size[dir_key], " + ", directory_size[prev_directory])

                directory_size[dir_key] += directory_size[prev_directory]
                # print("new size: ", directory_size[f"{current_directory}"])


                # print("moving out of directory: ", prev_directory, " and back to ", current_directory)

            else: # move into directory
                print("moving into directory: ", cmd_input)
                current_directory.append(cmd_input)
                
                dir_key = get_dir_key(current_directory)

                stack.append((dir_key, 0))
                directory_size[dir_key] = 0

        else: # ls, move to the next line
            continue
    
    else: # file
        res = process_directory_files(line_list)
        # print("res: ", res)
        if(res > 0): # is file size
            # print("current_dir: ", current_directory)
            # print("sizes: ", directory_size)
            dir_key = get_dir_key(current_directory)

            directory_size[dir_key] += res
            # print("key", dir_key)
            # print("size for: ",current_directory, " has been adjust to: ",directory_size[dir_key])

        else: # is directory
            dir_key = get_dir_key(current_directory)
            directory_parent[line_list[1]] = dir_key

# print("updaaaate.....", update_parent_size(directory_size, stack, current_directory))
directory_size = update_parent_size(directory_size, stack, current_directory)
print("sizes: ", directory_size)

answer = 0

for size in directory_size.values():
    if(size < 100000):
        answer += size
        
print(answer)

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
print("inv_directory_size: ", inv_directory_size)

needed_space = unused_space_needed - current_unused_space
smallest_directory_size_needed = sys.maxsize
print("smallest_directory_size_needed: ", smallest_directory_size_needed)

for (v, k) in inv_directory_size.items():
    if(v >= needed_space and v < smallest_directory_size_needed):
        smallest_directory_size_needed = v        
        print("found a smaller one! ", v)

    elif(v < needed_space):
        print("stop!")
        break
    
answer = smallest_directory_size_needed

t.stop()

print_solution_2(answer, t.last_elapsed_time())