import matplotlib.pyplot as plt
import numpy as np

# Define the original vector v
v = np.array([2, 1])

# Calculate the scaled vector v/2
scaled_v = v / 2

# --- Plotting ---
# Create a figure and axis for the plot
plt.figure(figsize=(8, 6))
ax = plt.gca()

# Plot the original vector v
ax.quiver(0, 0, v[0], v[1],
          angles='xy', scale_units='xy', scale=1,
          color='blue', label='v = (2, 1)')

# Plot the scaled vector v/2
ax.quiver(0, 0, scaled_v[0], scaled_v[1],
          angles='xy', scale_units='xy', scale=1,
          color='red', label='v/2 = (1, 0.5)')

# --- Formatting the Graph ---
# Set the viewing limits
plt.xlim(-1, 3)
plt.ylim(-1, 2)

# Add a grid, labels, and a title
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Geometric Representation of a Scaled Vector')
plt.legend()

# Draw the main x and y axes
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Ensure the axes are scaled equally
ax.set_aspect('equal', adjustable='box')

# Save the plot to a file
plt.show()