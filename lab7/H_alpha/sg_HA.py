import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

# Data
HAT_data = np.genfromtxt('H_alpha_transition.TXT')
HA_lambda = HAT_data[:,0]
HA_cur = HAT_data[:,1]

# Flicker data (Took Chris' data as my flicker for 3to2 was improperly measured
af_data = np.genfromtxt('Chris_flicker_H_alpha.dat')
HAF_cur = af_data[:,1]
HA_mean = np.mean(np.abs(HAF_cur))


# Splicing data to only the peaks 
just_HT = np.abs(HAT_data[600:750])
just_HTcur = just_HT[:,1]
just_HTlam = just_HT[:,0]
HA_mean = np.mean(np.abs(HAF_cur))
HA_std = np.std(np.abs(HAF_cur), ddof=1)

# Background intensity
dark_cur = np.abs(HA_cur[1:200])
dark_curmean = np.mean(dark_cur)
std_dark = np.std(dark_cur)

# Calculating quad
HA_mean = HA_mean - dark_curmean
HA_err = np.sqrt(std_dark**2 + ((np.abs(just_HTcur) - dark_curmean)*HA_std/(HA_mean-dark_curmean))**2)

# Fitter function
def func(x, p):
    z = p[0] * np.exp(-(x - p[1]) * (x - p[1])/2./p[2]) + p[3]
    return z

def errfunc(p, x, y, func, sigma):
    return (y - func(x,p))/sigma

p0 = [.85,656.04,.0001,.2]

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(just_HTlam,just_HTcur,func,HA_err),
        full_output=1)

pfinal = out[0]  # final fit params
covar = out[1]   # covariance matrix - sqrt(diagonal) ˜ unc per param
mydict = out[2]  # dict, includes weighted resids (list), key=’fvec’
mesg = out[3]    # message from fitter
ier = out[4]     # error flag: success if 1, 2, 3, or 4 (or check covar)
resids = mydict['fvec']
chisq = np.sum(resids**2)
degs_frdm = len(just_HTlam)-len(pfinal) # degrees of freedom
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

xfit = np.linspace(np.min(just_HTlam),np.max(just_HTlam), 1000)
yfit = func(xfit, pfinal)

# Plotting
fig, ax = plt.subplots(1,1, figsize=(10,7.5))
ax.scatter(just_HTlam, just_HTcur)
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Intensity (mA)')
#ax.scatter(HA_lambda, np.abs(HA_cur))
ax.plot(xfit, yfit)
ax.errorbar(just_HTlam,just_HTcur, yerr=HA_err, fmt='|', capsize=5)
plt.show()
plt.close()
