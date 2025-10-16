import matplotlib.pyplot as plt
import numpy as np

# Define vector u
u = np.array([-2, 3])

# Define vector v = (3/2)u
v = (3/2) * u

# Create the plot
plt.figure(figsize=(8, 8))
ax = plt.gca()

# --- Plot the vectors ---
# Plot vector u starting from the origin (0, 0)
ax.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='blue', label='u = (-2, 3)')

# Plot vector v with a tiny offset (e.g., at (0.1, 0)) to make it visually distinct
ax.quiver(0.1, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='red', label='v = 3/2u = (-3, 4.5)')

# --- Add annotations for clarity ---
# Add text labels near the arrowheads
plt.text(u[0], u[1] + 0.2, 'u', color='blue', fontsize=14)
plt.text(v[0], v[1] + 0.2, 'v', color='red', fontsize=14)


# --- Formatting the plot ---