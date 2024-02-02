import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Function to check if a point is inside the quarter circle
def is_inside_circle(x, y):
    return x**2 + y**2 <= 1

# Function to perform the Monte Carlo simulation
def monte_carlo_simulation(num_points):
    inside_circle = 0

    # Generate random points and count how many fall inside the quarter circle
    for _ in range(num_points):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if is_inside_circle(x, y):
            inside_circle += 1

    # Estimate the value of π
    pi_estimate = 4 * (inside_circle / num_points)
    return pi_estimate

# Function to update the plot for animation
def update(frame):
    num_points = frame * 100  # Increase the number of points over time
    pi_estimate = monte_carlo_simulation(num_points)

    # Generate random points for visualization
    points_x = np.random.uniform(0, 1, num_points)
    points_y = np.random.uniform(0, 1, num_points)

    # Separate points inside and outside the quarter circle
    inside_circle_x = [x for x, y in zip(points_x, points_y) if is_inside_circle(x, y)]
    inside_circle_y = [y for x, y in zip(points_x, points_y) if is_inside_circle(x, y)]
    outside_circle_x = [x for x, y in zip(points_x, points_y) if not is_inside_circle(x, y)]
    outside_circle_y = [y for x, y in zip(points_x, points_y) if not is_inside_circle(x, y)]

    # Clear the previous plot and plot the new points and the quarter circle
    plt.clf()
    plt.scatter(outside_circle_x, outside_circle_y, color='black', label='Outside Circle', marker='x')
    plt.scatter(inside_circle_x, inside_circle_y, color='green', label='Inside Circle',marker='o')
    plt.title(f'Monte Carlo Simulation for π: {pi_estimate:.5f}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=.1)

# Set up the initial plot
fig, ax = plt.subplots(figsize=(10, 10))
ani = FuncAnimation(fig, update, frames=range(1, 61), interval=100, repeat=True)  # Change the number of frames as needed
plt.show()
