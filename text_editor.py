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

# menu

def menu():
    print('1. Create File')
    print('2. Read File')
    print('3. Append Data to File')
    print('4. Menu')
    print('5. Clear Screen')
    print('6. Exit')


# app logic


print('Welcome to TextEditor')
menu()

while True:
    inp = int(input('Choose an Option (1-6): '))

    if inp == 1:
        filename = input('Enter File Name: ')
        data = text_editor()
        write_file(filename, data)
    elif inp == 2:
        filename = input('Enter File Name: ')
        data = read_file_v2(filename)
        print(data)
    elif inp == 3:
        filename = input('Enter File Name: ')
        new_data = text_editor()
        msg = append_data_to_file(filename, new_data)
        print(msg)
    elif inp == 4:
        menu()
    elif inp == 5:
        os.system('clear')
        #  use cls in windows os
        # os.system('cls')
    elif inp == 6:
        break
    else:
        print('Invalid Option')
