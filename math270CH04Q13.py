import matplotlib.pyplot as plt
import numpy as np

# Define the vectors u and w
u = np.array([-2, 3])
w = np.array([-3, -2])

# Calculate the scaled vector 2w and the final resultant vector v
scaled_w = 2 * w
v = u + scaled_w

# --- Plotting ---
# Create a figure and axis for the plot
plt.figure(figsize=(8, 8))
ax = plt.gca()

# 1. Plot vector u from the origin (0,0)
ax.quiver(0, 0, u[0], u[1],
          angles='xy', scale_units='xy', scale=1,
          color='blue', label='u = (-2, 3)')

# 2. Plot vector 2w starting from the tip of u
ax.quiver(u[0], u[1], scaled_w[0], scaled_w[1],
          angles='xy', scale_units='xy', scale=1,
          color='green', label='2w = (-6, -4)')

# 3. Plot the resultant vector v from the origin
ax.quiver(0, 0, v[0], v[1],
          angles='xy', scale_units='xy', scale=1,
          color='red', label='v = u + 2w = (-8, -1)')

# --- Formatting the Graph ---
# Set the viewing limits of the x and y axes
plt.xlim(-9, 2)
plt.ylim(-5, 4)

# Add a grid, axis labels, and a title
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Geometric Representation of v = u + 2w')

# Add a legend to identify the vectors
plt.legend()

# Draw the main x and y axes for reference
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Ensure the x and y axes are scaled equally
ax.set_aspect('equal', adjustable='box')

# Display the final plot
plt.show()