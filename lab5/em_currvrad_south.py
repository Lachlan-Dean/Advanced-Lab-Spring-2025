import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

Ic, Rc  = np.genfromtxt('em_current_radii_south.txt', unpack=True)

mu_0 = 4 * np.pi * 10**-7
n = 130
chg_v = ufloat(240, 0.1)
std_rc = np.std(1/Rc)

rc = ufloat(0.165, 0.02)
z = rc / 2


K = (mu_0 / 2) * (rc**2) / ((rc**2 + z**2)**(3/2))*2*n

B = K * Ic

def func(x, p):
    z = p[0] * x + p[1]
    return z

def errfunc(p, x, y, err):
    return(y - func(x,p)) / err

sig = std_rc * len(Rc)
p0 = [1, 0]

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(Ic, 1/Rc, sig),
        full_output=1)

pfinal = out[0]  # final fit params
covar = out[1]   # covariance matrix - sqrt(diagonal) ˜ unc per param
mydict = out[2]  # dict, includes weighted resids (list), key=’fvec’
mesg = out[3]    # message from fitter
ier = out[4]     # error flag: success if 1, 2, 3, or 4 (or check covar)
resids = mydict['fvec']
chisq = np.sum(resids**2)
degs_frdm = len(Ic)-len(pfinal) # degrees of freedom
reduced_chisq = chisq/degs_frdm

print('Fitter status: ', ier, ' -- aka -- ', mesg)
i = 0
if covar is not None:
    for u in pfinal:
        print(f'Param {i+1}: {u:.2f} +/- {np.sqrt(covar[i,i]):.2f}')
        i = i+1
    print(f'Reduced chisq {reduced_chisq:.5f}')
else:
    print('Fitter failed (no covariance matrix).')


xfit = np.linspace(0, 2, 1000)
yfit = pfinal[0]*xfit + pfinal[1]

# Data scatter
figure, axis = plt.subplots(1, 1, sharex=True, figsize=(5,5))

axis.scatter(Ic,1/Rc, label='Current vs 1/R')
axis.plot(xfit, yfit)
axis.errorbar(Ic, 1/Rc, yerr=1/0.2, xerr=None, color='red', fmt='s')

pfinal_wunc = ufloat(pfinal[0], covar[1,1])
print(B)
em =  (pfinal[0])**2 * 2 * chg_v / K**2  
print(f'{em:.2e}')
plt.show()
