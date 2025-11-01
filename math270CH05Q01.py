import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Create the 3D plot ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Setup the plot ---
ax.set_title("Vector Cross Product: j × i = -k", fontsize=16)
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_xlabel('X-axis (i)', fontsize=12)
ax.set_ylabel('Y-axis (j)', fontsize=12)
ax.set_zlabel('Z-axis (k)', fontsize=12)
# Set a good viewing angle
ax.view_init(elev=20, azim=30)

# --- Draw faint coordinate axes ---
ax.plot([-1.5, 1.5], [0, 0], [0, 0], 'k--', alpha=0.3, label='X-axis') # X-axis
ax.plot([0, 0], [-1.5, 1.5], [0, 0], 'k--', alpha=0.3, label='Y-axis') # Y-axis
ax.plot([0, 0], [0, 0], [-1.5, 1.5], 'k--', alpha=0.3, label='Z-axis') # Z-axis

# --- Define and plot the vectors ---
# Vector j (0, 1, 0)
ax.quiver(0, 0, 0, 0, 1, 0, color='blue', arrow_length_ratio=0.15, linewidth=2, label='j')
# Vector i (1, 0, 0)
ax.quiver(0, 0, 0, 1, 0, 0, color='red', arrow_length_ratio=0.15, linewidth=2, label='i')
# Result vector -k (0, 0, -1)
ax.quiver(0, 0, 0, 0, 0, -1, color='green', arrow_length_ratio=0.15, linewidth=3, label='j × i = -k')

# --- Add labels to the vectors ---
ax.text(1.1, 0, 0, 'i', color='red', fontsize=14)
ax.text(0, 1.1, 0, 'j', color='blue', fontsize=14)
ax.text(0, 0, -1.2, '-k (Result)', color='green', fontsize=14)

# --- Show the plot ---
plt.show()
