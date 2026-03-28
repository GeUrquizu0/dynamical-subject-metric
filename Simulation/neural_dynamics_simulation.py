import numpy as np
import matplotlib.pyplot as plt

# number of neurons
N = 20

# random connectivity
W = np.random.randn(N, N) * 0.3

# simulation parameters
dt = 0.01
T = 1000

x = np.random.randn(N)

trajectory = []

for t in range(T):

    noise = 0.05 * np.random.randn(N)

    dx = -x + np.tanh(W @ x) + noise

    x = x + dt * dx

    trajectory.append(x.copy())

trajectory = np.array(trajectory)

plt.plot(trajectory[:,0])
plt.title("Example neural trajectory")
plt.show()
