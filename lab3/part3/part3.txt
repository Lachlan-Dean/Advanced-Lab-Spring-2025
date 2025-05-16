import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def func(x, p):
    z = p[0] + p[1] * x + p[2] * x**2
    return z

def errfunc(p, x, y, func, sigma):
    return (y - func(x,p))/sigma


x, y, sig = np.genfromtxt("part3_data.txt", unpack=True)

p0 = [100,4000,1]

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(x,y,func,sig),
        full_output=1)

pfinal = out[0]  # final fit params
covar = out[1]   # covariance matrix - sqrt(diagonal) ˜ unc per param
mydict = out[2]  # dict, includes weighted resids (list), key=’fvec’
mesg = out[3]    # message from fitter
ier = out[4]     # error flag: success if 1, 2, 3, or 4 (or check covar)
resids = mydict['fvec']
chisq = np.sum(resids**2)
degs_frdm = len(x)-len(pfinal) # degrees of freedom
reduced_chisq = chisq/degs_frdm

print('Fitter status: ', ier, ' -- aka -- ', mesg)
i = 0
if covar is not None:
    for u in pfinal:
        print(f'Param {i+1}: {u:.2f} +/- {covar[i,i]:.2f}')
        i = i+1
    print(f'Reduced chisq {reduced_chisq:.2f}')
else:
    print('Fitter failed (no covariance matrix).')

#plt.scatter(x, resids)


xfit = np.linspace(0, 30, 1500)
yfit = pfinal[0] + pfinal[1] * xfit + pfinal[2] * xfit**2
plt.figure(figsize=(10,10))
plt.subplot(211)
p1 = plt.scatter(x, y, color='blue')
p2 = plt.plot(xfit, yfit, 'k', label = 'Fitted Data') # ’k’: black; line is assumed.
plt.show()

