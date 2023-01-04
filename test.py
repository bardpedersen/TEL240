"""
In this task we modified code from the lectures to satisfy our work requirement.
The code we modified was retrieved from PowerPoint:
Tilstandsestimering med Kalman-filter [Kap. 34], Ons 6.4 kl 1415-1600
Date retrieved: 2.mai 2022
Code mady by: Finn Aakre Haugen.
Original code description can be found in the comment bellow.
"""

"""

Level control of buffer tank with PI controller
+ Kalman filter for estimation of assumed unknown inflow.

Process model:

    dh_dt = (1/A_area)*(F_in - F_out)

where:

    - h [m] is the water level in the tank
    - F_in [m^3/s] is water inflow
    - F_out [m^3/s] is water outflow
    - A_area [m^2] is cross-sesctional area of tank.

The level control signal to the outlet pump is

    u = F_out [m^3/s]

The controller is a standard PI controller tuned with
the Skogestad method.

The level meas has uniformly distributed random noise.

No random process disturbance is included.

Finn Aakre Haugen, USN
finn.haugen@usn.no

2020 07 17

Programmed in Python 3.7.

"""

import matplotlib.pyplot as plt
import numpy as np

# Time settings:
time_steps = 10  # Sim time-step [s]
time_start = 0.0  # [s]
time_stop = 10000  # [s]
num_sim = int((time_stop - time_start) / time_steps) + 1

# Defining arrays for plotting:
t_array = np.zeros(num_sim)
h_array = np.zeros(num_sim)
h_sp_array = np.zeros(num_sim)
F_out_array = np.zeros(num_sim)
F_in_array = np.zeros(num_sim)

# Model parameters:
A_area = 2000  # [m2]
F_in = 3  # [m^3/s]
h_sp = 1
h_measmin = 0  # [m] Min level av water
h_measmax = 4  # [m] Max level av water

# Controller parameters:
Tc = 1000  # [s] Specified closed loop time constant
Ki = -1 / A_area  # Process integrator gain

# Skogestad methode:
Kc = 1 / (Ki * Tc)  # [(m3/s)/m] Controller gain
Ti = 2 * Tc  # [s] Integrator gain


# Definition of function of PI controller:
def pi_controller(y_sp_k, y_m_k, f_out_i_km1, Kc_LC, Ti_LC, time_steps):

    flow_out_man = 3  # [m3/s]
    flow_out_min = 0  # [m3/s]
    flow_out_max = 8  # [m3/s]
    flow_out_i_min = -8  # [m3/s]
    flow_out_i_max = 8  # [m3/s]

    e_k = y_sp_k - y_m_k  # Control error
    flow_out_p_k = Kc_LC * e_k  # P term

    # Anti-windup by limiting integral term:
    flow_out_i_k_tempor = f_out_i_km1 + (Kc_LC / Ti_LC) * time_steps * e_k
    flow_out_i_k = np.clip(flow_out_i_k_tempor, flow_out_i_min, flow_out_i_max)

    flow_out_k_tempor = flow_out_man + flow_out_p_k + flow_out_i_k
    flow_out_k = np.clip(flow_out_k_tempor, flow_out_min, flow_out_max)

    return flow_out_k, flow_out_i_k


# Initial states:
h_k = 1  # [m]
F_out_i_km1 = 0.0  # [m3/s]

# For-loop for simulation:
for k in range(0, num_sim):
    t_k = k * time_steps

    # Sinus wave
    F_in = np.sin((2*np.pi*(1/1200)) * t_k) + 3

    # Level PI controller:
    (F_out_k, F_out_i_k) = pi_controller(h_sp, h_k, F_out_i_km1, Kc, Ti, time_steps)

    # Process simulation:
    dh_dt_k = (1 / A_area) * (F_in - F_out_k)
    h_kp1_tempor = h_k + dh_dt_k * time_steps
    h_kp1 = np.clip(h_kp1_tempor, h_measmin, h_measmax)

    # Arrays for plotting:
    t_array[k] = t_k
    h_sp_array[k] = h_sp
    h_array[k] = h_k
    F_out_array[k] = F_out_k
    F_in_array[k] = F_in

    # Time shift:
    F_out_i_km1 = F_out_i_k
    h_k = h_kp1


# Plotting:
plt.close("all")
plt.figure(num=1, figsize=(12, 9))

plt.subplot(2, 1, 1)
plt.grid()
plt.xlim(time_start, time_stop)
plt.ylim(0, 2)
plt.plot(t_array, h_sp_array, 'g')
plt.plot(t_array, h_array, 'b')
plt.xlabel('t [s]')
plt.ylabel('[m]')
plt.legend(('height_set-point', 'height',))

plt.subplot(2, 1, 2)
plt.grid()
plt.xlim(time_start, time_stop)
plt.ylim(0, 6)
plt.plot(t_array, F_in_array, 'b')
plt.plot(t_array, F_out_array, 'r')
plt.xlabel('t [s]')
plt.ylabel('[cm3/s]')
plt.legend(('Flow_in', 'Flow_out',))

plt.show()
