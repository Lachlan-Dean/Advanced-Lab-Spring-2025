import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

Ic = np.array([.100, .200, .300, .400, .500])
B_g = np.array([.14925*10**-4, .5950*10**-4, 1.0490*10**-4, 1.4975*10**-4, 1.9515*10**-4])

sig_i = [.1] * len(Ic)
sig_b = [.002] * len(B_g)

mu_0 = 4 * np.pi * 10**-7
r = ufloat(.15175, 0.002)
z = ufloat(.086, 0.002)
sig_rz = 0.002 

K = ((mu_0 / 2) * r*r / (r*r + z*z)**(3/2)) 

def func(x,p):
    z = p[0] * x + p[1]
    return z

def errfunc(p, x, y,func,  err):
    return(y - func(x,p)) / err

p0 = [1, 0]

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(Ic, B_g,func, sig_b),
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
        print(f'Param {i+1}: {u:.4e} +/- {np.sqrt(covar[i,i]):.4e}')
        i = i+1
    print(f'Reduced chisq {reduced_chisq:.2f}')
else:
    print('Fitter failed (no covariance matrix).')


xfit = np.linspace(0,.55,1000)
yfit = pfinal[0]*xfit + pfinal[1]

figure, axis = plt.subplots(1, 1, sharex=False, figsize=(5,5))

axis.scatter(Ic, B_g)
axis.plot(xfit,yfit)

print(pfinal[0] / K)

plt.show()


