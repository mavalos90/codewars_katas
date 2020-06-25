# Chess Fun 1: Chess Board Cell Color
# 6 kyu

'''
Task
Given two cells on the standard chess board, determine whether they have the same color or not.

Example
For cell1 = "A1" and cell2 = "C3", the output should be true.
For cell1 = "A1" and cell2 = "H3", the output should be false.

Input/Output
[input] string cell1

[input] string cell2

[output] a boolean value

true if both cells have the same color, false otherwise.
'''

def chess_board_cell_color(cell1, cell2):
    #cx = 0 if black, cx = 1 if white
    c1 = (ord(cell1[0]) + int(cell1[1])) % 2
    c2 = (ord(cell2[0]) + int(cell2[1])) % 2
    return c1 == c2