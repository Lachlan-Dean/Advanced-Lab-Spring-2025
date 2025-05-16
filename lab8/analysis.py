import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties.umath import *

stokes_data = np.genfromtxt('1secAQ_pack_cooler_heat127_stokes.txt')
dis = stokes_data[:,0]
stokes = stokes_data[:,1]
astokes = stokes_data[:,2]
temp_data = np.genfromtxt('1secAQ_pack_cooler_heat127temp.txt')
temp = temp_data[:,1]

# Chop values to only outside the DTS
dis_out = dis[655:771]
stokes_out = stokes[655:771]
astokes_out = stokes[655:771]
temp_out = temp[655:771]

figure, axis = plt.subplots(1, 3, figsize=(17,8))
axis[0].plot(dis, stokes)
axis[0].vlines(x=0, ymin=0, ymax=np.max(stokes), color='r', ls='--')
axis[0].set_xlabel('Distance (m)')
axis[0].set_ylabel('Amplitude')
axis[1].plot(dis,astokes, color='orange')
axis[1].set_xlabel('Distance (m)')
axis[1].vlines(x=0, ymin=0, ymax=np.max(stokes), color='r', ls='--')
axis[2].plot(dis,stokes)
axis[2].plot(dis,astokes)
axis[2].set_xlabel('Distance (m)')
axis[2].vlines(x=0, ymin=0, ymax=np.max(stokes), color='r', ls='--')
#plt.show()
plt.close()

figure2, axis2 = plt.subplots(1,1, figsize=(10,10))
axis2.plot(dis, temp)
axis2.vlines(x=0, ymin=0, ymax=np.max(temp), color='r', ls='--')
axis2.set_ylabel('Temperature (Degrees Celsius)')
axis2.set_xlabel('Distance (m)')
#plt.show()
plt.close()

# stan dev for temp
t_sig = np.std(temp_out, ddof=1)

# differential loss
da = 0.25 * (np.log(10) / 10000)

# temperature scaling factor
gamma = 482.000

# temp offset
toffset = 0

# Fitter function
def func(x, p):
    z = (gamma / (p[0] + (da*x) + np.log(stokes[650:771]/astokes[650:771]))) + (toffset - 273.15)
    return z

p0 = [1.4]

def errfunc(p, x, y, func, sigma):
    return (y - func(x,p))/sigma

out = sp.optimize.leastsq(errfunc,
        p0,
        args=(dis[650:771],temp[650:771],func,0.005),
        full_output=1)

pfinal = out[0]  # final fit params
covar = out[1]   # covariance matrix - sqrt(diagonal) ˜ unc per param
mydict = out[2]  # dict, includes weighted resids (list), key=’fvec’
mesg = out[3]    # message from fitter
ier = out[4]     # error flag: success if 1, 2, 3, or 4 (or check covar)
resids = mydict['fvec']
chisq = np.sum(resids**2)
degs_frdm = len(dis)-len(pfinal) # degrees of freedom
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

xfit = np.linspace(np.min(dis[650:771]), np.max(dis[650:771]), len(stokes[650:771]))
yfit = func(xfit, pfinal)

fig, ax = plt.subplots(1,1, figsize=(10,10))
ax.plot(xfit, yfit, color='green')
ax.vlines(x=0, ymin=0, ymax=np.max(temp), color='r', ls='--')
ax.plot(dis[650:771], temp[650:771], color='black', ls='--')
ax.set_ylabel('Temperature (Degrees Celsius)')
ax.set_xlabel('Distance (m)')
#plt.show()
plt.close()

fig2, ax2 = plt.subplots(1,1, figsize=(10,10))
ax2.scatter(dis[650:771], resids)
ax2.set_ylabel('Temperature (Degrees Celsius)')
ax2.set_xlabel('Distance (m)')
plt.show()
plt.close()


