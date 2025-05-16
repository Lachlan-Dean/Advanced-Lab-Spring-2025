import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

hene = np.genfromtxt('HeNe_plot.TXT')
hn_lam = hene[:,0]
hn_cur = np.abs(hene[:,1]) - .195

halpha = np.genfromtxt('H_alpha_transition.TXT')
ha_lam = halpha[:,0]
ha_cur = np.abs(halpha[:,1]) - .195

std_lam = np.std(hn_lam, ddof=1)
std_cur = np.std(hn_cur, ddof=1)
cur_mean = np.mean(hn_cur)


def SFWHM(X,Y, frac):
    d = Y - (np.max(Y) / frac) 
    indexes = np.where(d >= 0)[0]
    left_ind = X[indexes[-1]]
    right_ind = X[indexes[0]]
    return np.abs(X[indexes[-1]] - X[indexes[0]]), left_ind, right_ind

# FWHM for hene
a, b, c = SFWHM(hn_lam, hn_cur, 2)
fwHE = a
HEleft = b
HEright = c
print(fwHE, HEleft, HEright)

# FWHM for H alpha
d, e, f = SFWHM(ha_lam, ha_cur, 2)
haerr = 1.920e-05
fha = ufloat(e, haerr) - ufloat(f, haerr)
ha = (ufloat(e, haerr) + ufloat(f, haerr)) / 2
print(d, e, f)

hene_peak = (b + c) / 2
tran_lam = (ufloat(b, std_lam) + ufloat(c, std_lam)) / 2
fwhmhene = ufloat(b, std_lam) - ufloat(c, std_lam)

delta = fwhmhene / tran_lam - fha / ha
fs = delta * ha

print(delta.s, delta.n)
print(fs.s, fs.n)

fig, ax = plt.subplots(1,1, figsize=(10,10))
ax.scatter(hn_lam, hn_cur)
ax.vlines(x=hene_peak, ymin=.19, ymax=np.max(hn_cur), color='red')
threshold = np.max(hn_cur) / 2
#ax.fill_between(hn_lam, 0, 1, where=hn_cur > threshold, color='green', alpha=0.5, transform=ax.get_xaxis_transform())
plt.show()
