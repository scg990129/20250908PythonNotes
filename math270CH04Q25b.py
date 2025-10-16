import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the original vector v
v = np.array([1, 2, 2])

# Calculate the scaled vector -v
scaled_v = -v

# --- Plotting ---
# Create a 3D figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Draw the vectors ---
# The quiver function draws arrows in 3D.
# We specify the start (0,0,0) and the vector components (x,y,z).

# Plot the original vector v
ax.quiver(0, 0, 0, v[0], v[1], v[2],
          color='blue', label='v = (1, 2, 2)',
          arrow_length_ratio=0.1)

# Plot the scaled vector -v
ax.quiver(0, 0, 0, scaled_v[0], scaled_v[1], scaled_v[2],
          color='red', label='-v = (-1, -2, -2)',
          arrow_length_ratio=0.1)


# --- Formatting the Graph ---
# Set the viewing limits for the axes
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Add labels and a title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Geometric Representation of a 3D Scaled Vector')
ax.legend()

# Show the plot
plt.show()