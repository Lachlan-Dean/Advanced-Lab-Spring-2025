import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

nm_data = np.genfromtxt('Ne_NM_1scan_CL.TXT')
I_nm = np.abs(nm_data[:,1])
lam_nm = nm_data[:,0]

wm_data = np.genfromtxt('Ne_WM_1scan_CL.TXT')
I_wm = np.abs(wm_data[:,1])
lam_wm = wm_data[:,0]

mp0 = np.genfromtxt('Ne_WM_WP0_1scan_CL.TXT')
I_p0 = np.abs(mp0[:,1])
lam_p0 = mp0[:,0]

mp02 = np.genfromtxt('Ne_WM_WP0_2scan_CL.TXT')
I_p02 = np.abs(mp02[:,1])
lam_p02 = mp02[:,0]

mp90 = np.genfromtxt('Ne_WM_WP90_1scan_CL.TXT')
I_p90 = np.abs(mp90[:,1])
lam_p90 = np.abs(mp90[:,0])

mp902 = np.genfromtxt('Ne_WM_WP90_2scan_CL.TXT')
I_p902 = np.abs(mp902[:,1])
lam_p902 = np.abs(mp902[:,0])

fig, ax = plt.subplots(2,3, figsize=(15,10))
fig.suptitle('Graphs of Neon with and without Magnet and/or Polarizer', fontsize=16)
ax[0,0].scatter(lam_nm, I_nm, color='green')
ax[0,0].set_title('Initial Scan No Magnet or Polarizer')
ax[0,0].set_ylabel('Intensity (mA)')
ax[0,1].scatter(lam_wm, I_wm)
ax[0,1].set_title('Scan with Magnet, No Polarizer')
ax[0,2].scatter(lam_p0, I_p0)
ax[0,2].set_title('Initial Scan with Magnet and Polarizer set to 0')
ax[1,0].scatter(lam_p02, I_p02)
ax[1,0].set_title('Second Scan with Magnet and Polarzier set to 0')
ax[1,0].set_ylabel('Intensity (mA)')
ax[1,0].set_xlabel('Wavelength (nm)')
ax[1,1].scatter(lam_p90, I_p90)
ax[1,1].set_title('Initial Scan with Magnet and Polarizer set to 90')
ax[1,1].set_xlabel('Wavelength (nm)')
ax[1,2].scatter(lam_p902, I_p902)
ax[1,2].set_title('Second Scan with Magnet and Polarizer set to 90')
ax[1,2].set_xlabel('Wavelength (nm)')
plt.show()
plt.close()
