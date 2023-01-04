import numpy as np
import matplotlib.pyplot as plt

height_initial = 10  # Start height for Wood chips level (m)
height_min = 0  # Lowest value for chip tank (m)
height_max = 15  # Highest value for chip tank (m)
u = 50  # Control signal to feed screw (%)
k_s = 0.5  # Feed screw gain (%)
w_s = k_s * u  # Feed screw flow (kg/s)
w_in = w_s  # Wood chips flow into tank (kg/s)
w_out = 25  # Wood chips outflow from tank (kg/s)
p = 145  # Wood chips density (kg/m^3)
A = 13.4  # Tank cross-sectional area (m^2)
t = 250  # Transport time on conveyor belt (s)

dt = 1  # Time step
time_start = 0  # Initial time
time_end = 5000  # Final time
n_sim = int((time_end - time_start)/dt) + 1  # Number of runs the simulation shall take
height_simulation = height_initial  # Sett the high in the simulation the same as the start height


def calculate_slope(height__array):
    x_start = 1000
    x_end = 4000
    y_start = height__array[x_start]
    y_end = height__array[x_end]
    slop = (y_end - y_start) / (x_end - x_start)  # Calculate the slope
    return slop


def calculate_height(height__simulation, w__in):
    height__simulation = np.clip(height__simulation, height_min, height_max)  # Prevents the height
    # from going lower or higher than the silo
    h_derivative = (1 / (p * A)) * (w__in - w_out)  # Formula for calculating the derivative
    # of height
    height__simulation += dt * h_derivative  # updates the height after one second
    return height__simulation


def plot(x_axis, y_axis):
    slope = calculate_slope(y_axis)
    print('Slope to graph = ', slope)  # Print the slope per hour
    plt.plot(x_axis, y_axis)  # Plots the height in a graph
    plt.title('Height of Wood chips in tank')
    plt.xlabel('Time in seconds')
    plt.ylabel('Height in meter')
    plt.show()  # Shows the plot


# %% Task 1
numb_seconds_array = np.zeros(n_sim)  # Creates an empty array
height_array = np.zeros(n_sim)  # Creates an empty array
w_s_array = np.zeros(n_sim)  # Creates an empty array

for seconds in range(n_sim):  # The simulation loop
    numb_seconds_array[seconds] = seconds  # Adds the seconds to ann array
    w_s_array[seconds] = w_s  # Adds the inflow to ann array
    w_in = w_s_array[seconds - t]  # Used to calculate the inflow with delay
    height_simulation = calculate_height(height_simulation, w_in)
    height_array[seconds] = height_simulation

plot(numb_seconds_array, height_array)


# %% Task 2
numb_seconds_array = np.zeros(n_sim)  # Creates an empty array
height_array = np.zeros(n_sim)  # Creates an empty array
w_s_array = np.zeros(n_sim)  # Creates an empty array

height_simulation = height_initial  # Sett the high in the simulation the same as the start height
for seconds in range(n_sim):  # The simulation loop
    if seconds == 500:  # Chooses the time the machine steps up from 50% to 55%
        u = 55
    w_s = u * k_s  # Calculate the w_s again

    numb_seconds_array[seconds] = seconds  # Adds the seconds to ann array
    w_s_array[seconds] = w_s  # Adds the inflow to ann array
    w_in = w_s_array[seconds - t]  # Used to calculate the inflow with delay
    height_simulation = calculate_height(height_simulation, w_in)
    height_array[seconds] = height_simulation

plot(numb_seconds_array, height_array)
