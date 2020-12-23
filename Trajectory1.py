# import numpy as np
import math
import matplotlib.pyplot as plt

g = 9.80665 # gravitational acceleration constant in m/s2
samples_no = 100 # the number of points on the plot

def datainit():
    global h0, v0, ang
    h0 = float(input('Enter Initial height from ground in meters: '))
    v0 = float(input('Enter Initial velocity in meters per second: '))
    ang = float(input('Enter the launching angle in degrees: '))
    print('********** Initial conditions **********')
    print('Gravitational acceleration: {:5.2f} m/s2'.format(g))
    print('Inital height from ground: {:5.2f} m'.format(h0))
    print('Inital velocity: {:5.2f} m/s'.format(v0))
    print('Launching angle: {:5.2f} degrees'.format(ang))
    print()
    if v0 < 0 or ang < 0:
        print("WARNING: Velocity or angle can't be negative!")
        return -1
    else:
        return 0

def calctrajectory():
    global vx, vy, ymax, hmax, ta, td, tt, xhmax, xmax
    global tt
    vx = v0 * math.cos(math.radians((ang))) # horizontal velocity
    vy = v0 * math.sin(math.radians((ang))) # initial vertical velocity
    ymax = (vy * vy) / (2 * g)              # vertical height from the point of launch
    hmax = h0 + ymax                        # maximum height from ground
    ta = vy / g                             # time to ascend
    td = math.sqrt(2 * hmax / g)            # time to descend
    tt = ta + td                            # total travel time
    xhmax = vx * ta                         # horizontal distance where reached maximum height
    xmax = vx * tt                          # maximum horizontal distance
    print('********** Trajectory key info **********')
    print('Horizontal velocity: {:5.2f} m/s'.format(vx))
    print('Initial vertical velocity: {:5.2f} m/s'.format(vy))
    print('Maximum height from the point of launch: {:5.2f} m'.format(ymax))
    print('Maximum height from ground: {:5.2f} m'.format(hmax))
    print('Time to ascend: {:5.2f} s'.format(ta))
    print('Time to descend: {:5.2f} s'.format(td))
    print('Total travel time: {:5.2f} s'.format(tt))
    print('Horizontal distance where reached maximum height: {:5.2f} m'.format(xhmax))
    print('Maximum horizontal distance: {:5.2f} m'.format(xmax))
    return

def plottraj_v1(xtime, samples_no):
    """
    Function to plot the trajectory based on total time travelled
    :param xtime: total time traveled on x axis
    :param samples_no: the number of samples of Y and Y coordinates
    :return: nothing
    """
    step = xtime / samples_no   # the step between the points
    t = 0
    x = []  # list to store the X coordinates
    y = []  # list to store the Y coordinates
    while t <= tt:      # calculate the X and Y coordinates and append the to the lists
        px = vx*t
        py = h0 + (vy*t) - (g*t*t/2)
        x.append(px)
        y.append(py)
        t += step
    fig, ax = plt.subplots()  # Create a figure containing a single axes subplot.
    ax.plot(x, y)  # Plot the data on the axes.
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.title("Plot Projectile Trajectory (using time)")
    plt.show()
    return

def plottraj_v2(v0, ang, xmax, samples_no):
    """
    Function to plot the the trajectory based on (max) distance travelled on X axis
    :param v0: initial velocity
    :param ang: angle
    :param xmax: (max) distance travelled on X axis
    :param samples_no: the number of samples of Y and Y coordinates
    :return: nothing
    """
    x = []  # list to store the X coordinates
    y = []  # list to store the Y coordinates
    xi=0
    while xi<= xmax:    # calculate the X and Y coordinates and append the to the lists
        x.append(xi)
        yi = h0 + (xi * math.tan(math.radians((ang)))) - ((g * xi * xi) / (2 * v0 * v0 * math.cos(math.radians((ang))) * math.cos(math.radians((ang)))))
        y.append(yi)
        xi += xmax/samples_no
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.title("Plot projectile trajectory (using trajectory equation)")
    ax.plot(x, y)  # Plot the data on the axes.
    plt.show()
    return

if datainit() == 0:
    calctrajectory()
    plottraj_v1(tt, samples_no)
    plottraj_v2(v0, ang, xmax, samples_no)

