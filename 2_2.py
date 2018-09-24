"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    def remove_zero(lst):
        """
        remove zeros in the list
        """
        lst1 = []
        for num in range(0, len(lst)):
            if lst[num] != 0:
                lst1.append(lst[num])
        if len(lst1) < len(lst):
            lst1.extend([0]*(len(lst)-len(lst1)))
        return lst1
    
    def combine(lst1):
        """
        combine numbers that are the same
        """
        for num in range(0,len(lst1)-1):
            if lst1[num]==lst1[num+1]:
                lst1[num] = lst1[num]*2
                lst1[num+1] = 0
        return lst1
    
    list1 = remove_zero(line)
    list2 = combine(list1)
    list3 = remove_zero(list2)
    return list3


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.default_list = {UP: [(0,dum_col) for dum_col in range(grid_width)],
                           DOWN: [(grid_height-1, dum_col) for dum_col in range(grid_width)],
                           LEFT: [(dum_row, 0) for dum_row in range(grid_height)],
                           RIGHT: [(dum_row, grid_width-1) for dum_row in range(grid_height)]
                          }
        self.reset()
                           
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[ 0 for dum_col in range(self.grid_width)] 
                      for dum_row in range(self.grid_height)]
        if self.empty_num() > 0:
            self.new_tile()
        if self.empty_num() > 0:
            self.new_tile()

    def empty_num(self):
        """
        return the number of empty cells.
        """
        zero_count = 0
        for num_i in range(0, self.grid_height):
            for num_j in range(0, self.grid_width):
                if self._grid[num_i][num_j] == 0:
                    zero_count += 1
        return zero_count
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == 1 or direction == 2:
            for temp_start in self.default_list[direction]:
                temp_list = []
                for num in range(0,self.grid_height):
                    temp_row = temp_start[0] + OFFSETS[direction][0]*num
                    temp_col = temp_start[1] + OFFSETS[direction][1]*num
                    temp_list.append(self.get_tile(temp_row, temp_col))
                
                new_list = merge(temp_list)
                for num in range(0,self.grid_height):
                    temp_row = temp_start[0] + OFFSETS[direction][0]*num
                    temp_col = temp_start[1] + OFFSETS[direction][1]*num
                    self.set_tile(temp_row, temp_col, new_list[num])
                                  
        else:
            for temp_start in self.default_list[direction]:
                temp_list = []
                for num in range(0,self.grid_width):
                    temp_row = temp_start[0] + OFFSETS[direction][0]*num
                    temp_col = temp_start[1] + OFFSETS[direction][1]*num
                    temp_list.append(self.get_tile(temp_row, temp_col))
                
                new_list = merge(temp_list)
                for num in range(0,self.grid_width):
                    temp_row = temp_start[0] + OFFSETS[direction][0]*num
                    temp_col = temp_start[1] + OFFSETS[direction][1]*num
                    self.set_tile(temp_row, temp_col, new_list[num])   

        if self.empty_num() > 0:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        random_row = random.randrange(0, self.grid_height)
        random_col = random.randrange(0, self.grid_width)
        if self._grid[random_row][random_col] == 0:
            if int(random.random() * 100) < 90:
                self.set_tile(random_row, random_col, 2)
            else:
                self.set_tile(random_row, random_col, 4)
        else: self.new_tile()
                
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
