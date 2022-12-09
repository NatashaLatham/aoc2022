from toolbox.data_reader import read_file
from toolbox.timer import Timer
from toolbox.pretty_printer import print_solution_1, print_solution_2, print_matrix

data = read_file('day8_demo.txt')
# print(data)



t = Timer()

answer = 0
grid = []
is_visible = []

t.start()
row = 0

for input in data:
    tree_line = [int(x) for x in input]
    is_vis_line = [True if (x == 0 or x == len(input)-1) else False for x in range(len(input))]

    if(row == 0 or row == len(data)-1):
        is_vis_line = [True for x in input]
    
    row+=1
    grid.append(tree_line)
    is_visible.append(is_vis_line)

# print(grid)
# print(is_visible)
# grid(x, y)
# top = x-1
# bottom = x+1
# left = y-1
# right = y+1

grid_row_len = len(grid)
grid_col_len = len(grid[0])

# outer = (grid_x * 2) + ((grid_y-2)*2)
# outer_trees = grid_row_len*2 + (grid_col_len-2)*2
# print("outer: ", outer_trees)


def is_vis_from_side(cur_tree_x, cur_tree_y, offset_x, offset_y):
    curr_tree = grid[cur_tree_x][cur_tree_y]
    side_tree = grid[cur_tree_x+offset_x][cur_tree_y+offset_y]
    side_tree_is_vis = is_visible[cur_tree_x+offset_x][cur_tree_y+offset_y]
    
    return (curr_tree, side_tree, side_tree_is_vis)

def is_vis_from_top(cur_tree_x, cur_tree_y, offset_x, offset_y):
    curr_tree, side_tree, side_tree_is_vis = is_vis_from_side(cur_tree_x, cur_tree_y, offset_x, offset_y)
    
    if(curr_tree > side_tree and side_tree_is_vis):
        return True
    elif(curr_tree > side_tree and not side_tree_is_vis):
        if(offset_x > 0):
            return is_vis_from_left(cur_tree_x, cur_tree_y, offset_x-1, offset_y)
    else:
        return False

def is_vis_from_bottom(cur_tree_x, cur_tree_y, offset_x, offset_y):
    curr_tree, side_tree, side_tree_is_vis = is_vis_from_side(cur_tree_x, cur_tree_y, offset_x, offset_y)
    
    if(curr_tree > side_tree and side_tree_is_vis):
        return True
    elif(curr_tree > side_tree and not side_tree_is_vis):
        if(offset_x < grid_row_len - 1):
            return is_vis_from_left(cur_tree_x, cur_tree_y, offset_x+1, offset_y)
    else:
        return False

def is_vis_from_left(cur_tree_x, cur_tree_y, offset_x, offset_y):
    curr_tree, side_tree, side_tree_is_vis = is_vis_from_side(cur_tree_x, cur_tree_y, offset_x, offset_y)
    
    if(curr_tree > side_tree and side_tree_is_vis):
        return True
    elif(curr_tree > side_tree and not side_tree_is_vis):
        if(offset_y > 0):
            return is_vis_from_left(cur_tree_x, cur_tree_y, offset_x, offset_y-1)
    else:
        return False

def is_vis_from_right(cur_tree_x, cur_tree_y, offset_x, offset_y):
    curr_tree, side_tree, side_tree_is_vis = is_vis_from_side(cur_tree_x, cur_tree_y, offset_x, offset_y)
   
    # print(f"right ({cur_tree_x},{cur_tree_y}) - offset_y: {offset_y}")
    
    if(curr_tree > side_tree and side_tree_is_vis):
        return True
    elif(curr_tree > side_tree and not side_tree_is_vis):
        if(offset_y < grid_col_len - 1):
            return is_vis_from_right(cur_tree_x, cur_tree_y, offset_x, offset_y+1)
    else:
        return False



    # return is_vis_from_side(cur_tree_x, cur_tree_y, 0, 1)


# check top and bottom
def scan_top_and_bottom():
    for y in range(1, grid_row_len-1):
        for x in range(1, grid_col_len-1):
            if(is_vis_from_top(x, y, -1, 0)):
            # if(is_vis_from_top(x, y, -1, 0) or is_vis_from_left(y, x, 0, -1)):
            # if(is_vis_from_left(y, x, 0, -1)):
                is_visible[x][y] = True
            
            print(f"top_grid({x},{y}): ", grid[x][y])
            # print(f"left_grid({y},{x}): ", grid[y][x])
            # print(f"bottom_grid({x_2},{y}): ", grid[x_2][y])
            print("=====")

            # x_2 = grid_row_len-x-1
            # if(is_vis_from_bottom(x_2, y, 1, 0)):            
            #     is_visible[x_2][y] = True

def scan_all_1():
    for y in range(1, grid_row_len-1):
        for x in range(1, grid_col_len-1):
            # if(is_vis_from_top(x, y, -1, 0)):
            # if(is_vis_from_top(x, y, -1, 0) or is_vis_from_left(x, y, 0, -1)):
            # # if(is_vis_from_left(y, x, 0, -1)):
            #     is_visible[x][y] = True
            
            # if(is_vis_from_top(y, x, -1, 0) or is_vis_from_left(y, x, 0, -1)):
            #     is_visible[y][x] = True
            
            # if(is_vis_from_left(y, x, 0, -1)):
            # print(f"top_grid({x},{y}): ", grid[x][y])
            # print(f"left_grid({y},{x}): ", grid[y][x])
            # print(f"bottom_grid({x_2},{y}): ", grid[x_2][y])
            # print("=====")

            x_2 = grid_row_len-x-1
            y_2 = grid_col_len-y-1

            if(is_vis_from_bottom(x_2, y, 1, 0) or is_vis_from_right(x_2, y, 0, 1)):
                is_visible[x_2][y] = True
            
            if(is_vis_from_bottom(x, y_2, 1, 0) or is_vis_from_right(x, y_2, 0, 1)):
                is_visible[x][y_2] = True
            

def scan_left_and_right():
    for x in range(1, grid_row_len-1):
        for y in range(1, grid_col_len-1):
            # if(is_vis_from_left(x, y, 0, -1)):
            #     is_visible[x][y] = True
            
            y_2 = grid_col_len-y-1
            # print(f"left_grid({x},{y}): ", grid[x][y])
            print(f"right_grid({x},{y_2}): ", grid[x][y_2])
            print("=====")

            if(is_vis_from_right(x, y_2, 0, 1)):            
                is_visible[x][y_2] = True


# scan_top_and_bottom()
scan_all_1()

# print("is_visible: ", is_visible)
print_matrix(is_visible, "is_visible")
answer = sum(sum(x) for x in is_visible)

t.stop()

print_solution_1(answer, t.last_elapsed_time())


# Part 2
t = Timer()

# marker = 0
# t.start()

# for input in data:
#     marker = find_first_time_marker_appears(input, number_of_unique_characters=14)

# t.stop()

# print_solution_2(marker, t.last_elapsed_time())