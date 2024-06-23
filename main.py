#  our game table 

table = [
    'X', 'O', 'X', 
    'X', 'X', 'O', 
    'O', 'O', 'X'
]
table2 = [' '] * 9

def print_table(table):
    print(f' {table[0]} | {table[1]} | {table[2]} ')
    print('------------')
    print(f' {table[3]} | {table[4]} | {table[5]} ')
    print('------------')
    print(f' {table[6]} | {table[7]} | {table[8]} ')


def table_marker(table, mark, index):
    table[index-1] = mark


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
        return 'No one is winner'

# Game Play Logic
