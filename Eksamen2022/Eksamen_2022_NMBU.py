'''

Frequency response based stability analysis of
level control system of wood chip tank
using Python Control Package

Finn Aakre Haugen (finn@techteach.no)

Updated 2022 04 16

'''

# %% Imports:

import numpy as np
import control
import matplotlib.pyplot as plt

# %% Creating controller transfer function:

s = control.tf('s')

# PI controller (settings with ZN):
Kc = 3.05
Ti = 1249.5 # [s]
C = Kc + Kc/(Ti*s)

# %% Process transfer function:

# Transfer function of process model without time delay:
rho = 145  # [kg/m^3]
A = 13.4  # [m^2]
P_without_delay = 1/(rho*A*s)

# Transfer function of time delay repr by Pade approx:
t_delay = 250.0  # [s]
n_pade = 10
(num_pade, den_pade) = control.pade(t_delay, n_pade)
P_delay = control.tf(num_pade, den_pade)


# Resulting process transfer function:
P = P_without_delay*P_delay

#%% Control system transfer functions:

# Loop transfer function:
L = C*P
# print('L(s) =', L)

# Tracking transfer function:
# minreal() removes possible common factors in num and den
T = control.minreal(L/(1 + L))
# print('T =', T)

# %% Simulation of step response of T(s):

plt.close('all')

dt = 1  # Time-step [s]
t_start = 0  # [s]
t_stop = 8000  # [s]
t_array = np.arange(t_start, t_stop+dt, dt)

(t_array, y_array) = control.step_response(T, t_array)

const_r = 1

plt.figure(1)
plt.plot(t_array, np.zeros(len(y_array))+const_r, 'r',
         label='r')
plt.plot(t_array, y_array, 'b', label='y')
plt.title('Sim of response in y due to step in r')
plt.legend()
plt.grid()
plt.xlabel('t [s]')
plt.ylabel('[m]')

# %% Bode plot of loop transf fun with stability measures:

# Frequencies for Bode plot:
w0 = 0.0001  # [rad/s]
w1 = 0.01
dw = 0.0001
w = np.arange(w0, w1, dw)

plt.figure(3)

# Bode plot:
(mag, phase_rad, w) = control.bode_plot(L, w,
                                        dB=True,
                                        deg=True,
                                        margins=True,
                                        grid=True)

# Getting stability margins and crossover frequencies:
(GM, PM, wg, wp) = control.margin(L)
print('GM [1 (not dB)] =', f'{GM:.2e}')
print('PM [deg] =', f'{PM:.2e}')
print('wg [rad/s] =', f'{wg:.2e}')
print('wp [rad/s] =', f'{wp:.2e}')

plt.show()