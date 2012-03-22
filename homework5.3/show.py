import task
import matplotlib.pyplot as plt

def showpath(path, fix, answer):
    x_path = [dot[0] for dot in path]
    y_path = [dot[1] for dot in path]

    x_path.append(path[0][0])
    y_path.append(path[0][1])

    x_fix = []
    y_fix = []
    x_nofix = []
    y_nofix = []

    for ii, dot in enumerate(path):
        if fix[ii]:
            x_fix.append(dot[0])
            y_fix.append(dot[1])
        else:
            x_nofix.append(dot[0])
            y_nofix.append(dot[1])

    x_answer = [dot[0] for dot in answer]
    y_answer = [dot[1] for dot in answer]

    x_answer.append(answer[0][0])
    y_answer.append(answer[0][1])

    plt.plot(x_path, y_path, 'b-', x_fix, y_fix, 'ro', x_nofix, y_nofix, 'bo', x_answer, y_answer, 'k-')
    plt.axis([min(x_path + x_answer + x_fix) - 1, max(x_path + x_answer + x_fix) + 1, \
              min(y_path + y_answer + y_fix) - 1, max(y_path + y_answer + y_fix) + 1])

    plt.show()

#======================================================================

testpath1=[[0, 0], #fix
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0], #fix
      [6, 1],
      [6, 2],
      [6, 3], #fix
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3], #fix
      [0, 2],
      [0, 1]]
testfix1 = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

answer1 = task.smooth(testpath1, testfix1)
showpath(testpath1, testfix1, answer1)

testpath2 = [[0, 0], # fix
             [2, 0],
             [4, 0], # fix
             [4, 2],
             [4, 4], # fix
             [2, 4],
             [0, 4], # fix
             [0, 2]]
testfix2 = [1, 0, 1, 0, 1, 0, 1, 0]

answer2 = task.smooth(testpath2, testfix2)
showpath(testpath2, testfix2, answer2)

