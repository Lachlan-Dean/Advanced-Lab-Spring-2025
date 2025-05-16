import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

def SFWHM(X,Y, frac):
    d = Y - (np.max(Y) / frac)
    indexes = np.where(d >= 0)[0]
    left_ind = X[indexes[-1]]
    right_ind = X[indexes[0]]
    return np.abs(X[indexes[-1]] - X[indexes[0]]), left_ind, right_ind

w_0 = np.genfromtxt('w_01_H_eps.TXT')
w_0cur = np.abs(w_0[:,1]) 
w_0cur = w_0cur - .195
w_0lam = w_0[:,0]

w0a, w0b, w0c = SFWHM(w_0lam, w_0cur, 2)
print(w0a)
print((w0b + w0c) / 2)

w_5 = np.genfromtxt('w_05_H_eps.TXT')
w_5cur = np.abs(w_5[:,1]) - .195
w_5lam = w_5[:,0]

w5a, w5b, w5c = SFWHM(w_5lam, w_5cur, 2)
print(w5a)
print((w5b + w5c) / 2)

w_10 = np.genfromtxt('w_10_H_eps.TXT')
w_10cur = np.abs(w_10[:,1]) - .195
w_10lam = w_10[:,0]

w10a, w10b, w10c = SFWHM(w_10lam, w_10cur, 2)
print(w10a)
print((w10b + w10c) / 2)

w_15 = np.genfromtxt('w_15_H_eps.TXT')
w_15cur = np.abs(w_15[:,1]) - .195
w_15lam = w_15[:,0]

w15a, w15b, w15c = SFWHM(w_15lam, w_15cur, 2)
print(w15a)
print((w15b + w15c) / 2)

w_20 = np.genfromtxt('w_20_H_eps.TXT')
w_20cur = np.abs(w_20[:,1]) - .195
w_20lam = w_20[:,0]

w20a, w20b, w20c = SFWHM(w_20lam, w_20cur, 2)
print(w20a)
print((w20b + w20c) / 2)

# Just 
hddata = np.genfromtxt('H_epsilon_transition.TXT')
hd_lam = hddata[:,0]
hd_cur = np.abs(hddata[:,1]) - .195

hda, hdb, hdc = SFWHM(hd_lam, hd_cur, 2)
print(hda)
print((hdb+hdc) / 2)


fwhm_array = [w0a, w5a, w10a, w15a, w20a]
width_array = [0.01, 0.05, 0.10, 0.15, 0.20]

fig, ax = plt.subplots(1, 1, figsize=(10,10))
ax.scatter(width_array, fwhm_array)
ax.set_xlabel('Slit Width (mm)')
ax.set_ylabel('FWHM (nm)')
plt.show()
plt.close()

# Quick scatter plot to check data quality and see plots
figure, axis = plt.subplots(2, 3, figsize=(10,10))
axis[1,2].set_xlabel('Wavelength (nm)')
axis[0,0].set_ylabel('Intensity (mA)')

axis[0,0].scatter(w_0lam, w_0cur)
axis[0,0].set_title('Width of 0.01mm')

axis[0,1].scatter(w_5lam, w_5cur)
axis[0,1].set_title('Width of 0.05mm')

axis[1,0].scatter(w_10lam, w_10cur)
axis[1,0].set_title('Width of 0.10mm')

axis[1,1].scatter(w_15lam, w_15cur)
axis[1,1].set_title('Width of 0.15mm')

axis[0,2].scatter(w_20lam, w_20cur)
axis[0,2].set_title('Width of 0.20mm')

axis[1,2].scatter(hd_lam, hd_cur)
axis[1,2].set_title('Basic H_delta data, Width of 0.005mm')
plt.show()
