"""
This script calculates and plots superposition of two one-dimensional oscillators.
Play with the parameters in "Edit parameters here" section.
"""

#%% Load packages
import numpy as np
import os
import matplotlib.pyplot as plt
import numpy.matlib

#%% Define parameters
n_f = 100        # Number of modes (total available)
freq = np.arange(1, n_f)

#%% EDIT THESE PARAMETERS
#=============================================================================#

f1 = 50    # Frequency of oscillator 1 (Hz)
f2 = 13    # Frequency of oscillator 2 (Hz)
a1 = 1      # Amplitude of oscillator 1 (arbitrary units)
a2 = 0.1      # Amplitude of oscillator 2 (arbitrary units)
p = 0.5       # Phase difference between the two oscillators, phi_2 - phi_1 (pi/rad)
    		  # Phase diff of 180 deg: p = 1
			  # Phase diff of 90 deg: p = 0.5
t_end = 1   # End of time axis (s)

#=============================================================================#
#%% Other variables
t_start = 0     # Start time (s)
n_pts = 10000   # Number of data points in time axis
# Define time axis
t_axis = np.linspace(t_start, t_end, n_pts+1, True)

#%% Calculate displacements
# Oscillator 1
x1 = a1*np.cos(2*np.pi*f1*t_axis)       # 2*pi converts linear freq. to anfular freq.
# Oscillator 2
x2 = a2*np.cos(2*np.pi*f2*t_axis + np.pi*p)
# Superposition
x_t = x1 + x2

#%% Plots
# Offsets
o2 = a2 + np.max(x_t)
o1 = a1 + np.max(x2+o2)
plt.figure(1)
plt.clf()
plt.plot(t_axis, x1+o1, t_axis, x2+o2, t_axis, x_t)
plt.xlabel('Time (s)')
plt.ylabel('Diplacement (a. u.)')
