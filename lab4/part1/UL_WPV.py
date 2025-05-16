import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

t, pd1, pd2, err, temp, laser = np.genfromtxt('LaChris-data-Feb13-25WPV.txt', unpack=True)

figure, axis = plt.subplots(2, 2, sharex=True, figsize=(10,10))
#plt.xlim(100, 200)

# Time vs Laser plot
axis[0,0].plot(t,laser)
axis[0,0].set_title("Time vs Laser Power")

axis[0,1].plot(t, pd1)
axis[0,1].set_title("Time vs Photodiode 1")

axis[1,0].plot(t, pd2)
axis[1,0].set_title("Time vs Photodiode 2")

axis[1,1].plot(t, err)
axis[1,1].set_title("Time vs Error")

plt.show()



