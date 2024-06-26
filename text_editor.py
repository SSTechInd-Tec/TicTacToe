import os
from random import randint

#  file reader function 

def read_file(filename):
    try: 
        with open(filename, mode='r') as file:
            return file.read()
    except FileNotFoundError:
        return f'No Such File: {filename}'
    

def read_file_v2(filename):
    if os.path.isfile(filename):
        with open(filename, mode='r') as file:
            return file.read()
    else:
        return f'No Such File: {filename}'
    


#  file writer function 

def write_file(filename, text="Some Text"):
    if os.path.isfile(filename):
        filename_ext = os.path.splitext(filename)[1]
        only_filename = os.path.splitext(filename)[0]
        filename = f'{only_filename}-{randint(1, 1000)}{filename_ext}'

    with open(filename, mode='w') as file:
        file.write(text)
    
    return f'Successfully wrote a file: {filename}'


#  append new data to a file

def append_data_to_file(filename, new_data):
    if os.path.isfile(filename):
        with open(filename, mode='a') as file:
            file.write(f'\n{new_data}')
        return f'Successfully appended data to a file: {filename}'
    else:
        return f'No Such File: {filename}'


#  text editor

def text_editor():
    l = []

    while True:
        line = input('~ ')
        if line == '$S':
            break
        else:
            l.append(line)


    convert_to_str = '\n'.join(l)

    return convert_to_str


# app logic 
