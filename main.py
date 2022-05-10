from math import pi, sqrt, cos

# we will use the circle of 1 to find pi, the circumfrence of the circle of 1 is 2 * pi which means that pi = circumfrence/2
# the function that creates the circle of 1 is  X^2 + Y^2 = 1

# in order to optimize the code we don't need to measure the entire circumfrence but only a small size of it like 1 degree and multiply by 360

def deg_to_rad(deg):
    return deg * pi/180

def circle_of_one(x):
    return 1 - x**2

def euclidean_2d(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def get_pi_approx(step_size, degrees):
    max_dist_from_start = sqrt(2 - 2*cos(deg_to_rad(degrees)))
    startx = 0
    starty = 1
    curx = 0
    cury= 1
    circ = 0
    while(euclidean_2d(startx, starty, curx, cury) <= max_dist_from_start):
        cury = circle_of_one(curx)
        nextx = curx + step_size
        nexty = circle_of_one(nextx)
        circ += euclidean_2d(curx, cury, nextx, nexty)
        curx = nextx

    circ = circ * 360/degrees
    return circ/2


pi_approx = get_pi_approx(0.000000001, 0.5)

print("Pi approx: ", pi_approx)
print("Error: ", pi - pi_approx)