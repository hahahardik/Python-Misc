# -*- coding: utf-8 -*-
"""
This script solves ODE for damped oscillator.
Play with the parameters in "Edit parameters here" section.
"""
#%% Load packages
import numpy as np
import os
import matplotlib.pyplot as plt
import numpy.matlib
from scipy.integrate import odeint

#%% Define differential equation
def damped(y, t, *p):  # p is the list of parameters
    g = p[0]        # gamma
    w = p[1]       # omega_0
    
    dy1dt = -g*y[1] - w**2*y[0]     # y=[x, x']
    dy = [y[1], dy1dt]
    return dy    

#%% EDIT THESE PARAMETERS
#=============================================================================#

g_lin = 2    # Decay rate(Hz)
f0 = 1    # Frequency of oscillator (Hz)
y0 = [1, 0]     # Initial condiditon [x, x']

#=============================================================================#

#%% Other variables
t_start = 0             # Start time (s)
g_ang = 2*np.pi*g_lin   # Angular decay width
t_end = 10/(f0)         # Maximum time
w0 = 2*np.pi*f0         # Angular frequency
n_pts = 1000            # Number of data points in time axis
# Define time axis
t_axis = np.linspace(t_start, t_end, n_pts+1, True)
# Tuple for parameters
param = (g_ang, w0)

#%% Solve ODE
y_sol = odeint(damped, y0, t_axis, param)
x = y_sol[:,0]

#%% Plot
plt.figure(1)
plt.clf()
plt.plot(t_axis, x)
plt.xlabel('Time (s)')
plt.ylabel('Diplacement (a. u.)')

