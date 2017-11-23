'''
Created on Nov 6, 2017

@author: Mark
'''
# a shallow copy will only work one pointer level deep for lists
def shallow_copy(L):
    new_list = []
    for item in L:
        new_list.append(item)
    return new_list

# deep copy will work multiple levels down into the list hierarchy
def deep_copy(L):
    new_list = []
    for item in L:
        if isinstance(item, list):
            new_list.append(deep_copy(item))
        else:
            new_list.append(item)
    return new_list

def create_board(r, c):
    board = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(' ')
        board.append(row)
    return board

# this is called a list comprehension, where you put the logic sort of inside the list to be created
# lets you have some really short functions, but is somewhat more difficult to understand.
def create_board_comp(r, c):
    [[' ' for i in range(c)] for i in range(r) ]
    
def display_board(board):
    num_rows = len(board)
    for row in range(num_rows):
        num_cols = len(board[row])
        for col in range(num_cols):
            print(' ' + board[row][col] + ' ', end='')
            if col < num_cols - 1:
                print('|', end='')
        print()
        if row < num_rows - 1:
            print('-' * (num_cols * 4 - 1))
            
def find_max_2D(L):
    if L == [[]]:
        return None
    
    int_max = L[0][0]
    for itemList in L:
        for item in itemList:
            if item > int_max:
                int_max = item
    return int_max
print(find_max_2D([[1, 10, 9, 6], [3], [4, 12, 17, 1, 13], [8, 7]]))

def find_max_coords_2D(L):
    if L == [[]]:
        return None
    max_val = L[0][0]
    row_num = 0
    temp_row_num = 0
    col_num = 0
    for row in L:
        temp_col_num = 0
        temp_row_num += 1
        for x in row:
            temp_col_num += 1
            if x > max_val:
                max_val = x
                col_num = temp_col_num
                row_num = temp_row_num
    return(row_num, col_num)

def find_max_coords_2D_alt(L):
    max_val = L[0][0]
    row = col = 0
    for r in range(len(L)):
        for c in range(len(L[r])):
            if L[r][c] > max_val:
                max_val = L[r][c]
                row = r
                col = c
    return row, col

def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
    # you need a third and to copy one value into another.  You use the third to retrieve it, otherwise
    # it is lost

# this function has what is called a side-effect, it edits something in place without returning it
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, i, min_index)             
        