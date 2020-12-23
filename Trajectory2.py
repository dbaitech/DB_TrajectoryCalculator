import math
import matplotlib.pyplot as plt

class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Projectile:
    def __init__(self, pos, v0, ang):
        self.pos0 = Position(pos.x, pos.y)     # initial position
        self.v0 = v0        # initial velocity
        self.ang = ang      # initial launch angle

        self.pos = Position(pos.x, pos.y)               # instantaneous position
        self.vx = v0 * math.cos(math.radians((ang)))    # instantaneous velocity on x axis
        self.vy = v0 * math.sin(math.radians((ang)))    # instantaneous velocity on y axis

    def move(self, dt):     # new position after dt seconds
        dx = self.vx*dt
        dy = self.vy*dt - g*dt*dt/2.0
        self.pos.move(dx, dy)
        self.vx = self.vx
        self.vy = self.vy - g*dt

    def reset(self):        # reset the instantaneous position and velocity
        self.pos.x = self.pos0.x                                    # x instantaneous position to initial position
        self.pos.y = self.pos0.y                                    # y instantaneous position to initial position
        self.vx = self.v0 * math.cos(math.radians((self.ang)))      # instantaneous velocity on x axis
        self.vy = self.v0 * math.sin(math.radians((self.ang)))      # instantaneous velocity on y axis


class Trajectory:
    def __init__(self, prj):
        self.X = []
        self.Y = []

        self.ymax = (prj.vy * prj.vy) / (2 * g)     # vertical height from the point of launch
        self.hmax = prj.pos0.y + self.ymax          # maximum height from ground
        self.ta = prj.vy / g                        # time to ascend
        self.td = math.sqrt(2 * self.hmax / g)      # time to descend
        self.tt = self.ta + self.td                 # total travel time
        self.xhmax = prj.vx * self.ta               # horizontal distance where reached maximum height
        self.xmax = prj.vx * self.tt                # maximum horizontal distance
        print('********** Trajectory key info **********')
        print('Horizontal velocity: {:5.2f} m/s'.format(prj.vx))
        print('Initial vertical velocity: {:5.2f} m/s'.format(prj.vy))
        print('Vertical height from the point of launch: {:5.2f} m'.format(self.ymax))
        print('Maximum height from ground: {:5.2f} m'.format(self.hmax))
        print('Time to ascend: {:5.2f} s'.format(self.ta))
        print('Time to descend: {:5.2f} s'.format(self.td))
        print('Total travel time: {:5.2f} s'.format(self.tt))
        print('Horizontal distance where reached maximum height: {:5.2f} m'.format(self.xhmax))
        print('Maximum horizontal distance: {:5.2f} m'.format(self.xmax))

    def addposition(self, p):
        self.X.append(p.x)
        self.Y.append(p.y)

    def reset(self):
        self.X = []
        self.Y = []

    def plot_v1(self, prj, step):
        prj.reset()                 # reset position to allow reuse of plot function
        self.reset()                # reset the trajectory list to allow reuse of plot function
        self.addposition(prj.pos)   # add initial position to trajectory points list
        ptime = 0.0                 # plot time
        while ptime <= self.tt:
            prj.move(step)          # new position after tick seconds
            self.addposition(prj.pos)   # record the new position
            ptime += step

        fig, ax = plt.subplots()    # Create a figure containing a single axes subplot.
        plt.xlabel('Distance')
        plt.ylabel('Height')
        plt.title("Plot projectile trajectory (using time)")
        ax.plot(self.X, self.Y)     # Plot some data on the axes.
        plt.show()


def datainit():
    global hi, vi, angi, g
    g = 9.80665  # gravitational acceleration in m/s2
    hi = float(input('Enter Initial height from ground in meters: '))
    vi = float(input('Enter Initial velocity in meters per second: '))
    angi = float(input('Enter the launching angle in degrees: '))
    print('********** Initial conditions **********')
    print('Gravitational acceleration: {:5.2f} m/s2'.format(g))
    print('Inital height from ground: {:5.2f} m'.format(hi))
    print('Inital velocity: {:5.2f} m/s'.format(vi))
    print('Launching angle: {:5.2f} degrees'.format(angi))
    print()
    if vi < 0 or angi < 0:
        print("WARNING: Velocity or angle can't be negative!")
        return -1
    else:
        return 0

if datainit() == 0:
    p = Position(0.0, hi)
    pj = Projectile(p, vi, angi)
    trj = Trajectory(pj)
    step = 0.01                     # time increment for each trajectory position
    ttime = 0.0                     # total time

    trj.plot_v1(pj, step)
