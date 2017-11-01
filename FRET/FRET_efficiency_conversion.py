from scipy.integrate import odeint
import matplotlib.pyplot as plt
# Parameter values
# Masses:
m1 = 1.0
m2 = 1.0
# Spring constants
k1 = 1
k2 = 1
# Natural lengths
L1 = 0.5
L2 = 0.5
# Friction coefficients
b1 = 0.2
b2 = 0.2

# Initial conditions
# x1 and x2 are the initial displacements; y1 and y2 are the initial velocities
x1 = 0
y1 = 1.0
x2 = 40
y2 = 1.0

# ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 30
numpoints = 2500

# Create the time samples for the output of the ODE solver.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

p = [m1, m2, k1, k2, L1, L2, b1, b2]

import numpy as np
from numpy import loadtxt
from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
from matplotlib.font_manager import FontProperties
%matplotlib inline

class Coupled_Oscillator(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.w0 = [self.x1, self.y1, self.x2, self.y2]
        self.R_0 = 45
        self.speed = 1
    def vectorfield(self, t):
        # Create f = (x1',y1',x2',y2'):
        f = [y1,
            (-b1 * self.y1 - k1 * (self.x1 - L1) + k2 * (self.x2 - self.x1 - L2)) / m1,
            self.y2,
            (-b2 * self.y2 - k2 * (self.x2 - self.x1 - L2)) / m2]
        return f
    def solver(self):
        # Call the ODE solver.
        wsol = odeint(vectorfield, self.w0, t, args=(p,),
              atol=abserr, rtol=relerr)
        average_transfer_time = np.average(-1*(((1+(np.abs(wsol[:,0] - wsol[:,2])/(self.R_0))**6)**(-1))-1)*3.3)
        #print average_transfer_time
        average_time_of_molecule = np.average(np.abs(wsol[:,0] - wsol[:,2])/self.speed)
        return [average_transfer_time,average_time_of_molecule]
    def plot(self):
        # Two subplots, the axes array is 1-d
        f, axarr = plt.subplots(2, sharex=False)
        axarr[0].plot(t, self.solver()[0], 'b', linewidth=lw)
        axarr[1].plot(t, self.solver()[1], 'g', linewidth=lw)
		
		
N = 3000
import matplotlib.mlab as mlab
times_for_transfer = []
times_for_molecule = []
oscillatorList1 = [Coupled_Oscillator(np.random.uniform()+i,np.random.uniform(), np.random.uniform()+200+i, np.random.uniform()) for i in range(N)]
oscillatorList2 = [Coupled_Oscillator(np.random.uniform()+i,np.random.uniform(), np.random.uniform()+200+i, np.random.uniform()) for i in range(N)]
oscillatorList = [oscillatorList1, oscillatorList2]

for i in range(2):
    for j in range(N):
            x = oscillatorList[i][j].solver()
            times_for_transfer.append(x[0])
            times_for_molecule.append(x[1])
			
n, bins, patches = plt.hist(times_for_molecule, 500, facecolor='blue', alpha=0.75)
n, bins, patches = plt.hist(times_for_transfer, 500, facecolor='green', alpha=0.75)

from scipy.signal import deconvolve
result = deconvolve(times_for_molecule, times_for_transfer)

n, bins, patches = plt.hist(result, 500, facecolor='green', alpha=0.75)