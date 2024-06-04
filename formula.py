import numpy as np
import math

def cube_function(x):
    return 100 * (x[1] - x[0]**3)**2 + (1 - x[0])**2

def branin(x):
    x1, x2 = x
    a = 1
    b = 5.1 / (4 * np.pi**2)
    c = 5 / np.pi
    r = 6
    s = 10
    t = 1 / (8 * np.pi)
    
    term1 = a * (x2 - b * x1**2 + c * x1 - r)**2
    term2 = s * (1 - t) * np.cos(x1)
    term3 = s

    return term1 + term2 + term3

def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def levy13(x):
    term1 = (np.sin(3 * np.pi * x[0]))**2
    term2 = (x[0] - 1)**2 * (1 + np.sin(3 * np.pi * x[1])**2)
    term3 = (x[1] - 1)**2 * (1 + np.sin(2 * np.pi * x[1])**2)
    return term1 + term2 + term3

def mccormick(x):
    return np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1

def rotated_ellipse01(x):
    return 7.0 * x[0]**2 - 6 * math.sqrt(3) * x[0] * x[1] + 13 * x[1]**2

def rotated_ellipse02(x):
    return x[0]**2 - x[0] * x[1] + x[1]**2


def levy(x):
    w = 1 + (x -1)/4
    wd = w[-1]
    term1 = (np.sin(np.pi * w[0]))**2
    term2 = np.sum((w[:-1] - 1)**2 * (1 + 10 * np.sin( w[:-1] * np.pi + 1 )**2 ))
    term3 = (wd - 1)**2 * (1 + np.sin(2 * np.pi * wd )**2)
    return term1 + term2 + term3

def power_function(x):
    D = len(x)
    assert D % 4 == 0, "The length of x must be a multiple of 4"
    sum_result = 0
    for i in range(1, D//4 + 1):
        term1 = (x[4*i-4] + 10*x[4*i-3])**2
        term2 = 5 * (x[4*i-2] + x[4*i-1])**2
        term3 = (x[4*i-3] + 2*x[4*i-2])**4
        term4 = 10 * (x[4*i-4] + x[4*i-1])**4
        sum_result += term1 + term2 + term3 + term4
    return sum_result

def ackley(x):
    term1 = -20 * np.exp(-0.2* np.sqrt((1/len(x)) * np.sum(x**2)) )
    term2 = - np.exp((1/len(x)) * np.sum(np.cos( 2 * np.pi * x)))
    term3 = 20 + np.exp(1)
    return term1 + term2 + term3

def bent_cigar(x):
    return x[0]**2 + 10**6 * np.sum(x**2)

def rotated_hyper_ellipsoid(x):
    sum = 0
    for i in range(len(x)):
        sum += np.sum((x[0:i])**2)  
    return sum

def sum_squares(x):
    sum = 0
    for i in range(len(x)):
        sum += i*(x[i])**2
    return sum

def sum_of_different_powers(x):
    sum = 0
    for i in range(len(x)):
        sum += np.abs(x[i])**(i+2)
    return sum


###
def functionWithXY(f):
    return lambda x,y : f(np.array([x,y]))
