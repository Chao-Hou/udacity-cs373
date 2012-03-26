import task
import matplotlib.pyplot as plt

def showpath(path, answer):
    x_path = [dot[0] for dot in path]
    y_path = [dot[1] for dot in path]

    x_path.append(path[0][0])
    y_path.append(path[0][1])

    x_answer = [dot[0] for dot in answer]
    y_answer = [dot[1] for dot in answer]

    x_answer.append(answer[0][0])
    y_answer.append(answer[0][1])

    plt.figure()
    plt.plot(x_path, y_path, 'b-', x_path, y_path, 'bo', x_answer, y_answer, 'k-')
    plt.axis([min(x_path + x_answer) - 1, max(x_path + x_answer) + 1, \
              min(y_path + y_answer) - 1, max(y_path + y_answer) + 1])

#======================================================================

testpath1 = [[0, 0],
             [1, 0],
             [2, 0],
             [3, 0],
             [4, 0],
             [5, 0],
             [6, 0],
             [6, 1],
             [6, 2],
             [6, 3],
             [5, 3],
             [4, 3],
             [3, 3],
             [2, 3],
             [1, 3],
             [0, 3],
             [0, 2],
             [0, 1]]

answer1 = task.smooth(testpath1)
showpath(testpath1, answer1)

testpath2 = [[1, 0], # Move in the shape of a plus sign
             [2, 0],
             [2, 1],
             [3, 1],
             [3, 2],
             [2, 2],
             [2, 3],
             [1, 3],
             [1, 2],
             [0, 2], 
             [0, 1],
             [1, 1]]

answer2 = [[1.239080543767428, 0.5047204351187283],
           [1.7609243903912781, 0.5047216452560908],
           [2.0915039821562416, 0.9085017167753027],
           [2.495281862032503, 1.2390825203587184],
           [2.4952805300504783, 1.7609262468826048],
           [2.0915003641706296, 2.0915058211575475],
           [1.7609195135622062, 2.4952837841027695],
           [1.2390757942466555, 2.4952826072236918],
           [0.9084962737918979, 2.091502621431358],
           [0.5047183914625598, 1.7609219230352355],
           [0.504719649257698, 1.2390782835562297],
           [0.9084996902674257, 0.9084987462432871]]

answer2 = task.smooth(testpath2)
showpath(testpath2, answer2)

plt.show()
