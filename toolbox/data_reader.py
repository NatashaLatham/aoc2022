def read_file(file_name):
    with open(f'data/{file_name}', 'r') as file:
        return [line.strip() for line in file]