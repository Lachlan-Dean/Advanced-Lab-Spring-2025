import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

# loading and unpacking data
data = np.genfromtxt('WM_2scan_CL.TXT')
I = np.abs(data[:,1])
lam = data[:,0]

# dark current

dark_cur1 = I[0:30]
dark_cur2 = I[270:]
dark_cur = [*dark_cur1, *dark_cur2]

dark_curmean = np.mean(dark_cur)
dark_curstd = np.std(dark_cur, ddof=1)

I = I - dark_curmean
I_mean = np.mean(I)
I_std = np.std(I, ddof=1)
 
I_err = np.sqrt(dark_curstd**2 + ((np.abs(I) - dark_curmean)*I_std/(I_mean-dark_curmean))**2)

###############
### FITTING ###
###############
# Fitter function
def func(x, p):
    z = p[0] * np.exp(-(x - p[1]) * (x - p[1])/2./p[2]) + p[3]
    return z

def errfunc(p, x, y, func, sigma):
    return (y - func(x,p))/sigma

p0 = [1.0,435.52,.0001,.19]

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(lam,I,func,dark_curstd),
        full_output=1)

pfinal = out[0]  # final fit params
covar = out[1]   # covariance matrix - sqrt(diagonal) ˜ unc per param
mydict = out[2]  # dict, includes weighted resids (list), key=’fvec’
mesg = out[3]    # message from fitter
ier = out[4]     # error flag: success if 1, 2, 3, or 4 (or check covar)
resids = mydict['fvec']
chisq = np.sum(resids**2)
degs_frdm = len(I)-len(pfinal) # degrees of freedom
reduced_chisq = chisq/degs_frdm

print('Fitter status: ', ier, ' -- aka -- ', mesg)
i = 0
if covar is not None:
    for u in pfinal:
        print('Param', i+1, ': ', u, ' +/-', np.sqrt(covar[i,i]))
        i = i+1
    print(f'Reduced chisq {reduced_chisq:.2f}')
else:
    print('Fitter failed (no covariance matrix).')

xfit = np.linspace(np.min(lam), np.max(lam), 1000)
yfit = func(xfit, pfinal)

fig, ax = plt.subplots(1,1, figsize=(10,10))
ax.plot(xfit, yfit, color='red')
ax.scatter(lam, I, color='green')
plt.show()
plt.close()
