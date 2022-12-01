from toolbox.data_reader import read_file
import numpy as np

data = read_file('day1.txt')
# print(data)


number_of_elfs = len([x for x in data if x == ''])

# part1
calories_per_elf = np.zeros(number_of_elfs+1)
elf = 0
for calories in data:
    if calories == '':
        elf = elf + 1
        continue

    calories_per_elf[elf] = calories_per_elf[elf] + int(calories)


print(max(calories_per_elf))

# part2
print(np.sort(calories_per_elf))
print(65240. + 68996. + 70374)
