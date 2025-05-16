import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def func(x, p):
    z = p[0] * np.exp(-(x - p[1]) * (x - p[1])/2./p[2]) + p[3]*np.exp(-(x - p[4]) * (x - p[4])/2./p[5]) + p[6]
    return z

def errfunc(p, x, y, func, sigma):
    return (y - func(x,p))/sigma


a = np.genfromtxt("part4_data-1.txt")
x = a[:,0]
y = np.abs(a[:,1])

p0 = [.3,655,.1,.6,656,.1,.19]

sigma = [3] * len(x)

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(x,y,func,sigma),
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
        print('Param', i+1, ': ', u, ' +/-', np.sqrt(covar[i,i]))
        i = i+1
    print(f'Reduced chisq {reduced_chisq:.2f}')
else:
    print('Fitter failed (no covariance matrix).')

xfit = np.linspace(655.25, 656.5,1000 )
yfit = pfinal[0] * np.exp(-(xfit - pfinal[1]) * (xfit - pfinal[1])/2./pfinal[2]) + pfinal[3]*np.exp(-(xfit - pfinal[4]) * (xfit - pfinal[4])/2./pfinal[5]) + pfinal[6]
plt.figure(figsize = (15,15))
plt.subplot(211)
p1 = plt.plot(xfit,yfit, label='Fitted Line')
p2 = plt.plot(x, y, label='Non-fitted')
p3 = plt.errorbar(x,y, yerr=.001, xerr=None, capsize=5,
    color='blue', fmt='o', label='Error', markerfacecolor='none')
plt.show()
