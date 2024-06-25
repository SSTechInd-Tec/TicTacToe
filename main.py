import os

#  our game table 

table = [
    'X', 'O', 'X', 
    'X', 'X', 'O', 
    'O', 'O', 'X'
]
table2 = [' '] * 9

def print_table(table):
    print(f' {table[0]} | {table[1]} | {table[2]} ')
    print('||||||||||||')
    print(f' {table[3]} | {table[4]} | {table[5]} ')
    print('||||||||||||')
    print(f' {table[6]} | {table[7]} | {table[8]} ')


def table_marker(table, mark, index):
    if table[index-1] == ' ':
        table[index-1] = mark
    else:
        print("This Cell Already Marked!")


def check_winner(table):
    # check if X is winner
    if (
        (table[0] == 'X' and table[1] == 'X' and table[2] == 'X') or 
        (table[3] == 'X' and table[4] == 'X' and table[5] == 'X') or
        (table[6] == 'X' and table[7] == 'X' and table[8] == 'X') or 
        (table[0] == 'X' and table[3] == 'X' and table[6] == 'X') or
        (table[1] == 'X' and table[4] == 'X' and table[7] == 'X') or
        (table[2] == 'X' and table[5] == 'X' and table[8] == 'X') or
        (table[0] == 'X' and table[4] == 'X' and table[8] == 'X') or
        (table[2] == 'X' and table[4] == 'X' and table[6] == 'X')
    ):
        return 'X is winner'
    
    # check if O is winner
    elif (
        (table[0] == 'O' and table[1] == 'O' and table[2] == 'O') or 
        (table[3] == 'O' and table[4] == 'O' and table[5] == 'O') or
        (table[6] == 'O' and table[7] == 'O' and table[8] == 'O') or 
        (table[0] == 'O' and table[3] == 'O' and table[6] == 'O') or
        (table[1] == 'O' and table[4] == 'O' and table[7] == 'O') or
        (table[2] == 'O' and table[5] == 'O' and table[8] == 'O') or
        (table[0] == 'O' and table[4] == 'O' and table[8] == 'O') or
        (table[2] == 'O' and table[4] == 'O' and table[6] == 'O')
    ):
        return 'O is winner'
    else:
        empty_cells_list = []
        for cell in table:
            if cell == ' ':
                empty_cells_list.append(cell)
        
        if len(empty_cells_list) == 0:
            return 'No one is winner'
                

# Game Play Logic

while True:
    x_index = int(input("Enter Your Position X (1-9): "))
    table_marker(table2, 'X', x_index)
    os.system('cls')
    print_table(table2)
    result_x = check_winner(table2)

    if result_x == 'X is winner':
        print(result_x)
        break
    elif result_x == 'No one is winner':
        print(result_x)
        break
    
    o_index = int(input("Enter Your Position O (1-9): "))
    table_marker(table2, 'O', o_index)
    os.system('cls')
    print_table(table2)
    result_o = check_winner(table2)
    if result_o == 'O is winner':
        print(result_o)
        break
    elif result_x == 'No one is winner':
        print(result_x)
        break
