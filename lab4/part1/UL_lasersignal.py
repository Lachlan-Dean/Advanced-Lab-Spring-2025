import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

t, pd1, pd2, err, temp, laser = np.genfromtxt('LaChris-data-Feb13-25NP.txt', unpack=True)

figure, axis = plt.subplots(1, 1, sharex=True, figsize=(10,10))

plt.xlim(100, 200)

# Time vs Laser plot
axis.plot(t,laser)
axis.set_title("Time vs Laser Power")

plt.show()

