from toolbox.data_reader import read_file
import numpy as np

data = read_file('day2.txt')
# print(data)

# Extract your and opponent choice
choice_score = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

# A or X = Rock
# B or Y = Paper
# C or Z = Scissors

# Opp choice vs your choice
# 0 - Draw
# 1 - Win
# -1 - Lose
win_match = {
    'A X' : 0, # Rock vs Rock
    'A Y' : 1, # Rock vs Paper
    'A Z' : -1, # Rock vs Scissors
    
    'B X' : -1, 
    'B Y' : 0,
    'B Z' : 1,
    
    'C X' : 1, 
    'C Y' : -1,
    'C Z' : 0,
}

def extract_my_choice_score(game_round):
    return choice_score[game_round[2]]

def calculate_score(game_round):
    if(win_match[game_round] == -1): # lose
        return extract_my_choice_score(game_round)
    
    if(win_match[game_round] == 0): # draw
        return extract_my_choice_score(game_round) + 3
    
    if(win_match[game_round] == 1): # win
        return extract_my_choice_score(game_round) + 6
    
my_total_score = 0

for game_round in data:
    my_total_score = my_total_score + calculate_score(game_round)

print(my_total_score)



# X means lose
# Y means draw
# Z means win

# A or X = Rock
# B or Y = Paper
# C or Z = Scissors
desired_outcome = {
    "X": -1,
    "Y": 0,
    "Z": 1, 
}

my_choice = {
    'A X' : 'Z', 
    'A Y' : 'X', 
    'A Z' : 'Y', 
    
    'B X' : 'X', 
    'B Y' : 'Y',
    'B Z' : 'Z',
    
    'C X' : 'Y',
    'C Y' : 'Z',
    'C Z' : 'X',
}


def extract_my_choice_score_2(game_round):
    return choice_score[my_choice[game_round]]

def extract_match_score(game_round):
    return desired_outcome[game_round[2]]

def calculate_score_2(game_round):
    if(extract_match_score(game_round) == -1): # lose
        return extract_my_choice_score_2(game_round)
    
    if(extract_match_score(game_round) == 0): # draw
        return extract_my_choice_score_2(game_round) + 3
    
    if(extract_match_score(game_round) == 1): # win
        return extract_my_choice_score_2(game_round) + 6
    
my_total_score = 0

for game_round in data:
    my_total_score = my_total_score + calculate_score_2(game_round)

print(my_total_score)
