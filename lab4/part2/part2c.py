import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# LaChris-data-Feb13-25LW45QP.txt  LaChris-data-Feb13-25LWQP.txt  data_p2c_45.txt  data_p2c_90.txt

t, pd1, pd2, err, temp, laser = np.genfromtxt('LaChris-data-Feb13-25LWQP.txt', unpack=True)
t2, pd12, pd22, err2, temp2, laser2 = np.genfromtxt('LaChris-data-Feb13-25LW45QP.txt', unpack=True)
v90, theta90 = np.genfromtxt('data_p2c_90.txt', unpack=True)
v45, theta45 = np.genfromtxt('data_p2c_45.txt', unpack=True)

figure, axis = plt.subplots(2, 2, sharex=False)

# Time vs Laser plot
axis[0,0].set_xlim(1350, 1600)
axis[0,0].plot(t,laser)
axis[0,0].set_title("Time vs Laser Power with 90 degree Polarizer")

axis[0,1].set_xlim(100,350)
axis[0,1].plot(t2, laser2)
axis[0,1].set_title("Time vs Laser Power with 45 degree Polarizer")

axis[1,0].set_xlim(80,260)
axis[1,0].plot(theta90, v90)
axis[1,0].set_title("Angle vs DVM Reading with 90 degree Polarizer")

axis[1,1].set_xlim(-90,80)
axis[1,1].plot(theta45, v45)
axis[1,1].set_title("Angle vs DVM Reading with 90 degree Polarizer")
plt.show()
