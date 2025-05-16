import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

t, pd1, pd2, err, temp, laser = np.genfromtxt('LaChris-data-Feb13-25NP.txt', unpack=True)

#x = t.reshape(100, 200)

figure, axis = plt.subplots(2, 2, sharex=True, figsize=(10,10))
plt.xlim(100, 200)

axis[0,0].plot(t, pd1)
axis[0,0].set_title("Time vs Photodiode 1")

axis[1,0].plot(t, pd2)
axis[1,0].set_title("Time vs Photodiode 2")

axis[1,1].plot(t, err)
axis[1,1].set_title("Time vs Error")

axis[0,1].plot(t, err)
axis[0,1].plot(t, pd1)
axis[0,1].plot(t, pd2)
axis[0,1].set_title("Time vs PD1, PD2 & Error")

plt.show()

