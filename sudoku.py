# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 01:50:58 2018

@author: dmonkoff
"""

import numpy as np
import random
def get_next_coord(i,j):
    if j == 8:
        return (i+1,0)
    else:
        return (i,j+1)
    
def generate_sudoku(field,i,j):
    #print((i,j))
    values = set(range(1,10))
    vertical_values = set(field[:,j])
    values = values.difference(vertical_values)
    horizontal_values = set(field[i,:])
    values = values.difference(horizontal_values)
    
    #values in closest square
    square_center_y = (i//3)*3+1
    square_center_x = (j//3)*3+1
    square_values = set(field[square_center_y-1:square_center_y+2
                              ,square_center_x-1:square_center_x+2].ravel())
    values = values.difference(square_values)
    res = None
    while res == None:
        if len(values) == 0:
            field[i,j] = 0
            return None
        else:
            elem = random.sample(values, 1)[0]
            values.remove(elem)
            field[i,j] = elem
            i_next,j_next = get_next_coord(i,j)
            if (i_next == 9):
                break
            res = generate_sudoku(field,i_next,j_next)
    return elem


field = np.zeros((9,9), dtype=np.int8)
print('generating')
a = generate_sudoku(field,0,0)
print('done')