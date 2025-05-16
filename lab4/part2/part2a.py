import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

t, pd1, pd2, err, temp, laser = np.genfromtxt('LaChris-data-Feb13-25LWP.txt', unpack=True)
v, theta = np.genfromtxt('data_p2a.txt', unpack=True)


figure, axis = plt.subplots(1, 2, sharex=False)

# Time vs Laser plot
axis[0].plot(t,laser, scalex=True)
axis[0].set_title("Time vs Laser Power")

plt.xlim(-90, 90)
axis[1].plot(theta, v, scalex=True)
axis[1].set_title("Angle vs DVM Reading")



plt.show()
