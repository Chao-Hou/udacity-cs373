# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    stable = False

    while not stable:
        stable = True
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if [x, y] == goal and value[x][y] > 0:
                    stable = False
                    value[x][y] = 0
                elif grid[x][y] == 1:
                    pass
                else:
                    for move in delta:
                        x2 = x + move[0]
                        y2 = y + move[1]
                        if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                            if value[x2][y2] + cost_step < value[x][y]:
                                value[x][y] = value[x2][y2] + cost_step
                                stable = False

    return value #make sure your function returns a grid of values as demonstrated in the previous video.

for row in compute_value():
    print row


