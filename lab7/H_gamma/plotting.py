import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

HBT_data = np.genfromtxt('H_gamma_transition.TXT')
HB_lambda = HBT_data[:,0]
HB_cur = HBT_data[:,1]

bf_data = np.genfromtxt('flicker6to2_data.dat')
HBF_cur = bf_data[:,1]

figure, axis = plt.subplots(1,1, figsize=(10,10))
axis.scatter(HB_lambda,np.abs(HB_cur))
axis.set_title("H Beta Transition")
plt.show()
plt.close()

# Splicing data to only the peaks
just_HT = np.abs(HBT_data[460:560])
just_HTcur = just_HT[:,1]
just_HTlam = just_HT[:,0]
just_DT = np.abs(HBT_data[230:320])
just_DTcur = just_DT[:,1]
just_DTlam = just_DT[:,0]


figure, axis = plt.subplots(1,1, figsize=(10,10))
axis.scatter(just_HTlam,just_HTcur)
axis.scatter(just_DTlam,just_DTcur)
plt.show()
plt.close()

