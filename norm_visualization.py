import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generating points
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30)
z = np.linspace(-1, 1, 30)
x, y, z = np.meshgrid(x, y, z)

# Euclidean norm
euclidean_norm = np.sqrt(x**2 + y**2 + z**2)

# Manhattan norm
manhattan_norm = np.abs(x) + np.abs(y) + np.abs(z)

# Infinity norm
infinity_norm = np.maximum(np.maximum(np.abs(x), np.abs(y)), np.abs(z))

# Plotting
fig = plt.figure(figsize=(18, 6))

# Euclidean norm plot
ax1 = fig.add_subplot(131, projection='3d')
ax1.scatter(x[euclidean_norm <= 1], y[euclidean_norm <= 1], z[euclidean_norm <= 1], c='blue', s=1)
ax1.set_title('Euclidean Norm (L2)')
ax1.set_xlim([-1, 1])
ax1.set_ylim([-1, 1])
ax1.set_zlim([-1, 1])

# Manhattan norm plot
ax2 = fig.add_subplot(132, projection='3d')
ax2.scatter(x[manhattan_norm <= 1], y[manhattan_norm <= 1], z[manhattan_norm <= 1], c='green', s=1)
ax2.set_title('Manhattan Norm (L1)')
ax2.set_xlim([-1, 1])
ax2.set_ylim([-1, 1])
ax2.set_zlim([-1, 1])

# Infinity norm plot
ax3 = fig.add_subplot(133, projection='3d')
ax3.scatter(x[infinity_norm <= 1], y[infinity_norm <= 1], z[infinity_norm <= 1], c='red', s=1)
ax3.set_title('Infinity Norm (L∞)')
ax3.set_xlim([-1, 1])
ax3.set_ylim([-1, 1])
ax3.set_zlim([-1, 1])

plt.tight_layout()
plt.show()
