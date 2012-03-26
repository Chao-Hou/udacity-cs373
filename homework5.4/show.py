from math import *
import matplotlib.pyplot as plt

from task import robot

radius = 25.0
params = [10.0, 15.0, 0.0]

x_track = [cos((t*pi/100)+(pi/2))*radius + radius for t in range(100)] \
        + [cos((t*pi/100)-(pi/2))*radius + 3*radius for t in range(100)]

y_track = [sin((t*pi/100)+(pi/2))*radius + radius for t in range(100,0,-1)] \
        + [sin((t*pi/100)-(pi/2))*radius + radius for t in range(100,0,-1)]

x_track.append(radius)
y_track.append(0.0)

#Draw the path
x_path = [0.0,]
y_path = [radius,]

myrobot = robot()
myrobot.set(0.0, radius, pi / 2.0)
speed = 1.0 # motion distance is equal to speed (we assume time = 1)
err = 0.0
int_crosstrack_error = 0.0
N = 200

crosstrack_error = myrobot.cte(radius)

for i in range(N*2):
    diff_crosstrack_error = - crosstrack_error
    crosstrack_error = myrobot.cte(radius)
    diff_crosstrack_error += crosstrack_error
    int_crosstrack_error += crosstrack_error
    steer = - params[0] * crosstrack_error \
            - params[1] * diff_crosstrack_error \
            - params[2] * int_crosstrack_error
    myrobot = myrobot.move(steer, speed)
    if i >= N:
        err += crosstrack_error ** 2

    x_path.append(myrobot.x)
    y_path.append(myrobot.y)

plt.figure()
plt.plot(x_track, y_track, 'k-', x_path, y_path, 'bo')
plt.axis([-radius*0.1, 4.1*radius, -radius*0.1, 2.1*radius])
plt.show()

