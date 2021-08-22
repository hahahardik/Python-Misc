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
    w_dr = p[2]
    a = p[3]
    
    dy1dt = -g*y[1] - w**2*y[0] + a*np.cos(w_dr*t)    # y=[x, x']
    dy = [y[1], dy1dt]
    return dy    

#%% EDIT THESE PARAMETERS
#=============================================================================#

g_lin = 0.1    # Decay rate(Hz)
f0 = 1    # Frequency of oscillator (Hz)
y0 = [0, 0]     # Initial condiditon [x, x']
f_dr = 1.1     # Drive frequency
a_dr = 1        # Drive amplitude (F0/m)

#=============================================================================#

#%% Other variables
t_start = 0             # Start time (s)
g_ang = 2*np.pi*g_lin   # Angular decay width
f_dr_ang = 2*np.pi*f_dr     # Angular drive frequency
t_end = 20/(f_dr)         # Maximum time
w0 = 2*np.pi*f0         # Angular frequency
n_pts = 1000            # Number of data points in time axis
# Define time axis
t_axis = np.linspace(t_start, t_end, n_pts+1, True)
# Tuple for parameters
param = (g_ang, w0, f_dr_ang, a_dr)

#%% Solve ODE
y_sol = odeint(damped, y0, t_axis, param)
x = y_sol[:,0]

#%% Plot
plt.figure(1)
plt.clf()
plt.plot(t_axis, x)
plt.xlabel('Time (s)')
plt.ylabel('Diplacement (a. u.)')

