import matplotlib.pyplot as plt
import numpy as np

# Define the vectors u and w
u = np.array([-2, 3])
w = np.array([-3, -2])

# Calculate the intermediate and final vectors
scaled_u = 3 * u
sum_vector = scaled_u + w
v = sum_vector / 2

# --- Plotting ---
# Create a figure and axis for the plot
plt.figure(figsize=(8, 8))
ax = plt.gca()

# 1. Plot vector 3u from the origin
ax.quiver(0, 0, scaled_u[0], scaled_u[1], angles='xy', scale_units='xy', scale=1, color='skyblue', label='3u = (-6, 9)')

# 2. Plot vector w starting from the tip of 3u
ax.quiver(scaled_u[0], scaled_u[1], w[0], w[1], angles='xy', scale_units='xy', scale=1, color='green', label='w = (-3, -2)')

# 3. Plot the intermediate sum vector (3u + w)
ax.quiver(0, 0, sum_vector[0], sum_vector[1], angles='xy', scale_units='xy', scale=1, color='gray', alpha=0.5, label='3u + w = (-9, 7)')

# 4. Plot the final resultant vector v
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='red', label='v = (3u + w)/2 = (-4.5, 3.5)')

# --- Formatting the Graph ---
# Set the viewing limits of the x and y axes
plt.xlim(-10, 2)
plt.ylim(-3, 10)

# Add a grid, axis labels, and a title
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Geometric Representation of v = (3u + w) / 2')

# Add a legend to identify the vectors
plt.legend()

# Draw the main x and y axes for reference
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Ensure the x and y axes are scaled equally
ax.set_aspect('equal', adjustable='box')

# Save the plot to a file
plt.show()