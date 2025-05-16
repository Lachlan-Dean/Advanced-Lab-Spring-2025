import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

phi2, ang2, volts2 = np.genfromtxt('data2.txt', unpack=True)
volts2 = volts2 - .0005

sig_phi = [.5] * len(phi2)
sig_v = [.005] * len(volts2)

# Transverse electric
theta2 = 90 - phi2/2

n1 = 1.0003

def func(x,p):
    x = (np.pi / 180) * x
    n = p[0] / n1
    E_r = (np.cos(x)) - (n**2 - (np.sin(x))**2)**(1/2)
    E = (np.cos(x)) + (n**2 - (np.sin(x))**2)**(1/2)
    z = (E_r / E)**2 * p[1] + p[2]
    return z

def errfunc(p, x, y,func,err):
    return(y - func(x,p)) / err

p0 = [1.5,1,.8]

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(theta2, volts2, func, sig_v),
        full_output=1)

pfinal = out[0]  # final fit params
covar = out[1]   # covariance matrix - sqrt(diagonal) ˜ unc per param
mydict = out[2]  # dict, includes weighted resids (list), key=’fvec’
mesg = out[3]    # message from fitter
ier = out[4]     # error flag: success if 1, 2, 3, or 4 (or check covar)
resids = mydict['fvec']
chisq = np.sum(resids**2)
degs_frdm = len(theta2)-len(pfinal) # degrees of freedom
reduced_chisq = chisq/degs_frdm

print('Fitter status: ', ier, ' -- aka -- ', mesg)
i = 0
if covar is not None:
    for u in pfinal:
        print(f'Param {i+1}: {u:.4e} +/- {np.sqrt(covar[i,i]):.4e}')
        i = i+1
    print(f'Reduced chisq {reduced_chisq}')
else:
    print('Fitter failed (no covariance matrix).')

xfit = np.linspace(20,90, 100)
yfit = func(xfit, pfinal)

# Brewster Angle Calculation: n2 = tan(theta_b)
n2 = ufloat((-1)*pfinal[0], covar[1,1])
n = n2/n1
theta_b = atan(n)
print(theta_b*180/np.pi)

figure, axis = plt.subplots(1, 1, sharex=True, figsize=(10,7.5))
axis.scatter(theta2, volts2)
axis.plot(xfit, yfit)
axis.set_xlabel('Angle of Incidence')
axis.set_ylabel('Intensity of Transverse Electric')
axis.errorbar(theta2, volts2, yerr=.005, xerr=None, color='red', fmt='|')
plt.show()

