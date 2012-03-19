# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------

    frontier = [[0] + init]
    explored = []

    #print "initial open list:"
    #print "\t %s" % (frontier[0])
    #print "---"

    while True:
        s = min(frontier)
        frontier.remove(s)

        #print "take list item:"
        #print "\t %s" % (s)

        explored.append(s)

        if s[1:] == goal:
            #print "####### search successful"
            return s

        for move in delta:
            next = [s[0] + cost, s[1] + move[0], s[2] + move[1]]

            #Discard X out of bounds
            if next[1] < 0 or next[1] > len(grid)-1:
                continue

            #Discard Y out of bounds
            if next[2] < 0 or next[2] > len(grid[0])-1:
                continue

            #Discard collisions
            if grid[next[1]][next[2]] == 1:
                continue

            if next[1:] not in [ x[1:] for x in explored ] and next[1:] not in [ x[1:] for x in frontier ]:
                frontier.append(next)

        #print "new open list:"
        #for ff in frontier:
        #    print "\t %s" % (ff)
        #print "---"

        if len(frontier) == 0:
            return "fail"

print search()
