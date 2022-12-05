def read_file(file_name):
    with open(f'data/{file_name}', 'r') as file:
        return [line.strip() for line in file]

def read_file_no_strip(file_name):
    with open(f'data/{file_name}', 'r') as file:
        return [line for line in file]